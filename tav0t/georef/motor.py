"""Orquestador del módulo de georreferenciación.

Ejecuta el flujo completo a partir de una configuración de proyecto (dict o
archivo JSON) y devuelve un informe. Es el punto de entrada que debe usar la
plataforma; ver ``docs/GUION_DE_FUNCIONAMIENTO.md``.

Flujo:
    1. Validar configuración
    2. Cargar y validar el modelo
    3. Pasar coordenadas de referencia a WGS84 (datum y alturas)
    4. Construir la georreferencia (paramétrica o por puntos de control)
    5. Georreferenciar nodos, desplazamientos y deformada
    6. Calcular derivas de entrepiso
    7. Clasificar elementos por la métrica elegida
    8. Consultar la zonificación en el punto de amarre
    9. Exportar GeoJSON / KML / CSV
   10. Escribir el informe
"""

from __future__ import annotations

import datetime as _dt
import json
from pathlib import Path

from .. import __version__
from .elipsoide import WGS84, obtener_elipsoide
from .exportar import (
    construir_geojson,
    construir_kml,
    exportar_csv_nodos,
    exportar_geojson,
    exportar_informe,
    exportar_kml,
)
from .geodesia import ecef_a_geodesicas, geodesicas_a_ecef, helmert_7p
from .modelo import ModeloEstructural, cargar_csv, cargar_json
from .resultados import EscalaColores, calcular_derivas, georreferenciar_modelo, metrica_elementos
from .transformacion import Georreferencia, PuntoControl, ajustar_puntos_control, factor_unidad
from .utm import utm_a_geodesicas
from .zonificacion import Zonificacion

FORMATOS = ("geojson", "kml", "csv", "informe")


class ErrorConfiguracion(ValueError):
    pass


def _requerir(d: dict, clave: str, contexto: str):
    if clave not in d:
        raise ErrorConfiguracion(f"Falta '{clave}' en {contexto}.")
    return d[clave]


class _ConversorCoordenadas:
    """Lleva coordenadas de entrada (geodésicas o UTM, en cualquier datum, con
    altura ortométrica o elipsoidal) a geodésicas sobre el elipsoide destino."""

    def __init__(self, config: dict, elipsoide_destino):
        self.destino = elipsoide_destino
        self.ondulacion = float(config.get("ondulacion_geoidal", 0.0))
        datum = config.get("datum_origen")
        self.helmert = None
        self.origen = elipsoide_destino
        if datum:
            self.origen = obtener_elipsoide(_requerir(datum, "elipsoide", "datum_origen"))
            self.helmert = {
                k: float(datum.get(k, 0.0)) for k in ("tx", "ty", "tz", "rx_seg", "ry_seg", "rz_seg", "s_ppm")
            }
            self.convencion = datum.get("convencion", "vector_posicion")

    def convertir(self, punto: dict, tipo_altura: str, contexto: str) -> tuple[float, float, float]:
        if "utm" in punto:
            u = punto["utm"]
            lat, lon, _, _ = utm_a_geodesicas(
                float(_requerir(u, "este", contexto)),
                float(_requerir(u, "norte", contexto)),
                int(_requerir(u, "zona", contexto)),
                str(u.get("hemisferio", "N")),
                self.origen,
            )
        else:
            lat = float(_requerir(punto, "latitud", contexto))
            lon = float(_requerir(punto, "longitud", contexto))
        altura = float(punto.get("altura", 0.0))
        if tipo_altura == "ortometrica":
            h = altura + self.ondulacion
        elif tipo_altura == "elipsoidal":
            h = altura
        else:
            raise ErrorConfiguracion(f"tipo_altura inválido en {contexto}: '{tipo_altura}'.")

        if self.helmert:
            ecef = helmert_7p(geodesicas_a_ecef(lat, lon, h, self.origen), **self.helmert, convencion=self.convencion)
            lat, lon, h_nueva = ecef_a_geodesicas(*ecef, self.destino)
            if tipo_altura == "elipsoidal":
                h = h_nueva
            # Con altura ortométrica, la altura final sigue siendo H + N (N respecto al
            # elipsoide destino); el cambio de datum solo afecta a la posición horizontal.
        return lat, lon, h


def _cargar_modelo(cfg: dict, base: Path) -> ModeloEstructural:
    formato = cfg.get("formato", "json").lower()
    if formato == "json":
        return cargar_json(base / _requerir(cfg, "archivo", "modelo"))
    if formato == "csv":

        def opcional(clave: str) -> Path | None:
            return base / cfg[clave] if cfg.get(clave) else None

        return cargar_csv(
            base / _requerir(cfg, "nodos", "modelo"),
            opcional("elementos"),
            opcional("desplazamientos"),
            caso=cfg.get("caso", "CASO_1"),
            unidades=cfg.get("unidades", "m"),
            unidades_resultados=cfg.get("unidades_resultados"),
            eje_vertical=cfg.get("eje_vertical", "Z").upper(),
        )
    raise ErrorConfiguracion(f"Formato de modelo no soportado: '{formato}' (use 'json' o 'csv').")


def _construir_georreferencia(
    cfg: dict, modelo: ModeloEstructural, conversor: _ConversorCoordenadas, zona_utm: int | None
) -> tuple[Georreferencia, dict | None]:
    metodo = cfg.get("metodo", "parametrico")
    tipo_altura = cfg.get("tipo_altura", "ortometrica")
    unidad = factor_unidad(modelo.unidades)
    comunes = {"unidad": unidad, "eje_vertical": modelo.eje_vertical, "elipsoide": conversor.destino}

    if metodo == "parametrico":
        origen = dict(_requerir(cfg, "origen", "georreferencia"))
        origen.setdefault("altura", cfg.get("altura", 0.0))
        lat, lon, h = conversor.convertir(origen, tipo_altura, "georreferencia.origen")
        georef = Georreferencia.parametrica(
            lat,
            lon,
            h,
            float(_requerir(cfg, "acimut_eje_x", "georreferencia")),
            norte=cfg.get("norte", "verdadero"),
            zona=zona_utm,
            punto_modelo=tuple(cfg.get("punto_modelo", (0.0, 0.0, 0.0))),
            **comunes,
        )
        return georef, None

    if metodo == "puntos_control":
        puntos = []
        for i, p in enumerate(_requerir(cfg, "puntos", "georreferencia")):
            nombre = str(p.get("nombre", f"P{i + 1}"))
            contexto = f"punto de control '{nombre}'"
            m = _requerir(p, "modelo", contexto)
            if len(m) == 2:
                m = [m[0], m[1], 0.0]
            lat, lon, h = conversor.convertir(p, p.get("tipo_altura", tipo_altura), contexto)
            puntos.append(PuntoControl(nombre, (float(m[0]), float(m[1]), float(m[2])), lat, lon, h))
        ajuste = ajustar_puntos_control(
            puntos,
            permitir_escala=bool(cfg.get("permitir_escala", False)),
            tolerancia_horizontal=float(cfg.get("tolerancia_horizontal", 0.05)),
            tolerancia_vertical=float(cfg.get("tolerancia_vertical", 0.10)),
            **comunes,
        )
        return ajuste.georreferencia, ajuste.como_dict()

    raise ErrorConfiguracion(f"Método de georreferencia desconocido: '{metodo}'.")


def ejecutar(config: dict, base: str | Path = ".") -> dict:
    """Ejecuta el módulo con una configuración ya cargada.

    ``base`` es el directorio respecto al cual se resuelven las rutas
    relativas de la configuración.
    """
    base = Path(base)
    advertencias: list[str] = []

    # 1. Configuración
    nombre = config.get("nombre", "Proyecto")
    elipsoide = obtener_elipsoide(config.get("elipsoide", WGS84.nombre))
    cfg_salidas = config.get("salidas", {})
    formatos = cfg_salidas.get("formatos", list(FORMATOS))
    desconocidos = set(formatos) - set(FORMATOS)
    if desconocidos:
        raise ErrorConfiguracion(f"Formatos de salida desconocidos: {sorted(desconocidos)}.")
    zona_utm = config.get("zona_utm")

    # 2. Modelo
    modelo = _cargar_modelo(_requerir(config, "modelo", "la configuración"), base)
    advertencias += modelo.validar()

    # 3-4. Georreferencia
    conversor = _ConversorCoordenadas(config, elipsoide)
    tipo_altura = config.get("georreferencia", {}).get("tipo_altura", "ortometrica")
    if "ondulacion_geoidal" not in config and tipo_altura == "ortometrica":
        advertencias.append(
            "No se indicó 'ondulacion_geoidal': se asume N = 0, así que las alturas elipsoidales "
            "pueden tener un error de decenas de metros (no afecta a la planta)."
        )
    georef, ajuste = _construir_georreferencia(
        _requerir(config, "georreferencia", "la configuración"), modelo, conversor, zona_utm
    )
    if ajuste:
        advertencias += ajuste["advertencias"]
    cuadricula = georef.datos_cuadricula(zona_utm)

    # 5. Nodos y desplazamientos
    cfg_res = config.get("resultados", {})
    caso = None
    nombre_caso = cfg_res.get("caso")
    if nombre_caso:
        caso = modelo.resultados.get(nombre_caso)
        if caso is None:
            raise ErrorConfiguracion(
                f"El caso '{nombre_caso}' no existe. Casos disponibles: {sorted(modelo.resultados)}."
            )
    elif len(modelo.resultados) == 1:
        caso = next(iter(modelo.resultados.values()))
    elif modelo.resultados:
        advertencias.append(
            f"El modelo tiene varios casos {sorted(modelo.resultados)} y no se eligió ninguno: "
            "se georreferencia solo la geometría."
        )
    factor_deformada = float(cfg_salidas.get("factor_deformada", 0.0)) if caso else 0.0
    nodos_geo = georreferenciar_modelo(
        modelo, georef, caso, cuadricula["zona"], conversor.ondulacion, factor_deformada
    )

    # 6. Derivas
    derivas = []
    if caso:
        derivas = calcular_derivas(
            modelo,
            caso,
            float(cfg_res.get("factor_amplificacion_deriva", 1.0)),
            cfg_res.get("limite_deriva"),
            float(cfg_res.get("tolerancia_niveles", 0.05)),
        )
        incumplen = [d for d in derivas if d.cumple is False]
        if incumplen:
            advertencias.append(f"{len(incumplen)} piso(s) superan el límite de deriva.")

    # 7. Clasificación
    metrica = cfg_res.get("metrica_color")
    escala = EscalaColores(list(cfg_res["umbrales"])) if cfg_res.get("umbrales") else None
    valores = metrica_elementos(modelo, nodos_geo, caso, metrica) if metrica else {}

    # 8. Zonificación
    zona_info = None
    cfg_zon = config.get("zonificacion")
    if cfg_zon:
        zonas = Zonificacion.desde_archivo(base / _requerir(cfg_zon, "archivo", "zonificacion"))
        zona_info = zonas.consultar(georef.lat0, georef.lon0)
        if zona_info is None:
            advertencias.append("El punto de amarre queda fuera de todos los polígonos de zonificación.")

    # 9. Exportación
    directorio = base / cfg_salidas.get("directorio", "salida")
    directorio.mkdir(parents=True, exist_ok=True)
    prefijo = cfg_salidas.get("prefijo", "georref")
    archivos = {}
    metadatos = {"proyecto": nombre, "georreferencia": georef.como_dict(), "caso": caso.nombre if caso else None}
    if "geojson" in formatos:
        gj = construir_geojson(modelo, nodos_geo, valores, escala, metrica, factor_deformada > 0, metadatos)
        archivos["geojson"] = str(exportar_geojson(directorio / f"{prefijo}.geojson", gj))
    if "kml" in formatos:
        kml = construir_kml(
            nombre,
            modelo,
            nodos_geo,
            valores,
            escala,
            metrica,
            cfg_salidas.get("modo_altitud_kml", "relativa"),
            factor_deformada,
            bool(cfg_salidas.get("incluir_nodos_kml", True)),
            (georef.lat0, georef.lon0, georef.h0),
        )
        archivos["kml"] = str(exportar_kml(directorio / f"{prefijo}.kml", kml))
    if "csv" in formatos:
        archivos["csv"] = str(exportar_csv_nodos(directorio / f"{prefijo}_nodos.csv", nodos_geo))

    # 10. Informe
    con_despl = [n for n in nodos_geo if n.desplazamiento_total is not None]
    maximo = max(con_despl, key=lambda n: n.desplazamiento_total) if con_despl else None
    informe = {
        "motor": {"nombre": "tav0t.georef", "version": __version__},
        "proyecto": nombre,
        "fecha": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "georreferencia": georef.como_dict(),
        "cuadricula_utm": cuadricula,
        "ajuste_puntos_control": ajuste,
        "modelo": {
            "nodos": len(modelo.nodos),
            "elementos": len(modelo.elementos),
            "unidades": modelo.unidades,
            "eje_vertical": modelo.eje_vertical,
            "casos": sorted(modelo.resultados),
        },
        "extension": {
            "lat_min": min(n.lat for n in nodos_geo),
            "lat_max": max(n.lat for n in nodos_geo),
            "lon_min": min(n.lon for n in nodos_geo),
            "lon_max": max(n.lon for n in nodos_geo),
            "altura_ortometrica_min": min(n.altura_ortometrica for n in nodos_geo),
            "altura_ortometrica_max": max(n.altura_ortometrica for n in nodos_geo),
        },
        "caso": caso.nombre if caso else None,
        "desplazamiento_maximo": (
            {
                "nodo": maximo.id,
                "total_m": maximo.desplazamiento_total,
                "horizontal_m": maximo.desplazamiento_horizontal,
                "acimut_grados": maximo.acimut_desplazamiento,
            }
            if maximo
            else None
        ),
        "derivas": [d.como_dict() for d in derivas],
        "zonificacion": zona_info,
        "archivos": archivos,
        "advertencias": advertencias,
    }
    if "informe" in formatos:
        ruta_informe = directorio / f"{prefijo}_informe.json"
        informe["archivos"]["informe"] = str(ruta_informe)
        exportar_informe(ruta_informe, informe)
    return informe


def ejecutar_proyecto(ruta: str | Path) -> dict:
    """Carga un archivo de proyecto JSON y lo ejecuta."""
    ruta = Path(ruta)
    with open(ruta, encoding="utf-8") as f:
        config = json.load(f)
    return ejecutar(config, ruta.parent)
