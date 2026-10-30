"""Consulta de zonificación por ubicación (sísmica, de suelos, de amenaza…).

La zonificación se carga desde un GeoJSON de polígonos cuyas propiedades
contienen los parámetros de la norma (por ejemplo ``{"zona": "Alta",
"Aa": 0.25, "Av": 0.25}``). El motor no trae valores de ninguna norma: los
datos oficiales los aporta cada proyecto o la plataforma, así se pueden
actualizar sin tocar el código.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


def _punto_en_anillo(lon: float, lat: float, anillo: list[list[float]]) -> bool:
    """Algoritmo de cruce de rayos (par-impar)."""
    dentro = False
    j = len(anillo) - 1
    for i in range(len(anillo)):
        xi, yi = anillo[i][0], anillo[i][1]
        xj, yj = anillo[j][0], anillo[j][1]
        if (yi > lat) != (yj > lat):
            x_cruce = (xj - xi) * (lat - yi) / (yj - yi) + xi
            if lon < x_cruce:
                dentro = not dentro
        j = i
    return dentro


def _punto_en_poligono(lon: float, lat: float, poligono: list[list[list[float]]]) -> bool:
    """El primer anillo es el exterior; los siguientes son huecos."""
    if not _punto_en_anillo(lon, lat, poligono[0]):
        return False
    return not any(_punto_en_anillo(lon, lat, hueco) for hueco in poligono[1:])


@dataclass
class _Zona:
    propiedades: dict
    poligonos: list[list[list[list[float]]]]
    caja: tuple[float, float, float, float]  # lon_min, lat_min, lon_max, lat_max


class Zonificacion:
    def __init__(self, geojson: dict, nombre: str = "zonificacion"):
        self.nombre = nombre
        self._zonas: list[_Zona] = []
        for f in geojson.get("features", []):
            geom = f.get("geometry") or {}
            if geom.get("type") == "Polygon":
                poligonos = [geom["coordinates"]]
            elif geom.get("type") == "MultiPolygon":
                poligonos = geom["coordinates"]
            else:
                continue
            xs = [c[0] for p in poligonos for c in p[0]]
            ys = [c[1] for p in poligonos for c in p[0]]
            self._zonas.append(_Zona(f.get("properties") or {}, poligonos, (min(xs), min(ys), max(xs), max(ys))))
        if not self._zonas:
            raise ValueError("La zonificación no contiene polígonos.")

    @classmethod
    def desde_archivo(cls, ruta: str | Path) -> "Zonificacion":
        ruta = Path(ruta)
        with open(ruta, encoding="utf-8") as f:
            return cls(json.load(f), ruta.stem)

    def consultar(self, lat: float, lon: float) -> dict | None:
        """Propiedades de la zona que contiene el punto, o None si cae fuera."""
        for z in self._zonas:
            x0, y0, x1, y1 = z.caja
            if not (x0 <= lon <= x1 and y0 <= lat <= y1):
                continue
            if any(_punto_en_poligono(lon, lat, p) for p in z.poligonos):
                return dict(z.propiedades)
        return None
