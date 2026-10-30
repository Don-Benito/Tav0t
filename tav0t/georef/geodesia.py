"""Conversiones geodésicas fundamentales.

Sistemas que maneja este módulo:

* Geodésicas: latitud φ y longitud λ en grados, altura elipsoidal h en metros.
* ECEF: cartesianas geocéntricas X, Y, Z en metros (origen en el centro de masa
  de la Tierra, eje Z hacia el polo norte, eje X hacia el meridiano de Greenwich).
* ENU: plano tangente local Este, Norte, Arriba (en metros) con origen en un
  punto de referencia. Es el sistema intermedio en el que se coloca el modelo
  estructural, porque no tiene distorsión de escala y su norte es el verdadero.
"""

from __future__ import annotations

import math
from typing import Sequence

from .elipsoide import WGS84, Elipsoide

Vector3 = tuple[float, float, float]


def geodesicas_a_ecef(lat: float, lon: float, h: float, elipsoide: Elipsoide = WGS84) -> Vector3:
    phi = math.radians(lat)
    lam = math.radians(lon)
    n = elipsoide.radio_vertical_primo(phi)
    cos_phi = math.cos(phi)
    x = (n + h) * cos_phi * math.cos(lam)
    y = (n + h) * cos_phi * math.sin(lam)
    z = (n * (1.0 - elipsoide.e2) + h) * math.sin(phi)
    return x, y, z


def ecef_a_geodesicas(x: float, y: float, z: float, elipsoide: Elipsoide = WGS84) -> Vector3:
    """Inversa iterativa. Converge a < 1e-12 rad en 2-4 iteraciones.

    La altura se calcula con ``h = p·cosφ + z·sinφ − a·sqrt(1 − e²·sin²φ)``,
    que es estable también cerca de los polos (no divide entre cosφ).
    """
    a, e2 = elipsoide.a, elipsoide.e2
    lam = math.atan2(y, x)
    p = math.hypot(x, y)
    phi = math.atan2(z, p * (1.0 - e2))
    h = 0.0
    for _ in range(10):
        s = math.sin(phi)
        n = a / math.sqrt(1.0 - e2 * s * s)
        h = p * math.cos(phi) + z * s - a * math.sqrt(1.0 - e2 * s * s)
        phi_nuevo = math.atan2(z, p * (1.0 - e2 * n / (n + h)))
        if abs(phi_nuevo - phi) < 1e-14:
            phi = phi_nuevo
            break
        phi = phi_nuevo
    s = math.sin(phi)
    h = p * math.cos(phi) + z * s - a * math.sqrt(1.0 - e2 * s * s)
    return math.degrees(phi), math.degrees(lam), h


def _matriz_ecef_a_enu(lat0: float, lon0: float) -> tuple[Vector3, Vector3, Vector3]:
    phi = math.radians(lat0)
    lam = math.radians(lon0)
    sp, cp = math.sin(phi), math.cos(phi)
    sl, cl = math.sin(lam), math.cos(lam)
    return (
        (-sl, cl, 0.0),
        (-sp * cl, -sp * sl, cp),
        (cp * cl, cp * sl, sp),
    )


class MarcoENU:
    """Plano tangente local con origen fijo. Precalcula la matriz de rotación."""

    def __init__(self, lat0: float, lon0: float, h0: float, elipsoide: Elipsoide = WGS84):
        self.lat0 = lat0
        self.lon0 = lon0
        self.h0 = h0
        self.elipsoide = elipsoide
        self.origen_ecef = geodesicas_a_ecef(lat0, lon0, h0, elipsoide)
        self._r = _matriz_ecef_a_enu(lat0, lon0)

    def desde_ecef(self, x: float, y: float, z: float) -> Vector3:
        dx = x - self.origen_ecef[0]
        dy = y - self.origen_ecef[1]
        dz = z - self.origen_ecef[2]
        r = self._r
        return (
            r[0][0] * dx + r[0][1] * dy + r[0][2] * dz,
            r[1][0] * dx + r[1][1] * dy + r[1][2] * dz,
            r[2][0] * dx + r[2][1] * dy + r[2][2] * dz,
        )

    def a_ecef(self, e: float, n: float, u: float) -> Vector3:
        r = self._r
        # La matriz es ortogonal: la inversa es la transpuesta.
        return (
            self.origen_ecef[0] + r[0][0] * e + r[1][0] * n + r[2][0] * u,
            self.origen_ecef[1] + r[0][1] * e + r[1][1] * n + r[2][1] * u,
            self.origen_ecef[2] + r[0][2] * e + r[1][2] * n + r[2][2] * u,
        )

    def desde_geodesicas(self, lat: float, lon: float, h: float) -> Vector3:
        return self.desde_ecef(*geodesicas_a_ecef(lat, lon, h, self.elipsoide))

    def a_geodesicas(self, e: float, n: float, u: float) -> Vector3:
        return ecef_a_geodesicas(*self.a_ecef(e, n, u), self.elipsoide)


# --- Transformación de datum (Helmert de 7 parámetros) -----------------------

ARCSEG_A_RAD = math.pi / (180.0 * 3600.0)


def helmert_7p(
    punto_ecef: Sequence[float],
    tx: float,
    ty: float,
    tz: float,
    rx_seg: float,
    ry_seg: float,
    rz_seg: float,
    s_ppm: float,
    convencion: str = "vector_posicion",
    inversa: bool = False,
) -> Vector3:
    """Transforma un punto ECEF entre dos datums.

    Traslaciones en metros, rotaciones en segundos de arco, escala en ppm.

    ``convencion``:
      * ``"vector_posicion"`` (EPSG 9606, la de la norma ISO 19111 y de IERS).
      * ``"marco_coordenadas"`` (EPSG 9607): mismas fórmulas con las rotaciones
        de signo contrario. Revise siempre qué convención publica la fuente
        oficial de los parámetros: usar la equivocada produce errores de metros.

    ``inversa=True`` aplica la transformación inversa exacta (no solo cambia
    el signo de los parámetros), resolviendo el sistema lineal 3x3.
    """
    signo = 1.0 if convencion == "vector_posicion" else -1.0
    if convencion not in ("vector_posicion", "marco_coordenadas"):
        raise ValueError("convencion debe ser 'vector_posicion' o 'marco_coordenadas'")
    rx = signo * rx_seg * ARCSEG_A_RAD
    ry = signo * ry_seg * ARCSEG_A_RAD
    rz = signo * rz_seg * ARCSEG_A_RAD
    m = 1.0 + s_ppm * 1e-6
    matriz = (
        (m, -m * rz, m * ry),
        (m * rz, m, -m * rx),
        (-m * ry, m * rx, m),
    )
    x, y, z = punto_ecef
    if not inversa:
        return (
            tx + matriz[0][0] * x + matriz[0][1] * y + matriz[0][2] * z,
            ty + matriz[1][0] * x + matriz[1][1] * y + matriz[1][2] * z,
            tz + matriz[2][0] * x + matriz[2][1] * y + matriz[2][2] * z,
        )
    return _resolver_3x3(matriz, (x - tx, y - ty, z - tz))


def _resolver_3x3(m: Sequence[Sequence[float]], b: Sequence[float]) -> Vector3:
    """Regla de Cramer para un sistema 3x3 bien condicionado."""

    def det(a: Sequence[Sequence[float]]) -> float:
        return (
            a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
        )

    d = det(m)
    sol = []
    for col in range(3):
        mc = [list(fila) for fila in m]
        for fila in range(3):
            mc[fila][col] = b[fila]
        sol.append(det(mc) / d)
    return sol[0], sol[1], sol[2]
