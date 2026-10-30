"""Genera los datos de ejemplo de un edificio aporticado de 3 pisos.

    python ejemplos/generar_ejemplos.py

Crea el modelo en formato neutro JSON, las mismas tablas en CSV y los puntos
de control del proyecto por ajuste. Los resultados son sintéticos (no salen
de un análisis real) y solo sirven para probar el módulo.
"""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(DIR.parent))

from tav0t.georef import Georreferencia, geodesicas_a_utm  # noqa: E402

VANOS_X = [0.0, 6.0, 12.0]
VANOS_Y = [0.0, 5.0, 10.0]
COTAS = [0.0, 3.5, 6.5, 9.5]
DESPL_X_MM = [0.0, 12.0, 26.0, 38.0]  # desplazamiento de piso, caso SISMO_X


def id_nodo(nivel: int, ix: int, iy: int) -> str:
    return f"{nivel}{iy}{ix + 1}"


def construir_modelo() -> dict:
    nodos, elementos, despl, dc = [], [], {}, {}
    for k, z in enumerate(COTAS):
        for iy, y in enumerate(VANOS_Y):
            for ix, x in enumerate(VANOS_X):
                nid = id_nodo(k, ix, iy)
                nodos.append({"id": nid, "x": x, "y": y, "z": z})
                # Traslación en X con una ligera torsión en planta.
                torsion = 0.04 * DESPL_X_MM[k] * (iy - 1)
                despl[nid] = [round(DESPL_X_MM[k] + torsion, 3), round(0.03 * DESPL_X_MM[k] * (ix - 1), 3), 0.0]

    for k in range(1, len(COTAS)):
        for iy in range(len(VANOS_Y)):
            for ix in range(len(VANOS_X)):
                eid = f"C{k}-{iy}{ix}"
                elementos.append({"id": eid, "tipo": "barra", "nodos": [id_nodo(k - 1, ix, iy), id_nodo(k, ix, iy)],
                                  "seccion": "C50x50" if k == 1 else "C40x40"})
                borde = ix in (0, 2) or iy in (0, 2)
                dc[eid] = round({1: 0.92, 2: 0.74, 3: 0.52}[k] + (0.11 if not borde else 0.0) - 0.03 * ix, 3)
        for iy in range(len(VANOS_Y)):
            for ix in range(len(VANOS_X) - 1):
                eid = f"VX{k}-{iy}{ix}"
                elementos.append({"id": eid, "tipo": "barra", "nodos": [id_nodo(k, ix, iy), id_nodo(k, ix + 1, iy)],
                                  "seccion": "V30x50"})
                dc[eid] = round(0.95 - 0.12 * (k - 1) - 0.05 * abs(iy - 1), 3)
        for ix in range(len(VANOS_X)):
            for iy in range(len(VANOS_Y) - 1):
                eid = f"VY{k}-{iy}{ix}"
                elementos.append({"id": eid, "tipo": "barra", "nodos": [id_nodo(k, ix, iy), id_nodo(k, ix, iy + 1)],
                                  "seccion": "V30x45"})
                dc[eid] = round(0.48 - 0.05 * (k - 1), 3)
        for iy in range(len(VANOS_Y) - 1):
            for ix in range(len(VANOS_X) - 1):
                elementos.append({
                    "id": f"L{k}-{iy}{ix}",
                    "tipo": "area",
                    "nodos": [id_nodo(k, ix, iy), id_nodo(k, ix + 1, iy), id_nodo(k, ix + 1, iy + 1), id_nodo(k, ix, iy + 1)],
                    "espesor_m": 0.12,
                })

    return {
        "unidades": "m",
        "eje_vertical": "Z",
        "nodos": nodos,
        "elementos": elementos,
        "resultados": {
            "SISMO_X": {
                "_comentario": "Resultados sintéticos de ejemplo, no provienen de un análisis real.",
                "unidades": "mm",
                "desplazamientos": despl,
                "elementos": {eid: {"relacion_dc": v} for eid, v in dc.items()},
            }
        },
    }


def escribir_csv(modelo: dict, carpeta: Path) -> None:
    """Tablas con ';' y coma decimal, como las exporta una hoja de cálculo en español."""
    carpeta.mkdir(exist_ok=True)

    def num(v: float) -> str:
        return f"{v:g}".replace(".", ",")

    lineas = ["id;x;y;z"] + [f"{n['id']};{num(n['x'])};{num(n['y'])};{num(n['z'])}" for n in modelo["nodos"]]
    (carpeta / "nodos.csv").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    lineas = ["id;tipo;n1;n2;n3;n4"]
    for e in modelo["elementos"]:
        ns = e["nodos"] + [""] * (4 - len(e["nodos"]))
        lineas.append(";".join([e["id"], e["tipo"], *ns]))
    (carpeta / "elementos.csv").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    despl = modelo["resultados"]["SISMO_X"]["desplazamientos"]
    lineas = ["nodo;ux;uy;uz"] + [f"{k};{num(v[0])};{num(v[1])};{num(v[2])}" for k, v in despl.items()]
    (carpeta / "desplazamientos.csv").write_text("\n".join(lineas) + "\n", encoding="utf-8")


def puntos_control_simulados(proyecto_parametrico: dict) -> list[dict]:
    """Simula un levantamiento topográfico de tres esquinas del edificio
    (coordenadas UTM con ruido de pocos milímetros)."""
    g = proyecto_parametrico["georreferencia"]
    n_geoide = proyecto_parametrico["ondulacion_geoidal"]
    georef = Georreferencia(
        g["origen"]["latitud"], g["origen"]["longitud"], g["origen"]["altura"] + n_geoide, g["acimut_eje_x"]
    )
    rnd = random.Random(7)
    puntos = []
    for nombre, (x, y) in {"A1": (0.0, 0.0), "C1": (12.0, 0.0), "C3": (12.0, 10.0), "A3": (0.0, 10.0)}.items():
        lat, lon, h = georef.modelo_a_geodesicas(x, y, 0.0)
        utm = geodesicas_a_utm(lat, lon)
        puntos.append({
            "nombre": nombre,
            "modelo": [x, y, 0.0],
            "utm": {
                "este": round(utm.este + rnd.uniform(-0.004, 0.004), 3),
                "norte": round(utm.norte + rnd.uniform(-0.004, 0.004), 3),
                "zona": utm.zona,
                "hemisferio": utm.hemisferio,
            },
            "altura": round(h - n_geoide + rnd.uniform(-0.006, 0.006), 3),
        })
    return puntos


# Hallazgos de la inspección con dron del laboratorio del curso (módulo 9):
# posición real sobre la cara del elemento, en coordenadas del modelo.
HALLAZGOS = [
    ("H01", "Fisura diagonal", "Cara exterior de la columna de esquina, tercio inferior.", "ancho ≈ 1.5 mm, largo 0.9 m",
     "Z_0143.JPG", (12.0, -0.25, 1.8)),
    ("H02", "Fisura vertical", "Cara exterior de la viga de fachada, centro de la luz, zona inferior.",
     "ancho < 0.5 mm (se ve, no se mide), largo 0.35 m", "Z_0217.JPG", (3.0, -0.15, 6.1)),
    ("H03", "Desprendimiento con acero expuesto", "Fondo de la viga de borde de cubierta, cerca del apoyo.",
     "0.25 × 0.15 m, barra corroída visible", "Z_0388.JPG", (12.15, 1.2, 9.15)),
    ("H04", "Mapa de fisuras", "Cara superior de la losa de cubierta, sin impermeabilización.",
     "fisuras finas en malla, < 0.5 mm, unos 2 m²", "Z_0402.JPG", (9.2, 2.6, 9.56)),
    ("H05", "Anomalía térmica", "Muro de fachada del piso 2: zona fría con forma de mancha de humedad.",
     "ΔT = 2.8 °C, 1.1 m²", "T_0091.JPG", (3.0, 10.12, 5.2)),
    ("H06", "Fisura horizontal", "Arranque de la columna de esquina, cara exterior, con eflorescencias.",
     "ancho ≈ 2 mm, en parte del perímetro", "Z_0012.JPG", (-0.25, 10.0, 0.3)),
]  # fmt: skip


def hallazgos_simulados(proyecto_parametrico: dict) -> dict:
    """Simula lo que entrega el modelo fotogramétrico: coordenadas UTM y altura
    ortométrica de cada hallazgo, con un error de un par de centímetros."""
    g = proyecto_parametrico["georreferencia"]
    n_geoide = proyecto_parametrico["ondulacion_geoidal"]
    georef = Georreferencia(
        g["origen"]["latitud"], g["origen"]["longitud"], g["origen"]["altura"] + n_geoide, g["acimut_eje_x"]
    )
    rnd = random.Random(11)
    hallazgos = []
    for id_, tipo, descripcion, medida, foto, (x, y, z) in HALLAZGOS:
        lat, lon, h = georef.modelo_a_geodesicas(x, y, z)
        utm = geodesicas_a_utm(lat, lon)
        hallazgos.append({
            "id": id_,
            "tipo": tipo,
            "descripcion": descripcion,
            "medida": medida,
            "foto": foto,
            "utm": {
                "este": round(utm.este + rnd.uniform(-0.02, 0.02), 3),
                "norte": round(utm.norte + rnd.uniform(-0.02, 0.02), 3),
                "zona": utm.zona,
                "hemisferio": utm.hemisferio,
            },
            "altura": round(h - n_geoide + rnd.uniform(-0.03, 0.03), 3),
        })  # fmt: skip
    return {
        "_comentario": "Hallazgos simulados para el laboratorio del curso. Altura ortométrica; datum WGS84.",
        "hallazgos": hallazgos,
    }


def main() -> None:
    modelo = construir_modelo()
    (DIR / "edificio_3p.json").write_text(json.dumps(modelo, ensure_ascii=False, indent=1), encoding="utf-8")
    escribir_csv(modelo, DIR / "csv")

    proyecto = json.loads((DIR / "proyecto_parametrico.json").read_text(encoding="utf-8"))
    ruta_control = DIR / "proyecto_puntos_control.json"
    control = json.loads(ruta_control.read_text(encoding="utf-8"))
    control["georreferencia"]["puntos"] = puntos_control_simulados(proyecto)
    ruta_control.write_text(json.dumps(control, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    hallazgos = hallazgos_simulados(proyecto)
    (DIR / "curso_drones" / "hallazgos.json").write_text(
        json.dumps(hallazgos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("Ejemplos generados en", DIR)


if __name__ == "__main__":
    main()
