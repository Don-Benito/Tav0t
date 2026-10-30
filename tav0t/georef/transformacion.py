"""Georreferenciación del modelo estructural.

Cadena de transformación (ida):

    modelo (x, y, z) [unidades del modelo]
      │ 1. restar punto de amarre del modelo (x0, y0, z0)
      │ 2. reordenar ejes si el modelo usa Y vertical
      │ 3. pasar a metros (factor de unidad) y aplicar escala (1 si es rígido)
      │ 4. rotar en planta según el acimut del eje X del modelo
      ▼
    ENU (E, N, U) [m] con origen en el punto de amarre geodésico
      ▼
    ECEF ──► geodésicas (φ, λ, h) ──► UTM (E, N, zona) si se pide

El modelo se coloca en el plano tangente local (ENU) y no directamente en UTM,
porque la cuadrícula UTM distorsiona las distancias (factor k entre 0.9996 y
~1.001) y su norte no es el verdadero. Así la geometría del modelo se conserva
exactamente y la proyección se aplica solo al final, punto por punto.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Sequence

from .elipsoide import WGS84, Elipsoide
from .geodesia import MarcoENU, Vector3
from .utm import CoordenadaUTM, geodesicas_a_utm

UNIDADES_LONGITUD = {
    "m": 1.0,
    "cm": 0.01,
    "mm": 0.001,
    "km": 1000.0,
    "ft": 0.3048,
    "in": 0.0254,
}


def factor_unidad(unidad: str) -> float:
    try:
        return UNIDADES_LONGITUD[unidad.lower()]
    except KeyError:
        disponibles = ", ".join(UNIDADES_LONGITUD)
        raise ValueError(f"Unidad de longitud desconocida '{unidad}'. Disponibles: {disponibles}") from None


def _normalizar_acimut(grados: float) -> float:
    return grados % 360.0


def _a_z_arriba(x: float, y: float, z: float, eje_vertical: str) -> Vector3:
    """Convierte un sistema con Y vertical a uno dextrógiro con Z vertical."""
    if eje_vertical == "Z":
        return x, y, z
    return x, -z, y


def _desde_z_arriba(x: float, y: float, z: float, eje_vertical: str) -> Vector3:
    if eje_vertical == "Z":
        return x, y, z
    return x, z, -y


@dataclass
class Georreferencia:
    """Parámetros que fijan el modelo local en la Tierra.

    Atributos:
        lat0, lon0, h0: punto de amarre geodésico (grados, grados, metros de
            altura **elipsoidal**).
        acimut_x: acimut verdadero del eje +X del modelo, en grados, medido en
            sentido horario desde el norte geográfico.
        punto_modelo: coordenadas del modelo (en sus unidades) que coinciden
            con el punto de amarre geodésico.
        unidad: factor que convierte las unidades del modelo a metros.
        escala: factor adicional; 1.0 para un modelo rígido (lo normal).
        eje_vertical: "Z" (SAP2000, ETABS, la mayoría) o "Y".
    """

    lat0: float
    lon0: float
    h0: float
    acimut_x: float
    punto_modelo: Vector3 = (0.0, 0.0, 0.0)
    unidad: float = 1.0
    escala: float = 1.0
    eje_vertical: str = "Z"
    elipsoide: Elipsoide = WGS84
    _marco: MarcoENU = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if not -90.0 <= self.lat0 <= 90.0:
            raise ValueError(f"Latitud de origen inválida: {self.lat0}")
        if not -180.0 <= self.lon0 <= 180.0:
            raise ValueError(f"Longitud de origen inválida: {self.lon0}")
        if self.eje_vertical not in ("Z", "Y"):
            raise ValueError("eje_vertical debe ser 'Z' o 'Y'")
        if self.unidad <= 0 or self.escala <= 0:
            raise ValueError("unidad y escala deben ser positivas")
        self.acimut_x = _normalizar_acimut(self.acimut_x)
        self.punto_modelo = tuple(float(v) for v in self.punto_modelo)  # type: ignore[assignment]
        self._marco = MarcoENU(self.lat0, self.lon0, self.h0, self.elipsoide)
        alfa = math.radians(self.acimut_x)
        self._sin = math.sin(alfa)
        self._cos = math.cos(alfa)

    # --- Constructores ------------------------------------------------------

    @classmethod
    def parametrica(
        cls,
        lat0: float,
        lon0: float,
        h0: float,
        acimut_x: float,
        norte: str = "verdadero",
        zona: int | None = None,
        **kwargs,
    ) -> "Georreferencia":
        """Crea la georreferencia a partir de un punto y un acimut.

        Si el acimut se midió sobre un plano en coordenadas UTM
        (``norte="cuadricula"``), se corrige con la convergencia de meridianos
        en el punto de amarre: acimut verdadero = acimut de cuadrícula + γ.
        """
        if norte not in ("verdadero", "cuadricula"):
            raise ValueError("norte debe ser 'verdadero' o 'cuadricula'")
        elipsoide = kwargs.get("elipsoide", WGS84)
        if norte == "cuadricula":
            gamma = geodesicas_a_utm(lat0, lon0, zona, elipsoide).convergencia
            acimut_x = acimut_x + gamma
        return cls(lat0, lon0, h0, acimut_x, **kwargs)

    # --- Puntos -------------------------------------------------------------

    def modelo_a_enu(self, x: float, y: float, z: float) -> Vector3:
        x0, y0, z0 = self.punto_modelo
        f = self.unidad * self.escala
        dx, dy, dz = _a_z_arriba((x - x0) * f, (y - y0) * f, (z - z0) * f, self.eje_vertical)
        return (
            dx * self._sin - dy * self._cos,
            dx * self._cos + dy * self._sin,
            dz,
        )

    def enu_a_modelo(self, e: float, n: float, u: float) -> Vector3:
        x0, y0, z0 = self.punto_modelo
        f = self.unidad * self.escala
        dx = e * self._sin + n * self._cos
        dy = -e * self._cos + n * self._sin
        mx, my, mz = _desde_z_arriba(dx, dy, u, self.eje_vertical)
        return x0 + mx / f, y0 + my / f, z0 + mz / f

    def modelo_a_geodesicas(self, x: float, y: float, z: float) -> Vector3:
        return self._marco.a_geodesicas(*self.modelo_a_enu(x, y, z))

    def geodesicas_a_modelo(self, lat: float, lon: float, h: float) -> Vector3:
        return self.enu_a_modelo(*self._marco.desde_geodesicas(lat, lon, h))

    def modelo_a_utm(self, x: float, y: float, z: float, zona: int | None = None) -> tuple[CoordenadaUTM, float]:
        lat, lon, h = self.modelo_a_geodesicas(x, y, z)
        return geodesicas_a_utm(lat, lon, zona, self.elipsoide), h

    # --- Vectores (desplazamientos, fuerzas) -------------------------------

    def rotar_vector(self, vx: float, vy: float, vz: float, unidad_vector: float = 1.0) -> Vector3:
        """Lleva un vector de ejes del modelo a ejes ENU.

        Solo rota (y cambia de unidad): un desplazamiento no se traslada ni se
        escala con la geometría. ``unidad_vector`` convierte el vector a las
        unidades de salida (por ejemplo, 0.001 para pasar de mm a m).
        """
        dx, dy, dz = _a_z_arriba(vx * unidad_vector, vy * unidad_vector, vz * unidad_vector, self.eje_vertical)
        return (
            dx * self._sin - dy * self._cos,
            dx * self._cos + dy * self._sin,
            dz,
        )

    # --- Información de cuadrícula -----------------------------------------

    def datos_cuadricula(self, zona: int | None = None) -> dict:
        """Convergencia, factor de escala y factor combinado en el punto de amarre.

        El factor combinado = k (proyección) × factor de elevación, y convierte
        una distancia horizontal real a nivel de la obra en distancia de
        cuadrícula UTM. Es la cifra que hay que tener en cuenta al comparar el
        modelo con planos topográficos en coordenadas UTM.
        """
        utm = geodesicas_a_utm(self.lat0, self.lon0, zona, self.elipsoide)
        phi = math.radians(self.lat0)
        e2 = self.elipsoide.e2
        s2 = math.sin(phi) ** 2
        m = self.elipsoide.a * (1 - e2) / (1 - e2 * s2) ** 1.5
        n = self.elipsoide.a / math.sqrt(1 - e2 * s2)
        radio = math.sqrt(m * n)
        factor_elevacion = radio / (radio + self.h0)
        return {
            "zona": utm.zona,
            "hemisferio": utm.hemisferio,
            "este": utm.este,
            "norte": utm.norte,
            "convergencia_grados": utm.convergencia,
            "acimut_x_cuadricula": _normalizar_acimut(self.acimut_x - utm.convergencia),
            "factor_escala_k": utm.escala,
            "factor_elevacion": factor_elevacion,
            "factor_combinado": utm.escala * factor_elevacion,
        }

    def como_dict(self) -> dict:
        return {
            "latitud": self.lat0,
            "longitud": self.lon0,
            "altura_elipsoidal": self.h0,
            "acimut_eje_x": self.acimut_x,
            "punto_modelo": list(self.punto_modelo),
            "factor_unidad": self.unidad,
            "escala": self.escala,
            "eje_vertical": self.eje_vertical,
            "elipsoide": self.elipsoide.nombre,
        }


# --- Ajuste por puntos de control ---------------------------------------------


@dataclass(frozen=True)
class PuntoControl:
    """Punto con coordenadas conocidas en el modelo y en la Tierra.

    ``h`` es altura elipsoidal. Si solo se conoce la ortométrica (sobre el
    nivel del mar), súmele la ondulación geoidal N: h = H + N.
    """

    nombre: str
    modelo: Vector3
    lat: float
    lon: float
    h: float


@dataclass
class Residuo:
    nombre: str
    de: float
    dn: float
    du: float

    @property
    def horizontal(self) -> float:
        return math.hypot(self.de, self.dn)


@dataclass
class ResultadoAjuste:
    georreferencia: Georreferencia
    residuos: list[Residuo]
    rms_horizontal: float
    rms_vertical: float
    escala_estimada: float
    advertencias: list[str]

    def como_dict(self) -> dict:
        return {
            "rms_horizontal_m": self.rms_horizontal,
            "rms_vertical_m": self.rms_vertical,
            "escala_estimada": self.escala_estimada,
            "residuos": [
                {
                    "punto": r.nombre,
                    "de_m": r.de,
                    "dn_m": r.dn,
                    "du_m": r.du,
                    "horizontal_m": r.horizontal,
                }
                for r in self.residuos
            ],
            "advertencias": list(self.advertencias),
        }


def ajustar_puntos_control(
    puntos: Sequence[PuntoControl],
    unidad: float = 1.0,
    eje_vertical: str = "Z",
    permitir_escala: bool = False,
    elipsoide: Elipsoide = WGS84,
    tolerancia_horizontal: float = 0.05,
    tolerancia_vertical: float = 0.10,
    tolerancia_escala: float = 1e-3,
) -> ResultadoAjuste:
    """Calcula la georreferencia por mínimos cuadrados a partir de ≥ 2 puntos.

    Método (Procrustes / Helmert 2D en forma cerrada):

    1. Se toma un origen ENU provisional en el centroide de los puntos.
    2. Se centran las coordenadas de modelo p y de terreno q en planta.
    3. Sxx = Σ(p'x·q'x + p'y·q'y),  Sxy = Σ(p'x·q'y − p'y·q'x)
       θ = atan2(Sxy, Sxx)  (giro antihorario del eje X del modelo respecto al Este)
       s = √(Sxx² + Sxy²) / Σ|p'|²  (solo si se permite escala; si no, s = 1)
    4. Acimut del eje X = 90° − θ.
    5. En vertical solo se ajusta la traslación (el eje vertical del modelo es
       la vertical local).
    6. Se mueve el origen ENU al centroide ajustado y se repite (2 vueltas
       bastan) para que el marco ENU final sea exactamente el del amarre.
    """
    if len(puntos) < 2:
        raise ValueError("Se necesitan al menos 2 puntos de control.")
    nombres = [p.nombre for p in puntos]
    if len(set(nombres)) != len(nombres):
        raise ValueError("Los nombres de los puntos de control deben ser únicos.")

    modelo_m = [_a_z_arriba(*(c * unidad for c in p.modelo), eje_vertical) for p in puntos]
    k = len(puntos)
    pm = tuple(sum(c[i] for c in modelo_m) / k for i in range(3))
    centrado_p = [(c[0] - pm[0], c[1] - pm[1], c[2] - pm[2]) for c in modelo_m]
    suma_p2 = sum(c[0] ** 2 + c[1] ** 2 for c in centrado_p)
    if suma_p2 < 1e-6:
        raise ValueError("Los puntos de control coinciden en planta; no definen la orientación.")

    lat0 = sum(p.lat for p in puntos) / k
    lon0 = sum(p.lon for p in puntos) / k
    h0 = sum(p.h for p in puntos) / k
    alfa = 0.0
    s = 1.0
    s_estimada = 1.0
    for _ in range(3):
        marco = MarcoENU(lat0, lon0, h0, elipsoide)
        terreno = [marco.desde_geodesicas(p.lat, p.lon, p.h) for p in puntos]
        qm = tuple(sum(c[i] for c in terreno) / k for i in range(3))
        centrado_q = [(c[0] - qm[0], c[1] - qm[1]) for c in terreno]
        sxx = sum(a[0] * b[0] + a[1] * b[1] for a, b in zip(centrado_p, centrado_q))
        sxy = sum(a[0] * b[1] - a[1] * b[0] for a, b in zip(centrado_p, centrado_q))
        theta = math.atan2(sxy, sxx)
        s_estimada = math.hypot(sxx, sxy) / suma_p2
        s = s_estimada if permitir_escala else 1.0
        alfa = 90.0 - math.degrees(theta)
        lat0, lon0, h0 = marco.a_geodesicas(*qm)

    # El punto del modelo que corresponde al amarre es el centroide de los
    # puntos de control, expresado de vuelta en las unidades y ejes del modelo.
    pm_modelo = tuple(c / unidad for c in _desde_z_arriba(*pm, eje_vertical))
    georef = Georreferencia(
        lat0,
        lon0,
        h0,
        alfa,
        punto_modelo=pm_modelo,
        unidad=unidad,
        escala=s,
        eje_vertical=eje_vertical,
        elipsoide=elipsoide,
    )

    residuos = []
    for p in puntos:
        pred = georef.modelo_a_enu(*p.modelo)
        obs = georef._marco.desde_geodesicas(p.lat, p.lon, p.h)
        residuos.append(Residuo(p.nombre, obs[0] - pred[0], obs[1] - pred[1], obs[2] - pred[2]))
    rms_h = math.sqrt(sum(r.horizontal**2 for r in residuos) / k)
    rms_v = math.sqrt(sum(r.du**2 for r in residuos) / k)

    advertencias = []
    if k == 2:
        advertencias.append(
            "Solo hay 2 puntos de control: el ajuste no tiene redundancia y los "
            "residuos no permiten detectar errores. Se recomiendan 3 o más."
        )
    if rms_h > tolerancia_horizontal:
        advertencias.append(
            f"RMS horizontal {rms_h:.3f} m supera la tolerancia de {tolerancia_horizontal} m: "
            "revise la correspondencia de puntos, las unidades o el datum."
        )
    if rms_v > tolerancia_vertical:
        advertencias.append(
            f"RMS vertical {rms_v:.3f} m supera la tolerancia de {tolerancia_vertical} m: "
            "revise si mezcló alturas ortométricas y elipsoidales."
        )
    if not permitir_escala and abs(s_estimada - 1.0) > tolerancia_escala:
        advertencias.append(
            f"La escala estimada es {s_estimada:.6f} (se esperaba 1): posible error de "
            "unidades del modelo o coordenadas de control en un sistema distinto."
        )
    return ResultadoAjuste(georef, residuos, rms_h, rms_v, s_estimada, advertencias)
