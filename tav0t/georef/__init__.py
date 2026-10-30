"""Módulo de georreferenciación de análisis estructural de Tav0t.

Motor propio, sin dependencias externas (solo biblioteca estándar de Python).
La especificación completa está en ``docs/GUION_DE_FUNCIONAMIENTO.md``.

Uso mínimo::

    from tav0t.georef import ejecutar_proyecto
    informe = ejecutar_proyecto("ejemplos/proyecto_parametrico.json")
"""

from .elipsoide import GRS80, INTERNACIONAL_1924, WGS84, Elipsoide, obtener_elipsoide
from .geodesia import MarcoENU, ecef_a_geodesicas, geodesicas_a_ecef, helmert_7p
from .modelo import ModeloEstructural, cargar_csv, cargar_json, modelo_desde_dict
from .motor import ErrorConfiguracion, ejecutar, ejecutar_proyecto
from .resultados import EscalaColores, calcular_derivas, georreferenciar_modelo
from .transformacion import Georreferencia, PuntoControl, ajustar_puntos_control
from .utm import CoordenadaUTM, geodesicas_a_utm, utm_a_geodesicas, zona_utm
from .zonificacion import Zonificacion

__all__ = [
    "GRS80",
    "INTERNACIONAL_1924",
    "WGS84",
    "CoordenadaUTM",
    "Elipsoide",
    "ErrorConfiguracion",
    "EscalaColores",
    "Georreferencia",
    "MarcoENU",
    "ModeloEstructural",
    "PuntoControl",
    "Zonificacion",
    "ajustar_puntos_control",
    "calcular_derivas",
    "cargar_csv",
    "cargar_json",
    "ecef_a_geodesicas",
    "ejecutar",
    "ejecutar_proyecto",
    "geodesicas_a_ecef",
    "geodesicas_a_utm",
    "georreferenciar_modelo",
    "helmert_7p",
    "modelo_desde_dict",
    "obtener_elipsoide",
    "utm_a_geodesicas",
    "zona_utm",
]
