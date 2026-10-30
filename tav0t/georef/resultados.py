"""Georreferenciación de nodos y procesamiento de resultados del análisis."""

from __future__ import annotations

import math
from dataclasses import dataclass, field

from .modelo import CasoResultados, ModeloEstructural
from .transformacion import Georreferencia, _a_z_arriba, factor_unidad
from .utm import geodesicas_a_utm


@dataclass
class NodoGeorreferenciado:
    id: str
    x: float
    y: float
    z: float
    lat: float
    lon: float
    h: float  # altura elipsoidal (m)
    altura_ortometrica: float  # h − N (m)
    este: float
    norte: float
    zona: int
    hemisferio: str
    desplazamiento_enu: tuple[float, float, float] | None = None  # (m)
    posicion_deformada: tuple[float, float, float] | None = None  # (lat, lon, h)

    @property
    def desplazamiento_total(self) -> float | None:
        if self.desplazamiento_enu is None:
            return None
        return math.sqrt(sum(c * c for c in self.desplazamiento_enu))

    @property
    def desplazamiento_horizontal(self) -> float | None:
        if self.desplazamiento_enu is None:
            return None
        return math.hypot(self.desplazamiento_enu[0], self.desplazamiento_enu[1])

    @property
    def acimut_desplazamiento(self) -> float | None:
        """Hacia dónde se mueve el nodo en planta (grados desde el norte verdadero)."""
        if self.desplazamiento_enu is None or self.desplazamiento_horizontal < 1e-12:
            return None
        return math.degrees(math.atan2(self.desplazamiento_enu[0], self.desplazamiento_enu[1])) % 360.0


def georreferenciar_modelo(
    modelo: ModeloEstructural,
    georef: Georreferencia,
    caso: CasoResultados | None = None,
    zona: int | None = None,
    ondulacion_geoidal: float = 0.0,
    factor_deformada: float = 0.0,
) -> list[NodoGeorreferenciado]:
    """Calcula la posición en la Tierra de cada nodo y, si hay un caso de
    resultados, su desplazamiento en ejes ENU y su posición deformada.

    Todos los nodos se proyectan en la misma zona UTM (la del punto de amarre
    salvo que se fuerce otra), para que las coordenadas sean continuas.
    """
    if zona is None:
        zona = geodesicas_a_utm(georef.lat0, georef.lon0, elipsoide=georef.elipsoide).zona
    f_modelo = factor_unidad(modelo.unidades)
    f_result = factor_unidad(caso.unidades) if caso else 1.0

    salida = []
    for nodo in modelo.nodos.values():
        lat, lon, h = georef.modelo_a_geodesicas(nodo.x, nodo.y, nodo.z)
        utm = geodesicas_a_utm(lat, lon, zona, georef.elipsoide)
        ng = NodoGeorreferenciado(
            nodo.id,
            nodo.x,
            nodo.y,
            nodo.z,
            lat,
            lon,
            h,
            h - ondulacion_geoidal,
            utm.este,
            utm.norte,
            utm.zona,
            utm.hemisferio,
        )
        if caso and nodo.id in caso.desplazamientos:
            ux, uy, uz = caso.desplazamientos[nodo.id]
            ng.desplazamiento_enu = georef.rotar_vector(ux, uy, uz, f_result)
            if factor_deformada:
                # El desplazamiento se pasa a unidades del modelo y se amplifica.
                r = f_result / f_modelo * factor_deformada
                ng.posicion_deformada = georef.modelo_a_geodesicas(nodo.x + ux * r, nodo.y + uy * r, nodo.z + uz * r)
        salida.append(ng)
    return salida


# --- Derivas de entrepiso ------------------------------------------------------


@dataclass
class DerivaPiso:
    nivel_inferior: float  # cota en m (sistema del modelo, Z vertical)
    nivel_superior: float
    altura: float
    deriva_x: float  # máximo valor absoluto entre las columnas del piso
    deriva_y: float
    deriva_resultante: float
    nodo_critico: str
    limite: float | None = None

    @property
    def relacion_limite(self) -> float | None:
        if not self.limite:
            return None
        return self.deriva_resultante / self.limite

    @property
    def cumple(self) -> bool | None:
        if not self.limite:
            return None
        return self.deriva_resultante <= self.limite

    def como_dict(self) -> dict:
        return {
            "nivel_inferior_m": self.nivel_inferior,
            "nivel_superior_m": self.nivel_superior,
            "altura_m": self.altura,
            "deriva_x": self.deriva_x,
            "deriva_y": self.deriva_y,
            "deriva_resultante": self.deriva_resultante,
            "nodo_critico": self.nodo_critico,
            "limite": self.limite,
            "relacion_limite": self.relacion_limite,
            "cumple": self.cumple,
        }


def _agrupar_niveles(cotas: list[float], tolerancia: float) -> list[float]:
    niveles: list[list[float]] = []
    for c in sorted(cotas):
        if niveles and c - niveles[-1][-1] <= tolerancia:
            niveles[-1].append(c)
        else:
            niveles.append([c])
    return [sum(g) / len(g) for g in niveles]


def calcular_derivas(
    modelo: ModeloEstructural,
    caso: CasoResultados,
    factor_amplificacion: float = 1.0,
    limite: float | None = None,
    tolerancia: float = 0.01,
) -> list[DerivaPiso]:
    """Deriva de entrepiso por columna: Δ = (δ_sup − δ_inf) / h.

    * Los niveles se forman agrupando las cotas de los nodos con la tolerancia
      dada (en metros).
    * Para cada nodo de un nivel se busca el nodo situado en la misma vertical
      (misma planta x, y dentro de la tolerancia) en el nivel inferior más
      cercano que lo tenga. Cada pareja es una "columna".
    * La deriva del piso es la mayor entre sus columnas, en dirección X e Y del
      modelo (que es como la piden las normas) y resultante.
    * ``factor_amplificacion`` multiplica las derivas cuando los
      desplazamientos son elásticos y la norma pide inelásticos (Cd, 0.75·R…).
    """
    f_modelo = factor_unidad(modelo.unidades)
    f_result = factor_unidad(caso.unidades)
    puntos = {}
    for nid, d in caso.desplazamientos.items():
        nodo = modelo.nodos.get(nid)
        if nodo is None:
            continue
        pos = _a_z_arriba(nodo.x * f_modelo, nodo.y * f_modelo, nodo.z * f_modelo, modelo.eje_vertical)
        despl = _a_z_arriba(d[0] * f_result, d[1] * f_result, d[2] * f_result, modelo.eje_vertical)
        puntos[nid] = (pos, despl)
    if not puntos:
        return []

    niveles = _agrupar_niveles([p[0][2] for p in puntos.values()], tolerancia)

    def indice_nivel(z: float) -> int:
        return min(range(len(niveles)), key=lambda i: abs(niveles[i] - z))

    celda = max(tolerancia, 1e-6)
    # Índice espacial por nivel: celda en planta -> nodos.
    por_nivel: list[dict[tuple[int, int], list[str]]] = [dict() for _ in niveles]
    for nid, (pos, _) in puntos.items():
        clave = (math.floor(pos[0] / celda), math.floor(pos[1] / celda))
        por_nivel[indice_nivel(pos[2])].setdefault(clave, []).append(nid)

    def buscar_debajo(nivel: int, x: float, y: float) -> str | None:
        cx, cy = math.floor(x / celda), math.floor(y / celda)
        for inferior in range(nivel - 1, -1, -1):
            mejor, dist_mejor = None, tolerancia
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for nid in por_nivel[inferior].get((cx + dx, cy + dy), ()):
                        p = puntos[nid][0]
                        dist = math.hypot(p[0] - x, p[1] - y)
                        if dist <= dist_mejor:
                            mejor, dist_mejor = nid, dist
            if mejor is not None:
                return mejor
        return None

    pisos: dict[tuple[int, int], DerivaPiso] = {}
    for i in range(1, len(niveles)):
        for celda_nodos in por_nivel[i].values():
            for nid in celda_nodos:
                (x, y, z), (ux, uy, _) = puntos[nid]
                abajo = buscar_debajo(i, x, y)
                if abajo is None:
                    continue
                (_, _, z_inf), (ux_inf, uy_inf, _) = puntos[abajo]
                h = z - z_inf
                if h <= tolerancia:
                    continue
                dx = abs(ux - ux_inf) / h * factor_amplificacion
                dy = abs(uy - uy_inf) / h * factor_amplificacion
                dr = math.hypot(ux - ux_inf, uy - uy_inf) / h * factor_amplificacion
                clave = (indice_nivel(z_inf), i)
                piso = pisos.get(clave)
                if piso is None:
                    pisos[clave] = DerivaPiso(niveles[clave[0]], niveles[i], h, dx, dy, dr, nid, limite)
                else:
                    piso.deriva_x = max(piso.deriva_x, dx)
                    piso.deriva_y = max(piso.deriva_y, dy)
                    if dr > piso.deriva_resultante:
                        piso.deriva_resultante = dr
                        piso.nodo_critico = nid
    return [pisos[k] for k in sorted(pisos)]


# --- Escala de colores -----------------------------------------------------------

# Semáforo: verde, amarillo, naranja, rojo (RGB hexadecimal).
PALETA_SEMAFORO = ("#2e9e44", "#e8c31c", "#f07c1a", "#d62828")


@dataclass
class EscalaColores:
    """Clasifica un valor en tramos: [−∞, u1), [u1, u2), …, [un, +∞)."""

    umbrales: list[float]
    colores: tuple[str, ...] = field(default=PALETA_SEMAFORO)

    def __post_init__(self) -> None:
        if sorted(self.umbrales) != list(self.umbrales):
            raise ValueError("Los umbrales deben estar en orden creciente.")
        if len(self.colores) != len(self.umbrales) + 1:
            raise ValueError("Debe haber exactamente un color más que umbrales.")

    def clase(self, valor: float | None) -> int | None:
        if valor is None:
            return None
        for i, u in enumerate(self.umbrales):
            if valor < u:
                return i
        return len(self.umbrales)

    def color(self, valor: float | None) -> str | None:
        i = self.clase(valor)
        return None if i is None else self.colores[i]


def metrica_elementos(
    modelo: ModeloEstructural,
    nodos_geo: list[NodoGeorreferenciado],
    caso: CasoResultados | None,
    metrica: str,
) -> dict[str, float]:
    """Valor escalar por elemento para colorear el mapa.

    Si ``metrica`` existe en los resultados de elementos del caso (por ejemplo
    ``relacion_dc``), se usa directamente. Si es ``desplazamiento``, se toma el
    máximo desplazamiento total de los nodos del elemento.
    """
    valores: dict[str, float] = {}
    if caso is None:
        return valores
    if metrica == "desplazamiento":
        por_id = {n.id: n.desplazamiento_total for n in nodos_geo}
        for el in modelo.elementos.values():
            vals = [por_id[n] for n in el.nodos if por_id.get(n) is not None]
            if vals:
                valores[el.id] = max(vals)
        return valores
    for eid, res in caso.elementos.items():
        if eid in modelo.elementos and metrica in res:
            valores[eid] = res[metrica]
    return valores
