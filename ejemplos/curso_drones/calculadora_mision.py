"""Calculadora de misión del curso de inspección con drones.

    python ejemplos/curso_drones/calculadora_mision.py gsd --camara gran_angular --distancia 6
    python ejemplos/curso_drones/calculadora_mision.py distancia --camara zoom --gsd 0.5
    python ejemplos/curso_drones/calculadora_mision.py fachada --camara gran_angular --ancho 30 --alto 24 --distancia 6
    python ejemplos/curso_drones/calculadora_mision.py densidad --altitud 3000

Resuelve los cálculos del módulo 4 del curso (docs/curso_inspeccion_drones/):
resolución en el objeto (GSD), distancia de vuelo, huella de la foto, malla de
fotos de una fachada y densidad del aire en altura. Las cámaras son genéricas;
para un equipo real use los datos de su ficha técnica.
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass, replace

PX_MEDICION = 3  # píxeles a lo ancho de un detalle (fisura, mancha térmica) para medirlo; criterio del curso


@dataclass(frozen=True)
class Camara:
    nombre: str
    sensor_ancho_mm: float
    sensor_alto_mm: float
    focal_mm: float
    px_ancho: int
    px_alto: int


CAMARAS = {
    "gran_angular": Camara('Gran angular, sensor 1"', 13.2, 8.8, 8.8, 5472, 3648),
    "zoom": Camara('Zoom, sensor 1/2"', 6.4, 4.8, 40.0, 4000, 3000),
    "termica": Camara("Térmica radiométrica 640×512, píxel 12 µm", 7.68, 6.144, 13.0, 640, 512),
}


def gsd_mm(camara: Camara, distancia_m: float) -> float:
    """Tamaño en el objeto de un píxel (mm/px), con la cámara perpendicular a la superficie."""
    return camara.sensor_ancho_mm * distancia_m * 1000.0 / (camara.focal_mm * camara.px_ancho)


def distancia_para_gsd(camara: Camara, gsd_objetivo_mm: float) -> float:
    """Distancia (m) a la que la cámara logra el GSD pedido."""
    return gsd_objetivo_mm * camara.focal_mm * camara.px_ancho / (camara.sensor_ancho_mm * 1000.0)


def huella_m(camara: Camara, distancia_m: float) -> tuple[float, float]:
    """Ancho y alto (m) del área que cubre una foto."""
    return (
        camara.sensor_ancho_mm * distancia_m / camara.focal_mm,
        camara.sensor_alto_mm * distancia_m / camara.focal_mm,
    )


def plan_fachada(
    camara: Camara,
    ancho_m: float,
    alto_m: float,
    distancia_m: float,
    solape_frontal: float = 0.8,
    solape_lateral: float = 0.7,
) -> dict:
    """Malla de fotos para una fachada plana con pasadas horizontales.

    La foto va en horizontal (lado largo a lo ancho de la fachada). Los centros
    de las fotos van de borde a borde de la fachada para que los bordes reciban
    el mismo solape que el centro.
    """
    if not (0 <= solape_frontal < 1 and 0 <= solape_lateral < 1):
        raise ValueError("Los solapes van de 0 a menos de 1 (p. ej. 0.8 = 80 %).")
    huella_ancho, huella_alto = huella_m(camara, distancia_m)
    paso_fotos = huella_ancho * (1 - solape_frontal)
    paso_pasadas = huella_alto * (1 - solape_lateral)
    fotos_por_pasada = math.ceil(ancho_m / paso_fotos) + 1
    pasadas = math.ceil(alto_m / paso_pasadas) + 1
    return {
        "gsd_mm": gsd_mm(camara, distancia_m),
        "huella_ancho_m": huella_ancho,
        "huella_alto_m": huella_alto,
        "paso_fotos_m": paso_fotos,
        "paso_pasadas_m": paso_pasadas,
        "fotos_por_pasada": fotos_por_pasada,
        "pasadas": pasadas,
        "fotos": fotos_por_pasada * pasadas,
    }


def densidad_aire(altitud_m: float) -> float:
    """Densidad del aire (kg/m³) en la atmósfera estándar ISA, hasta 11 km."""
    return 1.225 * (1 - 2.25577e-5 * altitud_m) ** 4.2559


def _camara(args) -> Camara:
    base = CAMARAS[args.camara]
    return replace(base, focal_mm=args.focal) if args.focal else base


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Calculadora de misión de inspección con drones.")
    sub = parser.add_subparsers(dest="comando", required=True)
    for nombre in ("gsd", "distancia", "fachada"):
        p = sub.add_parser(nombre)
        p.add_argument("--camara", choices=sorted(CAMARAS), default="gran_angular")
        p.add_argument("--focal", type=float, help="focal real en mm (para cambiar el zoom)")
    sub.choices["gsd"].add_argument("--distancia", type=float, required=True, help="m a la superficie")
    sub.choices["distancia"].add_argument("--gsd", type=float, required=True, help="GSD buscado en mm/px")
    fachada = sub.choices["fachada"]
    fachada.add_argument("--ancho", type=float, required=True, help="m")
    fachada.add_argument("--alto", type=float, required=True, help="m")
    fachada.add_argument("--distancia", type=float, required=True, help="m a la fachada")
    fachada.add_argument("--solape-frontal", type=float, default=0.8)
    fachada.add_argument("--solape-lateral", type=float, default=0.7)
    sub.add_parser("densidad").add_argument("--altitud", type=float, required=True, help="m s. n. m.")
    args = parser.parse_args(argv)

    try:
        if args.comando == "densidad":
            rho = densidad_aire(args.altitud)
            print(f"Densidad del aire a {args.altitud:g} m: {rho:.3f} kg/m³ "
                  f"({100 * (1 - rho / 1.225):.0f} % menos que a nivel del mar)")  # fmt: skip
            return 0
        camara = _camara(args)
        print(f"{camara.nombre}, focal {camara.focal_mm:g} mm")
        if args.comando == "gsd":
            g = gsd_mm(camara, args.distancia)
            ancho, alto = huella_m(camara, args.distancia)
            print(f"A {args.distancia:g} m: GSD {g:.2f} mm/px, huella {ancho:.2f} × {alto:.2f} m")
            print(f"Ancho mínimo medible (≥ {PX_MEDICION} px): {PX_MEDICION * g:.1f} mm")
        elif args.comando == "distancia":
            d = distancia_para_gsd(camara, args.gsd)
            print(f"GSD {args.gsd:g} mm/px a {d:.1f} m de la superficie")
        else:
            plan = plan_fachada(camara, args.ancho, args.alto, args.distancia,
                                args.solape_frontal, args.solape_lateral)  # fmt: skip
            print(f"Fachada {args.ancho:g} × {args.alto:g} m a {args.distancia:g} m: GSD {plan['gsd_mm']:.2f} mm/px")
            print(f"Huella {plan['huella_ancho_m']:.2f} × {plan['huella_alto_m']:.2f} m; "
                  f"foto cada {plan['paso_fotos_m']:.2f} m, pasada cada {plan['paso_pasadas_m']:.2f} m")  # fmt: skip
            print(f"{plan['pasadas']} pasadas × {plan['fotos_por_pasada']} fotos = {plan['fotos']} fotos")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
