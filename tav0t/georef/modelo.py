"""Modelo estructural en formato neutro.

El motor no depende de ningún programa comercial. Cualquier fuente (SAP2000,
ETABS, OpenSees, la propia plataforma) se convierte primero a este formato,
y desde ahí todo el proceso es idéntico.

Formato JSON neutro::

    {
      "unidades": "m",                  # longitud de las coordenadas
      "eje_vertical": "Z",              # "Z" o "Y"
      "nodos": [{"id": "1", "x": 0, "y": 0, "z": 0}, ...],
      "elementos": [
        {"id": "C1", "tipo": "barra", "nodos": ["1", "5"]},
        {"id": "L1", "tipo": "area",  "nodos": ["5", "6", "8", "7"]}
      ],
      "resultados": {
        "SISMO_X": {
          "unidades": "m",              # longitud de los desplazamientos
          "desplazamientos": {"5": [0.012, 0.001, 0.0], ...},
          "elementos": {"C1": {"relacion_dc": 0.82}, ...}
        }
      }
    }
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from pathlib import Path

from .transformacion import factor_unidad

TIPOS_ELEMENTO = ("barra", "area")


@dataclass
class Nodo:
    id: str
    x: float
    y: float
    z: float


@dataclass
class Elemento:
    id: str
    tipo: str
    nodos: list[str]
    propiedades: dict = field(default_factory=dict)


@dataclass
class CasoResultados:
    nombre: str
    unidades: str = "m"
    desplazamientos: dict[str, tuple[float, float, float]] = field(default_factory=dict)
    elementos: dict[str, dict[str, float]] = field(default_factory=dict)


@dataclass
class ModeloEstructural:
    nodos: dict[str, Nodo]
    elementos: dict[str, Elemento] = field(default_factory=dict)
    resultados: dict[str, CasoResultados] = field(default_factory=dict)
    unidades: str = "m"
    eje_vertical: str = "Z"

    def validar(self) -> list[str]:
        """Comprueba la coherencia interna. Lanza ValueError si hay errores graves
        y devuelve una lista de advertencias para los problemas menores."""
        errores = []
        advertencias = []
        factor_unidad(self.unidades)
        if self.eje_vertical not in ("Z", "Y"):
            errores.append(f"eje_vertical inválido: {self.eje_vertical}")
        if not self.nodos:
            errores.append("El modelo no tiene nodos.")
        for el in self.elementos.values():
            if el.tipo not in TIPOS_ELEMENTO:
                errores.append(f"Elemento {el.id}: tipo '{el.tipo}' no soportado {TIPOS_ELEMENTO}.")
            minimo = 2 if el.tipo == "barra" else 3
            if len(el.nodos) < minimo:
                errores.append(f"Elemento {el.id}: necesita al menos {minimo} nodos.")
            faltan = [n for n in el.nodos if n not in self.nodos]
            if faltan:
                errores.append(f"Elemento {el.id}: nodos inexistentes {faltan}.")
        for caso in self.resultados.values():
            factor_unidad(caso.unidades)
            sobrantes = [n for n in caso.desplazamientos if n not in self.nodos]
            if sobrantes:
                advertencias.append(
                    f"Caso {caso.nombre}: {len(sobrantes)} desplazamientos de nodos inexistentes se ignoran."
                )
            sobrantes_el = [e for e in caso.elementos if e not in self.elementos]
            if sobrantes_el:
                advertencias.append(
                    f"Caso {caso.nombre}: {len(sobrantes_el)} resultados de elementos inexistentes se ignoran."
                )
        if errores:
            raise ValueError("Modelo inválido:\n  - " + "\n  - ".join(errores))
        return advertencias


def _vector3(valor, contexto: str) -> tuple[float, float, float]:
    if isinstance(valor, dict):
        valor = [valor.get("ux", 0.0), valor.get("uy", 0.0), valor.get("uz", 0.0)]
    if len(valor) == 2:
        valor = [valor[0], valor[1], 0.0]
    if len(valor) != 3:
        raise ValueError(f"{contexto}: se esperaban 2 o 3 componentes, hay {len(valor)}.")
    return float(valor[0]), float(valor[1]), float(valor[2])


def modelo_desde_dict(datos: dict) -> ModeloEstructural:
    nodos = {}
    for n in datos.get("nodos", []):
        nid = str(n["id"])
        if nid in nodos:
            raise ValueError(f"Nodo duplicado: {nid}")
        nodos[nid] = Nodo(nid, float(n["x"]), float(n["y"]), float(n.get("z", 0.0)))

    elementos = {}
    for e in datos.get("elementos", []):
        eid = str(e["id"])
        if eid in elementos:
            raise ValueError(f"Elemento duplicado: {eid}")
        extra = {k: v for k, v in e.items() if k not in ("id", "tipo", "nodos")}
        elementos[eid] = Elemento(eid, e.get("tipo", "barra"), [str(n) for n in e["nodos"]], extra)

    resultados = {}
    for nombre, caso in datos.get("resultados", {}).items():
        resultados[nombre] = CasoResultados(
            nombre,
            caso.get("unidades", datos.get("unidades", "m")),
            {str(k): _vector3(v, f"Desplazamiento del nodo {k}") for k, v in caso.get("desplazamientos", {}).items()},
            {str(k): {kk: float(vv) for kk, vv in v.items()} for k, v in caso.get("elementos", {}).items()},
        )

    return ModeloEstructural(
        nodos,
        elementos,
        resultados,
        datos.get("unidades", "m"),
        datos.get("eje_vertical", "Z").upper(),
    )


def cargar_json(ruta: str | Path) -> ModeloEstructural:
    with open(ruta, encoding="utf-8") as f:
        return modelo_desde_dict(json.load(f))


def _leer_csv(ruta: str | Path) -> list[dict[str, str]]:
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        muestra = f.read(4096)
        f.seek(0)
        try:
            dialecto = csv.Sniffer().sniff(muestra, delimiters=",;\t")
        except csv.Error:
            dialecto = csv.excel
        lector = csv.DictReader(f, dialect=dialecto)
        return [{k.strip().lower(): (v or "").strip() for k, v in fila.items() if k} for fila in lector]


def _numero(texto: str) -> float:
    # Acepta coma decimal (habitual en hojas de cálculo en español).
    return float(texto.replace(",", ".")) if texto else 0.0


def cargar_csv(
    nodos: str | Path,
    elementos: str | Path | None = None,
    desplazamientos: str | Path | None = None,
    caso: str = "CASO_1",
    unidades: str = "m",
    unidades_resultados: str | None = None,
    eje_vertical: str = "Z",
) -> ModeloEstructural:
    """Carga un modelo desde tablas CSV exportadas por cualquier programa.

    * nodos: columnas ``id, x, y, z``
    * elementos: columnas ``id, tipo, n1, n2[, n3, n4, ...]``
    * desplazamientos: columnas ``nodo, ux, uy, uz``

    Detecta el separador (``,`` ``;`` o tabulador) y acepta coma decimal
    cuando el separador no es la coma.
    """
    datos: dict = {"unidades": unidades, "eje_vertical": eje_vertical, "nodos": [], "elementos": []}
    for fila in _leer_csv(nodos):
        datos["nodos"].append(
            {"id": fila["id"], "x": _numero(fila["x"]), "y": _numero(fila["y"]), "z": _numero(fila.get("z", ""))}
        )
    if elementos:
        for fila in _leer_csv(elementos):
            claves = sorted((k for k in fila if k.startswith("n") and k[1:].isdigit()), key=lambda k: int(k[1:]))
            datos["elementos"].append(
                {"id": fila["id"], "tipo": fila.get("tipo") or "barra", "nodos": [fila[k] for k in claves if fila[k]]}
            )
    if desplazamientos:
        despl = {}
        for fila in _leer_csv(desplazamientos):
            despl[fila["nodo"]] = [_numero(fila.get("ux", "")), _numero(fila.get("uy", "")), _numero(fila.get("uz", ""))]
        datos["resultados"] = {caso: {"unidades": unidades_resultados or unidades, "desplazamientos": despl}}
    return modelo_desde_dict(datos)
