import math
import random
import unittest

from tav0t.georef.geodesia import geodesicas_a_ecef
from tav0t.georef.transformacion import (
    Georreferencia,
    PuntoControl,
    ajustar_puntos_control,
    factor_unidad,
)
from tav0t.georef.utm import geodesicas_a_utm

LAT0, LON0, H0 = 4.651, -74.055, 2604.0


def _ecef(georef, p):
    return geodesicas_a_ecef(*georef.modelo_a_geodesicas(*p), georef.elipsoide)


class TestGeorreferenciaParametrica(unittest.TestCase):
    def test_punto_de_amarre(self):
        g = Georreferencia(LAT0, LON0, H0, 30.0, punto_modelo=(5.0, 2.0, 0.0))
        lat, lon, h = g.modelo_a_geodesicas(5.0, 2.0, 0.0)
        self.assertAlmostEqual(lat, LAT0, places=10)
        self.assertAlmostEqual(lon, LON0, places=10)
        self.assertAlmostEqual(h, H0, places=6)

    def test_orientacion_de_ejes(self):
        g = Georreferencia(LAT0, LON0, H0, 90.0)  # X hacia el Este
        self._enu(g.modelo_a_enu(100.0, 0.0, 0.0), (100.0, 0.0, 0.0))
        self._enu(g.modelo_a_enu(0.0, 100.0, 0.0), (0.0, 100.0, 0.0))  # Y al Norte
        g = Georreferencia(LAT0, LON0, H0, 0.0)  # X hacia el Norte
        self._enu(g.modelo_a_enu(100.0, 0.0, 0.0), (0.0, 100.0, 0.0))
        self._enu(g.modelo_a_enu(0.0, 100.0, 0.0), (-100.0, 0.0, 0.0))  # Y al Oeste
        g = Georreferencia(LAT0, LON0, H0, 45.0)
        e, n, _ = g.modelo_a_enu(10.0, 0.0, 0.0)
        self.assertAlmostEqual(e, n, places=9)
        self.assertGreater(e, 0)

    def _enu(self, obtenido, esperado):
        for a, b in zip(obtenido, esperado):
            self.assertAlmostEqual(a, b, places=9)

    def test_conserva_distancias_y_unidades(self):
        g = Georreferencia(LAT0, LON0, H0, 72.5, unidad=factor_unidad("mm"))
        a, b = (0.0, 0.0, 0.0), (12000.0, 10000.0, 9500.0)  # mm
        d_real = math.dist(_ecef(g, a), _ecef(g, b))
        self.assertAlmostEqual(d_real, math.dist(a, b) / 1000.0, places=7)

    def test_inversas(self):
        g = Georreferencia(LAT0, LON0, H0, 123.4, punto_modelo=(1.0, 2.0, 3.0), unidad=0.3048)
        p = (40.0, -25.0, 33.0)
        for a, b in zip(p, g.enu_a_modelo(*g.modelo_a_enu(*p))):
            self.assertAlmostEqual(a, b, places=9)
        for a, b in zip(p, g.geodesicas_a_modelo(*g.modelo_a_geodesicas(*p))):
            self.assertAlmostEqual(a, b, places=6)

    def test_eje_vertical_y(self):
        g = Georreferencia(LAT0, LON0, H0, 90.0, eje_vertical="Y")
        self._enu(g.modelo_a_enu(0.0, 10.0, 0.0), (0.0, 0.0, 10.0))
        self._enu(g.modelo_a_enu(5.0, 0.0, 0.0), (5.0, 0.0, 0.0))
        # Sistema dextrógiro con Y arriba: +Z del modelo apunta al Sur si X es Este.
        self._enu(g.modelo_a_enu(0.0, 0.0, 5.0), (0.0, -5.0, 0.0))
        p = (3.0, 7.0, -2.0)
        for a, b in zip(p, g.enu_a_modelo(*g.modelo_a_enu(*p))):
            self.assertAlmostEqual(a, b, places=9)

    def test_norte_de_cuadricula(self):
        gamma = geodesicas_a_utm(LAT0, LON0).convergencia
        g = Georreferencia.parametrica(LAT0, LON0, H0, 72.5, norte="cuadricula")
        self.assertAlmostEqual(g.acimut_x, 72.5 + gamma, places=12)
        self.assertAlmostEqual(g.datos_cuadricula()["acimut_x_cuadricula"], 72.5, places=10)
        with self.assertRaises(ValueError):
            Georreferencia.parametrica(LAT0, LON0, H0, 0.0, norte="magnetico")

    def test_acimut_de_cuadricula_coincide_con_utm(self):
        # Un eje X con acimut de cuadrícula 0° debe avanzar solo en Norte UTM.
        g = Georreferencia.parametrica(LAT0, LON0, H0, 0.0, norte="cuadricula")
        u0, _ = g.modelo_a_utm(0.0, 0.0, 0.0)
        u1, _ = g.modelo_a_utm(100.0, 0.0, 0.0)
        self.assertAlmostEqual(u1.este - u0.este, 0.0, places=4)
        # 100 m reales a 2604 m de altura equivalen a 100·k·factor_elevación en cuadrícula.
        # El informe usa el radio medio √(MN); en dirección norte rige el radio
        # meridiano M, de ahí una diferencia admisible de ~0.14 mm en 100 m.
        combinado = g.datos_cuadricula()["factor_combinado"]
        self.assertAlmostEqual(u1.norte - u0.norte, 100.0 * combinado, delta=5e-4)

    def test_rotar_vector_no_traslada(self):
        g = Georreferencia(LAT0, LON0, H0, 90.0, punto_modelo=(1000.0, 1000.0, 0.0))
        self._enu(g.rotar_vector(10.0, 0.0, 0.0, 0.001), (0.01, 0.0, 0.0))

    def test_datos_cuadricula(self):
        g = Georreferencia(LAT0, LON0, H0, 0.0)
        d = g.datos_cuadricula()
        self.assertEqual((d["zona"], d["hemisferio"]), (18, "N"))
        self.assertAlmostEqual(d["factor_combinado"], d["factor_escala_k"] * d["factor_elevacion"], places=15)
        self.assertLess(d["factor_elevacion"], 1.0)

    def test_validaciones(self):
        with self.assertRaises(ValueError):
            Georreferencia(95.0, 0.0, 0.0, 0.0)
        with self.assertRaises(ValueError):
            Georreferencia(0.0, 0.0, 0.0, 0.0, eje_vertical="X")
        with self.assertRaises(ValueError):
            factor_unidad("yardas")


def _puntos_desde(georef, coords_modelo, ruido=0.0, semilla=0):
    rnd = random.Random(semilla)
    puntos = []
    for i, c in enumerate(coords_modelo):
        e, n, u = georef.modelo_a_enu(*c)
        e += rnd.uniform(-ruido, ruido)
        n += rnd.uniform(-ruido, ruido)
        u += rnd.uniform(-ruido, ruido)
        lat, lon, h = georef._marco.a_geodesicas(e, n, u)
        puntos.append(PuntoControl(f"P{i + 1}", c, lat, lon, h))
    return puntos


class TestAjustePuntosControl(unittest.TestCase):
    COORDS = [(0.0, 0.0, 0.0), (30.0, 0.0, 0.0), (30.0, 20.0, 0.0), (0.0, 20.0, 3.0)]
    CENTROIDE = (15.0, 10.0, 0.75)

    def test_recupera_transformacion_exacta(self):
        # Con el amarre en el centroide de los puntos, el ajuste debe devolver
        # exactamente los mismos parámetros.
        real = Georreferencia(LAT0, LON0, H0, 37.3, punto_modelo=self.CENTROIDE)
        r = ajustar_puntos_control(_puntos_desde(real, self.COORDS))
        self.assertAlmostEqual(r.georreferencia.acimut_x, 37.3, places=9)
        self.assertAlmostEqual(r.georreferencia.lat0, LAT0, places=11)
        self.assertAlmostEqual(r.georreferencia.lon0, LON0, places=11)
        self.assertAlmostEqual(r.georreferencia.h0, H0, places=6)
        self.assertLess(r.rms_horizontal, 1e-6)
        self.assertLess(r.rms_vertical, 1e-6)
        self.assertEqual(r.advertencias, [])
        for p in ((15.0, 10.0, 9.0), (-50.0, 80.0, 30.0)):
            self.assertLess(math.dist(_ecef(real, p), _ecef(r.georreferencia, p)), 1e-6)

    def test_amarre_distinto_es_equivalente(self):
        # Si el amarre real está en otro punto, el acimut cambia en la
        # convergencia del plano tangente (~1e-5° en 18 m) y la vertical local
        # difiere unos microrradianes: diferencias sub-milimétricas.
        real = Georreferencia(LAT0, LON0, H0, 37.3)
        r = ajustar_puntos_control(_puntos_desde(real, self.COORDS))
        self.assertAlmostEqual(r.georreferencia.acimut_x, 37.3, delta=1e-4)
        self.assertLess(r.rms_horizontal, 1e-4)
        self.assertLess(r.rms_vertical, 1e-4)
        for p in ((15.0, 10.0, 9.0), (-50.0, 80.0, 30.0)):
            self.assertLess(math.dist(_ecef(real, p), _ecef(r.georreferencia, p)), 1e-3)

    def test_con_ruido(self):
        real = Georreferencia(LAT0, LON0, H0, 200.0)
        r = ajustar_puntos_control(_puntos_desde(real, self.COORDS, ruido=0.005, semilla=3))
        self.assertLess(r.rms_horizontal, 0.01)
        self.assertAlmostEqual(r.georreferencia.acimut_x, 200.0, delta=0.05)
        self.assertEqual(r.georreferencia.escala, 1.0)

    def test_y_vertical_y_milimetros(self):
        coords = [(0.0, 0.0, 0.0), (30000.0, 0.0, 0.0), (30000.0, 3000.0, -20000.0)]
        centroide = tuple(sum(c[i] for c in coords) / 3 for i in range(3))
        real = Georreferencia(LAT0, LON0, H0, 310.0, punto_modelo=centroide, unidad=0.001, eje_vertical="Y")
        r = ajustar_puntos_control(_puntos_desde(real, coords), unidad=0.001, eje_vertical="Y")
        self.assertAlmostEqual(r.georreferencia.acimut_x, 310.0, places=7)
        self.assertLess(r.rms_horizontal, 1e-6)

    def test_detecta_error_de_unidades(self):
        # El modelo está en cm pero se declara en m: la escala delata el error.
        real = Georreferencia(LAT0, LON0, H0, 10.0, unidad=0.01)
        coords = [(0.0, 0.0, 0.0), (3000.0, 0.0, 0.0), (3000.0, 2000.0, 0.0)]
        r = ajustar_puntos_control(_puntos_desde(real, coords), unidad=1.0)
        self.assertAlmostEqual(r.escala_estimada, 0.01, places=6)
        self.assertTrue(any("escala" in a for a in r.advertencias))
        self.assertTrue(any("RMS horizontal" in a for a in r.advertencias))

    def test_permitir_escala(self):
        real = Georreferencia(LAT0, LON0, H0, 10.0, punto_modelo=self.CENTROIDE, escala=1.0002)
        r = ajustar_puntos_control(_puntos_desde(real, self.COORDS), permitir_escala=True)
        self.assertAlmostEqual(r.georreferencia.escala, 1.0002, places=9)
        self.assertLess(r.rms_horizontal, 1e-6)

    def test_dos_puntos_advierte(self):
        real = Georreferencia(LAT0, LON0, H0, 10.0)
        r = ajustar_puntos_control(_puntos_desde(real, self.COORDS[:2]))
        self.assertTrue(any("redundancia" in a for a in r.advertencias))

    def test_errores(self):
        real = Georreferencia(LAT0, LON0, H0, 10.0)
        with self.assertRaises(ValueError):
            ajustar_puntos_control(_puntos_desde(real, self.COORDS[:1]))
        with self.assertRaises(ValueError):
            ajustar_puntos_control(_puntos_desde(real, [(1.0, 1.0, 0.0), (1.0, 1.0, 5.0)]))
        pts = _puntos_desde(real, self.COORDS[:2])
        with self.assertRaises(ValueError):
            ajustar_puntos_control([pts[0], pts[0]])


if __name__ == "__main__":
    unittest.main()
