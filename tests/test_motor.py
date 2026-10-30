import contextlib
import io
import json
import math
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from tav0t.georef import cargar_csv, cargar_json
from tav0t.georef.cli import main
from tav0t.georef.motor import ErrorConfiguracion, ejecutar

EJEMPLOS = Path(__file__).resolve().parent.parent / "ejemplos"


def _config(nombre: str, salida: Path) -> dict:
    config = json.loads((EJEMPLOS / nombre).read_text(encoding="utf-8"))
    config["salidas"]["directorio"] = str(salida)
    return config


class TestMotor(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_proyecto_parametrico(self):
        informe = ejecutar(_config("proyecto_parametrico.json", self.tmp), EJEMPLOS)
        self.assertEqual(informe["modelo"], {
            "nodos": 36, "elementos": 75, "unidades": "m", "eje_vertical": "Z", "casos": ["SISMO_X"],
        })  # fmt: skip
        self.assertEqual(informe["cuadricula_utm"]["zona"], 18)
        self.assertEqual(informe["zonificacion"]["zona"], "Z-2 (ficticia)")
        self.assertEqual(len(informe["derivas"]), 3)
        self.assertTrue(all(d["cumple"] for d in informe["derivas"]))
        for formato in ("geojson", "kml", "csv", "informe"):
            self.assertTrue(Path(informe["archivos"][formato]).is_file(), formato)

        gj = json.loads(Path(informe["archivos"]["geojson"]).read_text(encoding="utf-8"))
        self.assertEqual(gj["type"], "FeatureCollection")
        capas = {f["properties"]["capa"] for f in gj["features"]}
        self.assertEqual(capas, {"nodos", "elementos", "deformada"})
        punto = next(f for f in gj["features"] if f["geometry"]["type"] == "Point")
        lon, lat, h = punto["geometry"]["coordinates"]
        self.assertAlmostEqual(lon, -74.055, delta=0.001)  # orden RFC 7946: lon, lat
        self.assertAlmostEqual(lat, 4.651, delta=0.001)
        losa = next(f for f in gj["features"] if f["geometry"]["type"] == "Polygon")
        anillo = losa["geometry"]["coordinates"][0]
        self.assertEqual(anillo[0], anillo[-1])
        area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(anillo, anillo[1:]))
        self.assertGreater(area, 0)  # antihorario
        columna = next(f for f in gj["features"] if f["properties"]["id"] == "C1-11")
        self.assertIn("color", columna["properties"])

        raiz = ET.parse(informe["archivos"]["kml"]).getroot()
        ns = {"k": "http://www.opengis.net/kml/2.2"}
        self.assertEqual(len(raiz.findall(".//k:Folder", ns)), 3)

        lineas = Path(informe["archivos"]["csv"]).read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lineas), 37)

    def test_geometria_rigida_en_el_resultado(self):
        """Las distancias entre nodos georreferenciados son las del modelo."""
        from tav0t.georef.geodesia import geodesicas_a_ecef

        informe = ejecutar(_config("proyecto_parametrico.json", self.tmp), EJEMPLOS)
        gj = json.loads(Path(informe["archivos"]["geojson"]).read_text(encoding="utf-8"))
        nodos = {f["properties"]["id"]: f for f in gj["features"] if f["properties"]["capa"] == "nodos"}
        a, b = nodos["001"], nodos["323"]  # (0, 0, 0) y (12, 10, 9.5)
        pa = geodesicas_a_ecef(a["geometry"]["coordinates"][1], a["geometry"]["coordinates"][0], a["geometry"]["coordinates"][2])
        pb = geodesicas_a_ecef(b["geometry"]["coordinates"][1], b["geometry"]["coordinates"][0], b["geometry"]["coordinates"][2])
        self.assertAlmostEqual(math.dist(pa, pb), math.dist((0, 0, 0), (12, 10, 9.5)), delta=0.001)

    def test_puntos_control(self):
        informe = ejecutar(_config("proyecto_puntos_control.json", self.tmp), EJEMPLOS)
        ajuste = informe["ajuste_puntos_control"]
        self.assertLess(ajuste["rms_horizontal_m"], 0.01)
        self.assertEqual(len(ajuste["residuos"]), 4)
        self.assertAlmostEqual(informe["georreferencia"]["acimut_eje_x"], 72.5, delta=0.05)

    def test_csv_equivale_a_json(self):
        m_json = cargar_json(EJEMPLOS / "edificio_3p.json")
        m_csv = cargar_csv(
            EJEMPLOS / "csv" / "nodos.csv",
            EJEMPLOS / "csv" / "elementos.csv",
            EJEMPLOS / "csv" / "desplazamientos.csv",
            caso="SISMO_X",
            unidades_resultados="mm",
        )
        self.assertEqual(m_json.nodos, m_csv.nodos)
        self.assertEqual({k: v.nodos for k, v in m_json.elementos.items()}, {k: v.nodos for k, v in m_csv.elementos.items()})
        self.assertEqual(m_json.resultados["SISMO_X"].desplazamientos, m_csv.resultados["SISMO_X"].desplazamientos)
        informe = ejecutar(_config("proyecto_csv.json", self.tmp), EJEMPLOS)
        self.assertEqual(informe["caso"], "SISMO_X")
        self.assertAlmostEqual(informe["cuadricula_utm"]["acimut_x_cuadricula"], 72.5, places=9)

    def test_errores_de_configuracion(self):
        config = _config("proyecto_parametrico.json", self.tmp)
        config["resultados"]["caso"] = "NO_EXISTE"
        with self.assertRaises(ErrorConfiguracion):
            ejecutar(config, EJEMPLOS)
        config = _config("proyecto_parametrico.json", self.tmp)
        config["salidas"]["formatos"] = ["dwg"]
        with self.assertRaises(ErrorConfiguracion):
            ejecutar(config, EJEMPLOS)
        config = _config("proyecto_parametrico.json", self.tmp)
        config["georreferencia"]["metodo"] = "magia"
        with self.assertRaises(ErrorConfiguracion):
            ejecutar(config, EJEMPLOS)
        config = _config("proyecto_parametrico.json", self.tmp)
        del config["georreferencia"]["acimut_eje_x"]
        with self.assertRaises(ErrorConfiguracion):
            ejecutar(config, EJEMPLOS)

    def test_advierte_sin_ondulacion(self):
        config = _config("proyecto_parametrico.json", self.tmp)
        del config["ondulacion_geoidal"]
        informe = ejecutar(config, EJEMPLOS)
        self.assertTrue(any("ondulacion_geoidal" in a for a in informe["advertencias"]))

    def test_datum_local(self):
        # Coordenadas de amarre en un datum local ficticio: el desplazamiento
        # Helmert solo-traslación debe mover el resultado en la misma cantidad.
        config = _config("proyecto_parametrico.json", self.tmp)
        config["salidas"]["formatos"] = ["informe"]
        base = ejecutar(config, EJEMPLOS)["georreferencia"]
        config["datum_origen"] = {"elipsoide": "WGS84", "tx": 0.0, "ty": 0.0, "tz": 100.0}
        movido = ejecutar(config, EJEMPLOS)["georreferencia"]
        self.assertGreater(movido["latitud"], base["latitud"])


class TestCLI(unittest.TestCase):
    def _ejecutar(self, *args):
        salida, errores = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(salida), contextlib.redirect_stderr(errores):
            codigo = main(list(args))
        return codigo, salida.getvalue(), errores.getvalue()

    def test_utm_y_geo(self):
        codigo, salida, _ = self._ejecutar("utm", "4.651", "-74.055")
        self.assertEqual(codigo, 0)
        self.assertIn("18N", salida)
        self.assertIn("604815.6034", salida)
        codigo, salida, _ = self._ejecutar("geo", "604815.6034", "514156.6625", "18", "N")
        self.assertEqual(codigo, 0)
        self.assertIn("4.6510000", salida)

    def test_error_devuelve_2(self):
        codigo, _, errores = self._ejecutar("utm", "88", "0")
        self.assertEqual(codigo, 2)
        self.assertIn("Error", errores)
        codigo, _, _ = self._ejecutar("ejecutar", "no_existe.json")
        self.assertEqual(codigo, 2)


if __name__ == "__main__":
    unittest.main()
