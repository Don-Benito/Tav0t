import unittest

from tav0t.georef.modelo import modelo_desde_dict
from tav0t.georef.resultados import EscalaColores, calcular_derivas, georreferenciar_modelo, metrica_elementos
from tav0t.georef.transformacion import Georreferencia


def portico_dos_pisos(eje_vertical="Z", unidades_resultados="m"):
    """Dos columnas (x = 0 y x = 6) y dos pisos de 3 m y 4 m."""
    f = 1000.0 if unidades_resultados == "mm" else 1.0

    def coord(x, cota):
        return {"x": x, "y": 0.0, "z": cota} if eje_vertical == "Z" else {"x": x, "y": cota, "z": 0.0}

    def despl(ux):
        return [ux * f, 0.0, 0.0]
    nodos = [
        {"id": "1", **coord(0.0, 0.0)},
        {"id": "2", **coord(6.0, 0.0)},
        {"id": "3", **coord(0.0, 3.0)},
        {"id": "4", **coord(6.0, 3.0)},
        {"id": "5", **coord(0.0, 7.0)},
        {"id": "6", **coord(6.0, 7.0)},
    ]
    return modelo_desde_dict(
        {
            "unidades": "m",
            "eje_vertical": eje_vertical,
            "nodos": nodos,
            "elementos": [
                {"id": "C1", "nodos": ["1", "3"]},
                {"id": "C2", "nodos": ["2", "4"]},
                {"id": "V1", "nodos": ["3", "4"]},
                {"id": "C3", "nodos": ["3", "5"]},
                {"id": "C4", "nodos": ["4", "6"]},
                {"id": "V2", "nodos": ["5", "6"]},
            ],
            "resultados": {
                "SX": {
                    "unidades": unidades_resultados,
                    "desplazamientos": {
                        "1": despl(0.0),
                        "2": despl(0.0),
                        "3": despl(0.009),
                        "4": despl(0.012),
                        "5": despl(0.025),
                        "6": despl(0.030),
                    },
                    "elementos": {"C1": {"relacion_dc": 0.95}, "V1": {"relacion_dc": 0.5}},
                }
            },
        }
    )


class TestDerivas(unittest.TestCase):
    def test_portico(self):
        m = portico_dos_pisos()
        d = calcular_derivas(m, m.resultados["SX"])
        self.assertEqual(len(d), 2)
        self.assertAlmostEqual(d[0].altura, 3.0)
        self.assertAlmostEqual(d[0].deriva_x, 0.012 / 3.0)  # columna x=6 manda
        self.assertEqual(d[0].nodo_critico, "4")
        self.assertAlmostEqual(d[1].deriva_x, 0.018 / 4.0)
        self.assertAlmostEqual(d[1].deriva_y, 0.0)
        self.assertIsNone(d[0].cumple)

    def test_limite_y_amplificacion(self):
        m = portico_dos_pisos()
        d = calcular_derivas(m, m.resultados["SX"], factor_amplificacion=2.0, limite=0.0085)
        self.assertAlmostEqual(d[0].deriva_resultante, 0.008)
        self.assertTrue(d[0].cumple)
        self.assertAlmostEqual(d[1].deriva_resultante, 0.009)
        self.assertFalse(d[1].cumple)
        self.assertAlmostEqual(d[1].relacion_limite, 0.009 / 0.0085)

    def test_unidades_y_eje_y(self):
        m = portico_dos_pisos(eje_vertical="Y", unidades_resultados="mm")
        d = calcular_derivas(m, m.resultados["SX"])
        self.assertAlmostEqual(d[0].deriva_x, 0.004)
        self.assertAlmostEqual(d[1].deriva_x, 0.0045)

    def test_sin_resultados(self):
        m = portico_dos_pisos()
        m.resultados["SX"].desplazamientos.clear()
        self.assertEqual(calcular_derivas(m, m.resultados["SX"]), [])


class TestGeorreferenciarModelo(unittest.TestCase):
    def test_desplazamientos_y_deformada(self):
        m = portico_dos_pisos(unidades_resultados="mm")
        g = Georreferencia(4.651, -74.055, 2604.0, 90.0)  # X del modelo = Este
        nodos = {n.id: n for n in georreferenciar_modelo(m, g, m.resultados["SX"], factor_deformada=100.0)}
        n6 = nodos["6"]
        self.assertAlmostEqual(n6.desplazamiento_enu[0], 0.030, places=9)
        self.assertAlmostEqual(n6.desplazamiento_enu[1], 0.0, places=9)
        self.assertAlmostEqual(n6.acimut_desplazamiento, 90.0, places=6)
        # La deformada se desplaza 100 × 30 mm = 3 m hacia el Este.
        e, _, u = g._marco.desde_geodesicas(*n6.posicion_deformada)
        self.assertAlmostEqual(e, 6.0 + 3.0, places=5)
        self.assertAlmostEqual(u, 7.0, places=5)
        self.assertIsNone(nodos["1"].acimut_desplazamiento)  # nodo sin movimiento

    def test_ortometrica_y_zona(self):
        m = portico_dos_pisos()
        g = Georreferencia(4.651, -74.055, 2604.0, 0.0)
        nodos = georreferenciar_modelo(m, g, None, zona=17, ondulacion_geoidal=4.0)
        self.assertTrue(all(n.zona == 17 for n in nodos))
        self.assertAlmostEqual(nodos[0].altura_ortometrica, 2600.0, places=6)
        self.assertIsNone(nodos[0].desplazamiento_enu)


class TestEscalaYMetricas(unittest.TestCase):
    def test_clases(self):
        e = EscalaColores([0.6, 0.8, 1.0])
        self.assertEqual([e.clase(v) for v in (0.1, 0.6, 0.79, 0.8, 1.0, 1.5)], [0, 1, 1, 2, 3, 3])
        self.assertIsNone(e.clase(None))
        self.assertEqual(e.color(1.2), "#d62828")

    def test_validacion(self):
        with self.assertRaises(ValueError):
            EscalaColores([1.0, 0.5])
        with self.assertRaises(ValueError):
            EscalaColores([0.5], colores=("#000000",))

    def test_metricas(self):
        m = portico_dos_pisos()
        g = Georreferencia(4.651, -74.055, 2604.0, 0.0)
        nodos = georreferenciar_modelo(m, g, m.resultados["SX"])
        dc = metrica_elementos(m, nodos, m.resultados["SX"], "relacion_dc")
        self.assertEqual(dc, {"C1": 0.95, "V1": 0.5})
        despl = metrica_elementos(m, nodos, m.resultados["SX"], "desplazamiento")
        self.assertAlmostEqual(despl["V2"], 0.030, places=9)
        self.assertEqual(metrica_elementos(m, nodos, None, "relacion_dc"), {})


class TestValidacionModelo(unittest.TestCase):
    def test_errores(self):
        with self.assertRaises(ValueError):
            modelo_desde_dict({"nodos": [{"id": 1, "x": 0, "y": 0}, {"id": 1, "x": 1, "y": 0}]})
        m = modelo_desde_dict({"nodos": [{"id": 1, "x": 0, "y": 0}], "elementos": [{"id": "E", "nodos": [1, 9]}]})
        with self.assertRaises(ValueError):
            m.validar()
        m = modelo_desde_dict({"nodos": [], "elementos": []})
        with self.assertRaises(ValueError):
            m.validar()

    def test_advertencias(self):
        m = modelo_desde_dict(
            {
                "nodos": [{"id": 1, "x": 0, "y": 0}],
                "resultados": {"S": {"desplazamientos": {"1": [0, 0, 0], "99": {"ux": 1}}}},
            }
        )
        adv = m.validar()
        self.assertEqual(len(adv), 1)
        self.assertEqual(m.resultados["S"].desplazamientos["99"], (1.0, 0.0, 0.0))


if __name__ == "__main__":
    unittest.main()
