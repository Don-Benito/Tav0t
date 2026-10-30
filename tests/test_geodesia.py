import itertools
import math
import unittest

from tav0t.georef.elipsoide import GRS80, INTERNACIONAL_1924, WGS84, obtener_elipsoide
from tav0t.georef.geodesia import MarcoENU, ecef_a_geodesicas, geodesicas_a_ecef, helmert_7p


class TestElipsoide(unittest.TestCase):
    def test_constantes_wgs84(self):
        self.assertAlmostEqual(WGS84.b, 6356752.314245, places=5)
        self.assertAlmostEqual(WGS84.e2, 0.00669437999014, places=13)

    def test_obtener_por_nombre(self):
        self.assertIs(obtener_elipsoide("grs80"), GRS80)
        self.assertIs(obtener_elipsoide("INTERNACIONAL_1924"), INTERNACIONAL_1924)
        with self.assertRaises(ValueError):
            obtener_elipsoide("CLARKE")


class TestECEF(unittest.TestCase):
    def test_ecuador_greenwich(self):
        x, y, z = geodesicas_a_ecef(0.0, 0.0, 0.0)
        self.assertAlmostEqual(x, WGS84.a, places=6)
        self.assertAlmostEqual(y, 0.0, places=6)
        self.assertAlmostEqual(z, 0.0, places=6)

    def test_polo_norte(self):
        x, y, z = geodesicas_a_ecef(90.0, 0.0, 100.0)
        self.assertAlmostEqual(math.hypot(x, y), 0.0, places=6)
        self.assertAlmostEqual(z, WGS84.b + 100.0, places=6)

    def test_valor_de_referencia(self):
        # Referencia independiente calculada con PROJ (EPSG:4979 -> EPSG:4978).
        x, y, z = geodesicas_a_ecef(4.651, -74.055, 2604.0)
        self.assertAlmostEqual(x, 1747148.3364164394, places=5)
        self.assertAlmostEqual(y, -6115179.140642352, places=5)
        self.assertAlmostEqual(z, 513938.7947864924, places=5)

    def test_ida_y_vuelta(self):
        for lat, lon, h in itertools.product((-89.9, -45.0, -4.6, 0.0, 12.3, 60.0, 89.99), (-179.0, -74.0, 0.0, 120.0), (-400.0, 0.0, 2600.0, 9000.0)):
            lat2, lon2, h2 = ecef_a_geodesicas(*geodesicas_a_ecef(lat, lon, h))
            self.assertAlmostEqual(lat2, lat, places=11)
            self.assertAlmostEqual(lon2, lon, places=11)
            self.assertAlmostEqual(h2, h, places=6)


class TestENU(unittest.TestCase):
    def setUp(self):
        self.marco = MarcoENU(4.651, -74.055, 2604.0)

    def test_origen_es_cero(self):
        e, n, u = self.marco.desde_geodesicas(4.651, -74.055, 2604.0)
        for c in (e, n, u):
            self.assertAlmostEqual(c, 0.0, places=6)

    def test_direcciones(self):
        # 1 km al norte: la longitud no cambia y la latitud aumenta.
        lat, lon, _ = self.marco.a_geodesicas(0.0, 1000.0, 0.0)
        self.assertGreater(lat, 4.651)
        self.assertAlmostEqual(lon, -74.055, places=10)
        # 1 km al este: la longitud aumenta.
        lat, lon, _ = self.marco.a_geodesicas(1000.0, 0.0, 0.0)
        self.assertGreater(lon, -74.055)
        # Arriba: la altura aumenta lo mismo.
        _, _, h = self.marco.a_geodesicas(0.0, 0.0, 30.0)
        self.assertAlmostEqual(h, 2634.0, places=6)

    def test_ida_y_vuelta(self):
        for enu in ((0.0, 0.0, 0.0), (123.4, -56.7, 8.9), (-2500.0, 1800.0, -40.0)):
            vuelta = self.marco.desde_geodesicas(*self.marco.a_geodesicas(*enu))
            for a, b in zip(enu, vuelta):
                self.assertAlmostEqual(a, b, places=6)

    def test_conserva_distancias(self):
        p1 = self.marco.a_ecef(10.0, 20.0, 3.0)
        p2 = self.marco.a_ecef(-40.0, 65.0, 33.0)
        self.assertAlmostEqual(math.dist(p1, p2), math.dist((10, 20, 3), (-40, 65, 33)), places=8)


class TestHelmert(unittest.TestCase):
    PARAMS = dict(tx=-288.0, ty=175.0, tz=-376.0, rx_seg=1.2, ry_seg=-0.8, rz_seg=2.1, s_ppm=3.5)
    PUNTO = (1700000.0, -6000000.0, 500000.0)

    def test_vector_posicion_contra_proj(self):
        x, y, z = helmert_7p(self.PUNTO, **self.PARAMS, convencion="vector_posicion")
        self.assertAlmostEqual(x, 1699777.0974761108, places=6)
        self.assertAlmostEqual(y, -5999831.600983276, places=6)
        self.assertAlmostEqual(z, 499597.43678192736, places=6)

    def test_marco_coordenadas_contra_proj(self):
        x, y, z = helmert_7p(self.PUNTO, **self.PARAMS, convencion="marco_coordenadas")
        self.assertAlmostEqual(x, 1699658.8025238893, places=6)
        self.assertAlmostEqual(y, -5999860.399016725, places=6)
        self.assertAlmostEqual(z, 499654.0632180727, places=6)

    def test_inversa_exacta(self):
        ida = helmert_7p(self.PUNTO, **self.PARAMS)
        vuelta = helmert_7p(ida, **self.PARAMS, inversa=True)
        for a, b in zip(self.PUNTO, vuelta):
            self.assertAlmostEqual(a, b, places=6)

    def test_convencion_invalida(self):
        with self.assertRaises(ValueError):
            helmert_7p(self.PUNTO, **self.PARAMS, convencion="otra")


if __name__ == "__main__":
    unittest.main()
