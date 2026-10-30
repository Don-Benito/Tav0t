"""Laboratorio del curso de inspección con drones: ubica los hallazgos en el modelo.

    python ejemplos/curso_drones/ubicar_hallazgos.py
    python ejemplos/curso_drones/ubicar_hallazgos.py --ondulacion 0     # ejercicio: error de alturas

Lee los hallazgos de la inspección (coordenadas UTM y altura ortométrica, como
las entrega el software de fotogrametría en el mismo datum del proyecto), los
lleva al sistema del modelo estructural con la georreferencia del proyecto y
busca el elemento más cercano a cada uno. Un hallazgo lejos de todo elemento
suele estar en algo que no se modeló (mampostería, enchape, cubierta liviana).

El laboratorio está explicado en docs/curso_inspeccion_drones/09_georreferenciacion_e_integracion.md.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(DIR.parent.parent))

from tav0t.georef import (  # noqa: E402
    Georreferencia,
    ModeloEstructural,
    cargar_json,
    ejecutar,
    obtener_elipsoide,
    utm_a_geodesicas,
)

TOLERANCIA_M = 0.6  # medio lado de la sección más grande + error del modelo fotogramétrico


def _resta(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _cruz(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def distancia_segmento(p, a, b) -> float:
    ab, ap = _resta(b, a), _resta(p, a)
    t = max(0.0, min(1.0, _dot(ap, ab) / _dot(ab, ab)))
    return math.dist(p, (a[0] + t * ab[0], a[1] + t * ab[1], a[2] + t * ab[2]))


def distancia_poligono(p, vertices) -> float:
    """Distancia de un punto a un polígono plano y convexo (losa, muro)."""
    # Normal de Newell: robusta aunque los vértices no estén perfectamente en un plano.
    n = [0.0, 0.0, 0.0]
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        n[0] += (a[1] - b[1]) * (a[2] + b[2])
        n[1] += (a[2] - b[2]) * (a[0] + b[0])
        n[2] += (a[0] - b[0]) * (a[1] + b[1])
    largo = math.sqrt(_dot(n, n))
    n = (n[0] / largo, n[1] / largo, n[2] / largo)
    altura = _dot(_resta(p, vertices[0]), n)
    proyeccion = (p[0] - altura * n[0], p[1] - altura * n[1], p[2] - altura * n[2])
    dentro = all(
        _dot(_cruz(_resta(b, a), _resta(proyeccion, a)), n) >= 0 for a, b in zip(vertices, vertices[1:] + vertices[:1])
    )
    if dentro:
        return abs(altura)
    return min(distancia_segmento(p, a, b) for a, b in zip(vertices, vertices[1:] + vertices[:1]))


def elemento_mas_cercano(modelo: ModeloEstructural, punto) -> tuple[str, float]:
    """Id del elemento más cercano y su distancia, en unidades del modelo.

    Las barras se revisan primero: en un empate (el borde de una losa coincide
    con el eje de su viga) gana la barra.
    """
    mejor, distancia = None, math.inf
    for el in sorted(modelo.elementos.values(), key=lambda e: e.tipo != "barra"):
        xyz = [(modelo.nodos[n].x, modelo.nodos[n].y, modelo.nodos[n].z) for n in el.nodos]
        d = distancia_segmento(punto, *xyz[:2]) if el.tipo == "barra" else distancia_poligono(punto, xyz)
        if d < distancia:
            mejor, distancia = el.id, d
    return mejor, distancia


def ubicar(
    ruta_proyecto: str | Path,
    ruta_hallazgos: str | Path,
    ondulacion: float | None = None,
    tolerancia: float = TOLERANCIA_M,
) -> list[dict]:
    """Devuelve cada hallazgo con sus coordenadas de modelo y el elemento más cercano."""
    ruta_proyecto = Path(ruta_proyecto)
    config = json.loads(ruta_proyecto.read_text(encoding="utf-8"))
    if config.get("modelo", {}).get("formato", "json") != "json":
        raise ValueError("El laboratorio solo lee modelos en JSON neutro.")
    config["salidas"] = {**config.get("salidas", {}), "formatos": []}  # solo hace falta la georreferencia
    g = ejecutar(config, ruta_proyecto.parent)["georreferencia"]
    elipsoide = obtener_elipsoide(g["elipsoide"])
    georef = Georreferencia(
        g["latitud"], g["longitud"], g["altura_elipsoidal"], g["acimut_eje_x"], tuple(g["punto_modelo"]),
        g["factor_unidad"], g["escala"], g["eje_vertical"], elipsoide,
    )  # fmt: skip
    modelo = cargar_json(ruta_proyecto.parent / config["modelo"]["archivo"])
    n_geoide = float(config.get("ondulacion_geoidal", 0.0)) if ondulacion is None else ondulacion

    datos = json.loads(Path(ruta_hallazgos).read_text(encoding="utf-8"))
    ubicados = []
    for h in datos["hallazgos"]:
        u = h["utm"]
        lat, lon, _, _ = utm_a_geodesicas(u["este"], u["norte"], u["zona"], u.get("hemisferio", "N"), elipsoide)
        x, y, z = georef.geodesicas_a_modelo(lat, lon, h["altura"] + n_geoide)
        elemento, distancia = elemento_mas_cercano(modelo, (x, y, z))
        distancia *= g["factor_unidad"] * g["escala"]
        ubicados.append({
            "id": h["id"],
            "tipo": h["tipo"],
            "modelo": (x, y, z),
            "elemento": elemento if distancia <= tolerancia else None,
            "mas_cercano": elemento,
            "distancia_m": distancia,
        })  # fmt: skip
    return ubicados


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ubica los hallazgos de una inspección con dron en el modelo.")
    parser.add_argument("--proyecto", default=str(DIR.parent / "proyecto_puntos_control.json"))
    parser.add_argument("--hallazgos", default=str(DIR / "hallazgos.json"))
    parser.add_argument(
        "--ondulacion", type=float, help="N (m) para convertir los hallazgos; por defecto, la del proyecto"
    )
    parser.add_argument("--tolerancia", type=float, default=TOLERANCIA_M, help="m")
    args = parser.parse_args(argv)
    try:
        ubicados = ubicar(args.proyecto, args.hallazgos, args.ondulacion, args.tolerancia)
    except (OSError, KeyError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    print(f"{'Hallazgo':<9}{'x':>8}{'y':>8}{'z':>8}  {'Elemento':<10}{'d (m)':>7}  Tipo")
    for u in ubicados:
        x, y, z = u["modelo"]
        elemento = u["elemento"] or f"¿{u['mas_cercano']}?"
        print(f"{u['id']:<9}{x:8.2f}{y:8.2f}{z:8.2f}  {elemento:<10}{u['distancia_m']:7.2f}  {u['tipo']}")
    sin_elemento = [u["id"] for u in ubicados if u["elemento"] is None]
    if sin_elemento:
        print(f"\nA más de {args.tolerancia:g} m de todo elemento del modelo: {', '.join(sin_elemento)}. "
              "Revise si están en un elemento no modelado o si hay un error de coordenadas o de alturas.")  # fmt: skip
    return 0


if __name__ == "__main__":
    sys.exit(main())
