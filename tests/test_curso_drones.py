import importlib.util
import sys
import unittest
from pathlib import Path

CURSO = Path(__file__).resolve().parent.parent / "ejemplos" / "curso_drones"


def _cargar(nombre: str):
    spec = importlib.util.spec_from_file_location(nombre, CURSO / f"{nombre}.py")
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = modulo  # dataclasses lo necesita
    spec.loader.exec_module(modulo)
    return modulo


calc = _cargar("calculadora_mision")
lab = _cargar("ubicar_hallazgos")


class TestCalculadoraMision(unittest.TestCase):
    """Los valores son los de los ejemplos resueltos del módulo 4 del curso."""

    def test_gsd_y_distancia(self):
        camara = calc.CAMARAS["gran_angular"]
        self.assertAlmostEqual(calc.gsd_mm(camara, 6.0), 1.645, places=3)
        self.assertAlmostEqual(calc.gsd_mm(calc.CAMARAS["zoom"], 10.0), 0.40, places=3)
        self.assertAlmostEqual(calc.gsd_mm(calc.CAMARAS["termica"], 10.0), 9.23, places=2)
        self.assertAlmostEqual(calc.distancia_para_gsd(camara, calc.gsd_mm(camara, 7.3)), 7.3)
        ancho, alto = calc.huella_m(camara, 6.0)
        self.assertAlmostEqual(ancho, 9.0)
        self.assertAlmostEqual(alto, 6.0)

    def test_plan_fachada(self):
        plan = calc.plan_fachada(calc.CAMARAS["gran_angular"], 30.0, 24.0, 6.0, 0.8, 0.7)
        self.assertAlmostEqual(plan["paso_fotos_m"], 1.8)
        self.assertAlmostEqual(plan["paso_pasadas_m"], 1.8)
        self.assertEqual((plan["pasadas"], plan["fotos_por_pasada"], plan["fotos"]), (15, 18, 270))
        with self.assertRaises(ValueError):
            calc.plan_fachada(calc.CAMARAS["zoom"], 30.0, 24.0, 6.0, 1.0, 0.7)

    def test_densidad_aire(self):
        self.assertAlmostEqual(calc.densidad_aire(0.0), 1.225)
        self.assertAlmostEqual(calc.densidad_aire(3000.0), 0.909, places=3)


class TestUbicarHallazgos(unittest.TestCase):
    PROYECTO = CURSO / "proyecto_santiago.json"
    HALLAZGOS = CURSO / "hallazgos.json"

    def test_distancias(self):
        self.assertAlmostEqual(lab.distancia_segmento((1, 1, 0), (0, 0, 0), (2, 0, 0)), 1.0)
        self.assertAlmostEqual(lab.distancia_segmento((3, 0, 0), (0, 0, 0), (2, 0, 0)), 1.0)
        cuadro = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        self.assertAlmostEqual(lab.distancia_poligono((0.5, 0.5, 0.2), cuadro), 0.2)
        self.assertAlmostEqual(lab.distancia_poligono((0.5, 0.5, -0.2), cuadro[::-1]), 0.2)
        self.assertAlmostEqual(lab.distancia_poligono((2, 0.5, 0), cuadro), 1.0)

    def test_cada_hallazgo_cae_en_su_elemento(self):
        ubicados = {u["id"]: u for u in lab.ubicar(self.PROYECTO, self.HALLAZGOS)}
        esperado = {"H01": "C1-02", "H02": "VX2-00", "H03": "VY3-02", "H04": "L3-01", "H05": None, "H06": "C1-20"}
        self.assertEqual({k: u["elemento"] for k, u in ubicados.items()}, esperado)
        self.assertGreater(ubicados["H05"]["distancia_m"], lab.TOLERANCIA_M)  # muro de albañilería, no modelado

    def test_sin_ondulacion_los_hallazgos_bajan_n_metros(self):
        bien = lab.ubicar(self.PROYECTO, self.HALLAZGOS)
        mal = lab.ubicar(self.PROYECTO, self.HALLAZGOS, ondulacion=0.0)
        for b, m in zip(bien, mal):
            self.assertAlmostEqual(b["modelo"][2] - m["modelo"][2], 30.0, delta=0.01)
            self.assertIsNone(m["elemento"])


if __name__ == "__main__":
    unittest.main()
