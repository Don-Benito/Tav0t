"""Proyección Universal Transversa de Mercator (UTM).

Implementa las series de Krüger hasta orden n⁶ según C. F. F. Karney (2011),
"Transverse Mercator with an accuracy of a few nanometers", J. Geodesy 85(8).
Dentro de una zona UTM (±3° del meridiano central) el error es inferior a
1 mm, muy por debajo de lo que exige cualquier proyecto estructural.

Además de las coordenadas, las funciones devuelven:

* ``convergencia``: convergencia de meridianos γ en grados, medida en sentido
  horario desde el norte verdadero hasta el norte de cuadrícula.
  Acimut verdadero = acimut de cuadrícula + γ.
* ``escala``: factor de escala puntual k. Una distancia medida sobre el
  elipsoide se convierte en distancia de cuadrícula multiplicándola por k.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .elipsoide import WGS84, Elipsoide

K0 = 0.9996
FALSO_ESTE = 500000.0
FALSO_NORTE_SUR = 10000000.0


@dataclass(frozen=True)
class CoordenadaUTM:
    este: float
    norte: float
    zona: int
    hemisferio: str  # "N" o "S"
    convergencia: float = 0.0
    escala: float = K0


def zona_utm(lat: float, lon: float) -> int:
    """Zona UTM estándar, incluidas las excepciones de Noruega y Svalbard."""
    lon = ((lon + 180.0) % 360.0) - 180.0
    zona = min(int((lon + 180.0) // 6.0) + 1, 60)
    if 56.0 <= lat < 64.0 and 3.0 <= lon < 12.0:
        zona = 32
    if 72.0 <= lat < 84.0 and lon >= 0.0:
        if lon < 9.0:
            zona = 31
        elif lon < 21.0:
            zona = 33
        elif lon < 33.0:
            zona = 35
        elif lon < 42.0:
            zona = 37
    return zona


def meridiano_central(zona: int) -> float:
    if not 1 <= zona <= 60:
        raise ValueError(f"Zona UTM fuera de rango: {zona}")
    return (zona - 1) * 6.0 - 180.0 + 3.0


def _coeficientes(n: float) -> tuple[float, list[float], list[float]]:
    n2, n3, n4, n5, n6 = n**2, n**3, n**4, n**5, n**6
    a_rect = 1.0 + n2 / 4.0 + n4 / 64.0 + n6 / 256.0
    alfa = [
        0.0,
        n / 2 - 2 / 3 * n2 + 5 / 16 * n3 + 41 / 180 * n4 - 127 / 288 * n5 + 7891 / 37800 * n6,
        13 / 48 * n2 - 3 / 5 * n3 + 557 / 1440 * n4 + 281 / 630 * n5 - 1983433 / 1935360 * n6,
        61 / 240 * n3 - 103 / 140 * n4 + 15061 / 26880 * n5 + 167603 / 181440 * n6,
        49561 / 161280 * n4 - 179 / 168 * n5 + 6601661 / 7257600 * n6,
        34729 / 80640 * n5 - 3418889 / 1995840 * n6,
        212378941 / 319334400 * n6,
    ]
    beta = [
        0.0,
        n / 2 - 2 / 3 * n2 + 37 / 96 * n3 - 1 / 360 * n4 - 81 / 512 * n5 + 96199 / 604800 * n6,
        1 / 48 * n2 + 1 / 15 * n3 - 437 / 1440 * n4 + 46 / 105 * n5 - 1118711 / 3870720 * n6,
        17 / 480 * n3 - 37 / 840 * n4 - 209 / 4480 * n5 + 5569 / 90720 * n6,
        4397 / 161280 * n4 - 11 / 504 * n5 - 830251 / 7257600 * n6,
        4583 / 161280 * n5 - 108847 / 3991680 * n6,
        20648693 / 638668800 * n6,
    ]
    return a_rect, alfa, beta


def geodesicas_a_utm(
    lat: float,
    lon: float,
    zona: int | None = None,
    elipsoide: Elipsoide = WGS84,
) -> CoordenadaUTM:
    """Proyecta (lat, lon) a UTM.

    ``zona`` permite forzar una zona distinta de la natural (por ejemplo, para
    que todo un proyecto que cruza el borde de zona quede en la misma).
    """
    if not -80.0 <= lat <= 84.0:
        raise ValueError(f"Latitud {lat} fuera del dominio UTM (−80° a 84°); use UPS.")
    if zona is None:
        zona = zona_utm(lat, lon)
    lon0 = meridiano_central(zona)
    dlon = ((lon - lon0 + 180.0) % 360.0) - 180.0
    if abs(dlon) > 30.0:
        raise ValueError(f"Longitud {lon} demasiado lejos del meridiano central de la zona {zona}.")

    a, e = elipsoide.a, elipsoide.e
    a_rect, alfa, _ = _coeficientes(elipsoide.n)
    a_mayus = a / (1.0 + elipsoide.n) * a_rect

    phi = math.radians(lat)
    lam = math.radians(dlon)
    cos_l, sin_l, tan_l = math.cos(lam), math.sin(lam), math.tan(lam)

    tau = math.tan(phi)
    sigma = math.sinh(e * math.atanh(e * tau / math.sqrt(1.0 + tau * tau)))
    tau_p = tau * math.sqrt(1.0 + sigma * sigma) - sigma * math.sqrt(1.0 + tau * tau)

    xi_p = math.atan2(tau_p, cos_l)
    eta_p = math.asinh(sin_l / math.sqrt(tau_p * tau_p + cos_l * cos_l))

    xi, eta = xi_p, eta_p
    p_p, q_p = 1.0, 0.0
    for j in range(1, 7):
        s2, c2 = math.sin(2 * j * xi_p), math.cos(2 * j * xi_p)
        sh2, ch2 = math.sinh(2 * j * eta_p), math.cosh(2 * j * eta_p)
        xi += alfa[j] * s2 * ch2
        eta += alfa[j] * c2 * sh2
        p_p += 2 * j * alfa[j] * c2 * ch2
        q_p += 2 * j * alfa[j] * s2 * sh2

    este = K0 * a_mayus * eta + FALSO_ESTE
    norte = K0 * a_mayus * xi
    hemisferio = "N" if lat >= 0 else "S"
    if hemisferio == "S":
        norte += FALSO_NORTE_SUR

    gamma = math.atan(tau_p / math.sqrt(1.0 + tau_p * tau_p) * tan_l) + math.atan2(q_p, p_p)
    sin_phi = math.sin(phi)
    k = (
        K0
        * math.sqrt(1.0 - elipsoide.e2 * sin_phi * sin_phi)
        * math.sqrt(1.0 + tau * tau)
        / math.sqrt(tau_p * tau_p + cos_l * cos_l)
        * (a_mayus / a)
        * math.sqrt(p_p * p_p + q_p * q_p)
    )
    return CoordenadaUTM(este, norte, zona, hemisferio, math.degrees(gamma), k)


def utm_a_geodesicas(
    este: float,
    norte: float,
    zona: int,
    hemisferio: str,
    elipsoide: Elipsoide = WGS84,
) -> tuple[float, float, float, float]:
    """Inversa de UTM. Devuelve (lat, lon, convergencia, escala)."""
    hemisferio = hemisferio.upper()
    if hemisferio not in ("N", "S"):
        raise ValueError("hemisferio debe ser 'N' o 'S'")
    a, e, e2 = elipsoide.a, elipsoide.e, elipsoide.e2
    a_rect, _, beta = _coeficientes(elipsoide.n)
    a_mayus = a / (1.0 + elipsoide.n) * a_rect

    x = este - FALSO_ESTE
    y = norte - (FALSO_NORTE_SUR if hemisferio == "S" else 0.0)
    eta = x / (K0 * a_mayus)
    xi = y / (K0 * a_mayus)

    xi_p, eta_p = xi, eta
    p, q = 1.0, 0.0
    for j in range(1, 7):
        s2, c2 = math.sin(2 * j * xi), math.cos(2 * j * xi)
        sh2, ch2 = math.sinh(2 * j * eta), math.cosh(2 * j * eta)
        xi_p -= beta[j] * s2 * ch2
        eta_p -= beta[j] * c2 * sh2
        p -= 2 * j * beta[j] * c2 * ch2
        q += 2 * j * beta[j] * s2 * sh2

    sinh_eta_p = math.sinh(eta_p)
    sin_xi_p, cos_xi_p = math.sin(xi_p), math.cos(xi_p)
    tau_p = sin_xi_p / math.sqrt(sinh_eta_p * sinh_eta_p + cos_xi_p * cos_xi_p)

    # Newton-Raphson para recuperar τ = tan φ a partir de τ' (esfera conforme).
    tau = tau_p
    for _ in range(20):
        sigma = math.sinh(e * math.atanh(e * tau / math.sqrt(1.0 + tau * tau)))
        tau_i = tau * math.sqrt(1.0 + sigma * sigma) - sigma * math.sqrt(1.0 + tau * tau)
        delta = (
            (tau_p - tau_i)
            / math.sqrt(1.0 + tau_i * tau_i)
            * (1.0 + (1.0 - e2) * tau * tau)
            / ((1.0 - e2) * math.sqrt(1.0 + tau * tau))
        )
        tau += delta
        if abs(delta) < 1e-14:
            break

    phi = math.atan(tau)
    lam = math.atan2(sinh_eta_p, cos_xi_p)

    gamma = math.atan(math.tan(xi_p) * math.tanh(eta_p)) + math.atan2(q, p)
    sin_phi = math.sin(phi)
    k = (
        K0
        * math.sqrt(1.0 - e2 * sin_phi * sin_phi)
        * math.sqrt(1.0 + tau * tau)
        * math.sqrt(sinh_eta_p * sinh_eta_p + cos_xi_p * cos_xi_p)
        * (a_mayus / a)
        / math.sqrt(p * p + q * q)
    )
    lon = math.degrees(lam) + meridiano_central(zona)
    lon = ((lon + 180.0) % 360.0) - 180.0
    return math.degrees(phi), lon, math.degrees(gamma), k
