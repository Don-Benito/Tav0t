"""Escritura de resultados georreferenciados sin bibliotecas externas.

* GeoJSON (RFC 7946): para SIG (QGIS, ArcGIS) y visores web. Coordenadas
  [longitud, latitud, altura elipsoidal].
* KML: para Google Earth, con la estructura en 3D y colores por resultado.
* CSV: tabla de nodos con coordenadas geográficas y UTM.
* Informe JSON: parámetros, controles de calidad y resultados, para trazabilidad.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from xml.sax.saxutils import escape

from .modelo import ModeloEstructural
from .resultados import EscalaColores, NodoGeorreferenciado

DECIMALES_GRADOS = 9  # ~0.1 mm
DECIMALES_METROS = 4


def _r(valor: float | None, decimales: int = DECIMALES_METROS) -> float | None:
    return None if valor is None else round(valor, decimales)


def _coord(lon: float, lat: float, h: float) -> list[float]:
    return [round(lon, DECIMALES_GRADOS), round(lat, DECIMALES_GRADOS), round(h, DECIMALES_METROS)]


def _anillo_antihorario(coords: list[list[float]]) -> list[list[float]]:
    """RFC 7946 pide anillos exteriores en sentido antihorario."""
    area = 0.0
    for (x1, y1, *_), (x2, y2, *_) in zip(coords, coords[1:] + coords[:1]):
        area += x1 * y2 - x2 * y1
    anillo = list(reversed(coords)) if area < 0 else list(coords)
    return anillo + [anillo[0]]


def _propiedades_nodo(n: NodoGeorreferenciado) -> dict:
    props = {
        "capa": "nodos",
        "id": n.id,
        "x": n.x,
        "y": n.y,
        "z": n.z,
        "altura_elipsoidal": _r(n.h),
        "altura_ortometrica": _r(n.altura_ortometrica),
        "utm_este": _r(n.este),
        "utm_norte": _r(n.norte),
        "utm_zona": f"{n.zona}{n.hemisferio}",
    }
    if n.desplazamiento_enu is not None:
        de, dn, du = n.desplazamiento_enu
        props.update(
            {
                "despl_este_m": _r(de, 6),
                "despl_norte_m": _r(dn, 6),
                "despl_vertical_m": _r(du, 6),
                "despl_total_m": _r(n.desplazamiento_total, 6),
                "despl_horizontal_m": _r(n.desplazamiento_horizontal, 6),
                "acimut_despl": _r(n.acimut_desplazamiento, 2),
            }
        )
    return props


def construir_geojson(
    modelo: ModeloEstructural,
    nodos_geo: list[NodoGeorreferenciado],
    valores_elementos: dict[str, float] | None = None,
    escala: EscalaColores | None = None,
    metrica: str | None = None,
    incluir_deformada: bool = True,
    metadatos: dict | None = None,
) -> dict:
    valores_elementos = valores_elementos or {}
    por_id = {n.id: n for n in nodos_geo}
    features = []

    for el in modelo.elementos.values():
        coords = [_coord(por_id[n].lon, por_id[n].lat, por_id[n].h) for n in el.nodos]
        props = {"capa": "elementos", "id": el.id, "tipo": el.tipo, "nodos": el.nodos, **el.propiedades}
        valor = valores_elementos.get(el.id)
        if metrica and valor is not None:
            props[metrica] = valor
            if escala:
                props["clase"] = escala.clase(valor)
                props["color"] = escala.color(valor)
        features.append({"type": "Feature", "geometry": _geometria(el.tipo, coords), "properties": props})

        if incluir_deformada and all(por_id[n].posicion_deformada for n in el.nodos):
            coords_def = [_coord(p[1], p[0], p[2]) for p in (por_id[n].posicion_deformada for n in el.nodos)]
            props_def = {"capa": "deformada", "id": el.id, "tipo": el.tipo}
            if "color" in props:
                props_def["color"] = props["color"]
            features.append({"type": "Feature", "geometry": _geometria(el.tipo, coords_def), "properties": props_def})

    for n in nodos_geo:
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": _coord(n.lon, n.lat, n.h)},
                "properties": _propiedades_nodo(n),
            }
        )

    salida = {"type": "FeatureCollection", "features": features}
    if metadatos:
        # Miembro extranjero permitido por RFC 7946 §6.1; los SIG lo ignoran.
        salida["tav0t"] = metadatos
    return salida


def _geometria(tipo: str, coords: list[list[float]]) -> dict:
    if tipo == "area":
        return {"type": "Polygon", "coordinates": [_anillo_antihorario(coords)]}
    return {"type": "LineString", "coordinates": coords}


def exportar_geojson(ruta: str | Path, geojson: dict) -> Path:
    ruta = Path(ruta)
    ruta.write_text(json.dumps(geojson, ensure_ascii=False, indent=1), encoding="utf-8")
    return ruta


# --- KML ----------------------------------------------------------------------------


def _color_kml(hex_rgb: str, alfa: str = "ff") -> str:
    """KML usa el orden aabbggrr."""
    h = hex_rgb.lstrip("#")
    return f"{alfa}{h[4:6]}{h[2:4]}{h[0:2]}".lower()


def construir_kml(
    nombre: str,
    modelo: ModeloEstructural,
    nodos_geo: list[NodoGeorreferenciado],
    valores_elementos: dict[str, float] | None = None,
    escala: EscalaColores | None = None,
    metrica: str | None = None,
    modo_altitud: str = "relativa",
    factor_deformada: float = 0.0,
    incluir_nodos: bool = True,
    amarre: tuple[float, float, float] | None = None,
) -> str:
    """Genera el KML.

    ``modo_altitud``:
      * ``"relativa"``: altura sobre el nivel más bajo del modelo, apoyada en
        el terreno de Google Earth (``relativeToGround``). No requiere conocer
        la ondulación geoidal y es la opción más robusta para visualizar.
      * ``"absoluta"``: altura ortométrica (h − N) sobre el nivel del mar
        (``absolute``). Requiere haber indicado la ondulación geoidal correcta.
    """
    if modo_altitud not in ("relativa", "absoluta"):
        raise ValueError("modo_altitud debe ser 'relativa' o 'absoluta'")
    valores_elementos = valores_elementos or {}
    por_id = {n.id: n for n in nodos_geo}
    h_min = min(n.h for n in nodos_geo)
    modo_kml = "relativeToGround" if modo_altitud == "relativa" else "absolute"

    def alt(n_h: float, n_orto: float) -> float:
        return n_h - h_min if modo_altitud == "relativa" else n_orto

    def coords_nodos(ids: list[str], deformada: bool = False, cerrar: bool = False) -> str:
        partes = []
        for nid in ids + ([ids[0]] if cerrar else []):
            n = por_id[nid]
            if deformada:
                lat, lon, h = n.posicion_deformada
                orto = h - (n.h - n.altura_ortometrica)
            else:
                lat, lon, h, orto = n.lat, n.lon, n.h, n.altura_ortometrica
            partes.append(f"{lon:.{DECIMALES_GRADOS}f},{lat:.{DECIMALES_GRADOS}f},{alt(h, orto):.3f}")
        return " ".join(partes)

    colores = list(escala.colores) if escala else []
    estilos = [
        (
            '<Style id="base"><LineStyle><color>ff9a9a9a</color><width>3</width></LineStyle>'
            "<PolyStyle><color>809a9a9a</color></PolyStyle></Style>"
        ),
        (
            '<Style id="nodo"><IconStyle><scale>0.4</scale><Icon><href>'
            "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href></Icon></IconStyle>"
            "<LabelStyle><scale>0</scale></LabelStyle></Style>"
        ),
    ]
    for i, c in enumerate(colores):
        estilos.append(
            f'<Style id="clase{i}"><LineStyle><color>{_color_kml(c)}</color><width>4</width></LineStyle>'
            f"<PolyStyle><color>{_color_kml(c, '99')}</color></PolyStyle></Style>"
        )

    def placemark_elemento(el, deformada: bool) -> str:
        valor = valores_elementos.get(el.id)
        clase = escala.clase(valor) if (escala and valor is not None) else None
        estilo = f"#clase{clase}" if clase is not None else "#base"
        desc = f"Tipo: {el.tipo}<br/>Nodos: {', '.join(el.nodos)}"
        if metrica and valor is not None:
            desc += f"<br/>{metrica}: {valor:.4g}"
        if el.tipo == "area":
            geom = (
                f"<Polygon><altitudeMode>{modo_kml}</altitudeMode><outerBoundaryIs><LinearRing><coordinates>"
                f"{coords_nodos(el.nodos, deformada, cerrar=True)}</coordinates></LinearRing></outerBoundaryIs></Polygon>"
            )
        else:
            geom = (
                f"<LineString><altitudeMode>{modo_kml}</altitudeMode><coordinates>"
                f"{coords_nodos(el.nodos, deformada)}</coordinates></LineString>"
            )
        return (
            f"<Placemark><name>{escape(el.id)}</name><description><![CDATA[{desc}]]></description>"
            f"<styleUrl>{estilo}</styleUrl>{geom}</Placemark>"
        )

    carpetas = []
    carpetas.append(
        "<Folder><name>Estructura</name>"
        + "".join(placemark_elemento(el, False) for el in modelo.elementos.values())
        + "</Folder>"
    )
    if factor_deformada:
        deformables = [
            el for el in modelo.elementos.values() if all(por_id[n].posicion_deformada for n in el.nodos)
        ]
        if deformables:
            carpetas.append(
                f"<Folder><name>Deformada (x{factor_deformada:g})</name><visibility>0</visibility>"
                + "".join(placemark_elemento(el, True) for el in deformables)
                + "</Folder>"
            )
    if incluir_nodos:
        marcas = []
        for n in nodos_geo:
            desc = (
                f"Modelo: ({n.x:g}, {n.y:g}, {n.z:g})<br/>"
                f"Lat/Lon: {n.lat:.8f}, {n.lon:.8f}<br/>"
                f"UTM {n.zona}{n.hemisferio}: E {n.este:.3f}  N {n.norte:.3f}<br/>"
                f"h elipsoidal: {n.h:.3f} m  H ortométrica: {n.altura_ortometrica:.3f} m"
            )
            if n.desplazamiento_enu is not None:
                desc += f"<br/>Desplazamiento total: {n.desplazamiento_total * 1000:.2f} mm"
            marcas.append(
                f"<Placemark><name>{escape(n.id)}</name><description><![CDATA[{desc}]]></description>"
                f"<styleUrl>#nodo</styleUrl><Point><altitudeMode>{modo_kml}</altitudeMode>"
                f"<coordinates>{coords_nodos([n.id])}</coordinates></Point></Placemark>"
            )
        carpetas.append("<Folder><name>Nodos</name><visibility>0</visibility>" + "".join(marcas) + "</Folder>")
    if amarre:
        carpetas.append(
            f"<Placemark><name>Punto de amarre</name><Point><coordinates>"
            f"{amarre[1]:.{DECIMALES_GRADOS}f},{amarre[0]:.{DECIMALES_GRADOS}f},0</coordinates></Point></Placemark>"
        )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<kml xmlns="http://www.opengis.net/kml/2.2"><Document>'
        f"<name>{escape(nombre)}</name>" + "".join(estilos) + "".join(carpetas) + "</Document></kml>\n"
    )


def exportar_kml(ruta: str | Path, kml: str) -> Path:
    ruta = Path(ruta)
    ruta.write_text(kml, encoding="utf-8")
    return ruta


# --- CSV -------------------------------------------------------------------------------


def exportar_csv_nodos(ruta: str | Path, nodos_geo: list[NodoGeorreferenciado]) -> Path:
    ruta = Path(ruta)
    columnas = [
        "id", "x", "y", "z", "latitud", "longitud", "altura_elipsoidal", "altura_ortometrica",
        "utm_zona", "utm_este", "utm_norte",
        "despl_este_m", "despl_norte_m", "despl_vertical_m", "despl_total_m",
    ]  # fmt: skip
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(columnas)
        for n in nodos_geo:
            d = n.desplazamiento_enu or (None, None, None)
            w.writerow(
                [
                    n.id, n.x, n.y, n.z,
                    f"{n.lat:.{DECIMALES_GRADOS}f}", f"{n.lon:.{DECIMALES_GRADOS}f}",
                    f"{n.h:.4f}", f"{n.altura_ortometrica:.4f}",
                    f"{n.zona}{n.hemisferio}", f"{n.este:.4f}", f"{n.norte:.4f}",
                    *("" if v is None else f"{v:.6f}" for v in d),
                    "" if n.desplazamiento_total is None else f"{n.desplazamiento_total:.6f}",
                ]
            )  # fmt: skip
    return ruta


def exportar_informe(ruta: str | Path, informe: dict) -> Path:
    ruta = Path(ruta)
    ruta.write_text(json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8")
    return ruta
