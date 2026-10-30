import unittest
from pathlib import Path

from tav0t.georef.zonificacion import Zonificacion

EJEMPLO = Path(__file__).resolve().parent.parent / "ejemplos" / "zonificacion_ficticia.geojson"


class TestZonificacion(unittest.TestCase):
    def setUp(self):
        self.z = Zonificacion.desde_archivo(EJEMPLO)

    def test_dentro(self):
        self.assertEqual(self.z.consultar(4.651, -74.055)["zona"], "Z-2 (ficticia)")
        self.assertEqual(self.z.consultar(4.7, -73.9)["zona"], "Z-3 (ficticia)")

    def test_hueco_y_multipoligono(self):
        # El hueco de Z-2 está cubierto por la segunda parte del multipolígono Z-3.
        self.assertEqual(self.z.consultar(4.575, -74.125)["zona"], "Z-3 (ficticia)")

    def test_fuera(self):
        self.assertIsNone(self.z.consultar(10.0, -74.0))

    def test_sin_poligonos(self):
        with self.assertRaises(ValueError):
            Zonificacion({"type": "FeatureCollection", "features": []})


if __name__ == "__main__":
    unittest.main()
