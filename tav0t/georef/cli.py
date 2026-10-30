"""Línea de comandos.

    python -m tav0t.georef ejecutar proyecto.json [--json]
    python -m tav0t.georef utm <latitud> <longitud> [--zona Z]
    python -m tav0t.georef geo <este> <norte> <zona> <N|S>

Con ``--json`` la salida es el informe completo en JSON por la salida
estándar, para que la plataforma pueda invocar el motor como proceso externo
desde cualquier lenguaje. Código de salida 0 = correcto, 2 = error de datos.
"""

from __future__ import annotations

import argparse
import json
import sys

from .motor import ejecutar_proyecto
from .utm import geodesicas_a_utm, utm_a_geodesicas


def _resumen(informe: dict) -> str:
    g = informe["georreferencia"]
    c = informe["cuadricula_utm"]
    lineas = [
        f"Proyecto: {informe['proyecto']}",
        f"Amarre: lat {g['latitud']:.8f}  lon {g['longitud']:.8f}  h {g['altura_elipsoidal']:.3f} m",
        f"UTM {c['zona']}{c['hemisferio']}: E {c['este']:.3f}  N {c['norte']:.3f}",
        f"Acimut eje X: {g['acimut_eje_x']:.4f}° verdadero / {c['acimut_x_cuadricula']:.4f}° cuadrícula",
        f"Convergencia: {c['convergencia_grados']:.5f}°   factor combinado: {c['factor_combinado']:.8f}",
        f"Nodos: {informe['modelo']['nodos']}   elementos: {informe['modelo']['elementos']}",
    ]
    ajuste = informe.get("ajuste_puntos_control")
    if ajuste:
        lineas.append(
            f"Ajuste por puntos de control: RMS H {ajuste['rms_horizontal_m'] * 1000:.1f} mm, "
            f"RMS V {ajuste['rms_vertical_m'] * 1000:.1f} mm, escala {ajuste['escala_estimada']:.6f}"
        )
    if informe.get("desplazamiento_maximo"):
        d = informe["desplazamiento_maximo"]
        lineas.append(f"Caso {informe['caso']}: desplazamiento máximo {d['total_m'] * 1000:.2f} mm en nodo {d['nodo']}")
    for d in informe.get("derivas", []):
        estado = "" if d["cumple"] is None else ("  CUMPLE" if d["cumple"] else "  NO CUMPLE")
        lineas.append(
            f"  Piso {d['nivel_inferior_m']:.2f}–{d['nivel_superior_m']:.2f} m: "
            f"deriva X {d['deriva_x']:.5f}  Y {d['deriva_y']:.5f}  máx {d['deriva_resultante']:.5f}{estado}"
        )
    if informe.get("zonificacion"):
        lineas.append(f"Zonificación: {informe['zonificacion']}")
    for nombre, ruta in informe["archivos"].items():
        lineas.append(f"Archivo {nombre}: {ruta}")
    for a in informe["advertencias"]:
        lineas.append(f"ADVERTENCIA: {a}")
    return "\n".join(lineas)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="tav0t.georef", description="Georreferenciación de análisis estructural")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_ej = sub.add_parser("ejecutar", help="Ejecuta un proyecto de georreferenciación")
    p_ej.add_argument("proyecto")
    p_ej.add_argument("--json", action="store_true", help="Imprime el informe completo en JSON")

    p_utm = sub.add_parser("utm", help="Convierte latitud/longitud a UTM")
    p_utm.add_argument("latitud", type=float)
    p_utm.add_argument("longitud", type=float)
    p_utm.add_argument("--zona", type=int)

    p_geo = sub.add_parser("geo", help="Convierte UTM a latitud/longitud")
    p_geo.add_argument("este", type=float)
    p_geo.add_argument("norte", type=float)
    p_geo.add_argument("zona", type=int)
    p_geo.add_argument("hemisferio", choices=["N", "S", "n", "s"])

    args = parser.parse_args(argv)
    try:
        if args.comando == "ejecutar":
            informe = ejecutar_proyecto(args.proyecto)
            print(json.dumps(informe, ensure_ascii=False, indent=2) if args.json else _resumen(informe))
        elif args.comando == "utm":
            c = geodesicas_a_utm(args.latitud, args.longitud, args.zona)
            print(
                f"Zona {c.zona}{c.hemisferio}  E {c.este:.4f}  N {c.norte:.4f}  "
                f"convergencia {c.convergencia:.6f}°  k {c.escala:.8f}"
            )
        else:
            lat, lon, gamma, k = utm_a_geodesicas(args.este, args.norte, args.zona, args.hemisferio)
            print(f"Latitud {lat:.9f}  Longitud {lon:.9f}  convergencia {gamma:.6f}°  k {k:.8f}")
    except (ValueError, KeyError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
