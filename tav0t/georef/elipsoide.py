"""Elipsoides de referencia.

Un elipsoide queda definido por su semieje mayor ``a`` (metros) y su
achatamiento ``f``. Todas las demás constantes se derivan de esos dos valores.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Elipsoide:
    nombre: str
    a: float
    f: float

    @property
    def b(self) -> float:
        """Semieje menor (m)."""
        return self.a * (1.0 - self.f)

    @property
    def e2(self) -> float:
        """Primera excentricidad al cuadrado."""
        return self.f * (2.0 - self.f)

    @property
    def e(self) -> float:
        """Primera excentricidad."""
        return math.sqrt(self.e2)

    @property
    def n(self) -> float:
        """Tercer achatamiento, usado por las series de Krüger (UTM)."""
        return self.f / (2.0 - self.f)

    def radio_vertical_primo(self, lat_rad: float) -> float:
        """Radio de curvatura en el primer vertical N(φ)."""
        s = math.sin(lat_rad)
        return self.a / math.sqrt(1.0 - self.e2 * s * s)


WGS84 = Elipsoide("WGS84", 6378137.0, 1.0 / 298.257223563)
# GRS80 es el elipsoide de SIRGAS, MAGNA-SIRGAS, ITRF y NAD83.
GRS80 = Elipsoide("GRS80", 6378137.0, 1.0 / 298.257222101)
# Hayford 1924: elipsoide de PSAD56 y de varios datums locales antiguos.
INTERNACIONAL_1924 = Elipsoide("INTERNACIONAL_1924", 6378388.0, 1.0 / 297.0)

ELIPSOIDES = {e.nombre: e for e in (WGS84, GRS80, INTERNACIONAL_1924)}


def obtener_elipsoide(nombre: str) -> Elipsoide:
    try:
        return ELIPSOIDES[nombre.upper()]
    except KeyError:
        disponibles = ", ".join(sorted(ELIPSOIDES))
        raise ValueError(f"Elipsoide desconocido '{nombre}'. Disponibles: {disponibles}") from None
