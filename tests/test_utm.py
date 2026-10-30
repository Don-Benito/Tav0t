import random
import unittest

from tav0t.georef.utm import geodesicas_a_utm, meridiano_central, utm_a_geodesicas, zona_utm

# Valores de referencia independientes calculados con PROJ:
# (lat, lon, zona, hemisferio, este, norte, convergencia°, k)
REFERENCIAS = [
    (4.651, -74.055, 18, "N", 604815.6034, 514156.6625, 0.07663345, 0.9997359869),
    (-33.45, -70.66, 19, "S", 345713.1543, 6297592.0284, 0.91518784, 0.9998934831),
    (19.43, -99.13, 14, "N", 486353.0342, 2148412.2648, -0.04324521, 0.9996023020),
    (-12.05, -77.04, 18, "S", 277925.3458, 8667091.8511, 0.42605657, 1.0002101867),
    (40.4168, -3.7038, 30, "N", 440290.4581, 4474257.3820, -0.45631738, 0.9996438850),
    (-0.18, -78.47, 17, "S", 781616.4238, 9980085.0481, -0.00795349, 1.0005818883),
]


class TestUTM(unittest.TestCase):
    def test_contra_referencias(self):
        for lat, lon, zona, hem, este, norte, gamma, k in REFERENCIAS:
            with self.subTest(lat=lat, lon=lon):
                c = geodesicas_a_utm(lat, lon)
                self.assertEqual((c.zona, c.hemisferio), (zona, hem))
                self.assertAlmostEqual(c.este, este, places=3)
                self.assertAlmostEqual(c.norte, norte, places=3)
                self.assertAlmostEqual(c.convergencia, gamma, places=7)
                self.assertAlmostEqual(c.escala, k, places=9)

    def test_inversa_contra_referencias(self):
        for lat, lon, zona, hem, este, norte, gamma, k in REFERENCIAS:
            with self.subTest(lat=lat, lon=lon):
                lat2, lon2, gamma2, k2 = utm_a_geodesicas(este, norte, zona, hem)
                self.assertAlmostEqual(lat2, lat, places=8)
                self.assertAlmostEqual(lon2, lon, places=8)
                self.assertAlmostEqual(gamma2, gamma, places=6)
                self.assertAlmostEqual(k2, k, places=8)

    def test_ida_y_vuelta_aleatoria(self):
        rnd = random.Random(42)
        for _ in range(500):
            lat, lon = rnd.uniform(-79.9, 83.9), rnd.uniform(-179.9, 179.9)
            c = geodesicas_a_utm(lat, lon)
            lat2, lon2, gamma2, k2 = utm_a_geodesicas(c.este, c.norte, c.zona, c.hemisferio)
            self.assertAlmostEqual(lat2, lat, places=10)
            self.assertAlmostEqual(lon2, lon, places=10)
            self.assertAlmostEqual(gamma2, c.convergencia, places=9)
            self.assertAlmostEqual(k2, c.escala, places=11)

    def test_meridiano_central(self):
        c = geodesicas_a_utm(0.0, -75.0)
        self.assertAlmostEqual(c.este, 500000.0, places=6)
        self.assertAlmostEqual(c.norte, 0.0, places=6)
        self.assertAlmostEqual(c.convergencia, 0.0, places=12)
        self.assertAlmostEqual(c.escala, 0.9996, places=12)

    def test_zona_forzada(self):
        natural = geodesicas_a_utm(4.0, -71.9)
        forzada = geodesicas_a_utm(4.0, -71.9, zona=18)
        self.assertEqual(natural.zona, 19)
        self.assertEqual(forzada.zona, 18)
        lat, lon, _, _ = utm_a_geodesicas(forzada.este, forzada.norte, 18, "N")
        self.assertAlmostEqual(lon, -71.9, places=9)

    def test_zonas_especiales(self):
        self.assertEqual(zona_utm(4.6, -74.0), 18)
        self.assertEqual(zona_utm(60.0, 5.0), 32)  # Noruega
        self.assertEqual(zona_utm(78.0, 10.0), 33)  # Svalbard
        self.assertEqual(zona_utm(0.0, 180.0), 1)
        self.assertEqual(meridiano_central(18), -75.0)

    def test_fuera_de_dominio(self):
        with self.assertRaises(ValueError):
            geodesicas_a_utm(85.0, 0.0)
        with self.assertRaises(ValueError):
            utm_a_geodesicas(500000.0, 0.0, 18, "X")
        with self.assertRaises(ValueError):
            meridiano_central(61)


if __name__ == "__main__":
    unittest.main()
