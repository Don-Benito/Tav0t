# Tav0t

Plataforma de análisis estructural.

## Módulo de georreferenciación (`tav0t.georef`)

Coloca un modelo estructural (nodos, elementos y resultados en coordenadas
locales X, Y, Z) en la Tierra y genera mapas y reportes:

- Georreferenciación **paramétrica** (punto de amarre + acimut) o **por puntos
  de control** (ajuste por mínimos cuadrados con residuos).
- Conversión modelo ⇄ ENU ⇄ ECEF ⇄ latitud/longitud ⇄ UTM, cambio de datum
  (Helmert 7 parámetros), alturas ortométricas/elipsoidales, norte verdadero o
  de cuadrícula.
- Desplazamientos en direcciones reales, deformada, **derivas de entrepiso**
  con verificación del límite y colores por relación D/C o desplazamiento.
- Consulta de **zonificación** (sísmica, suelos…) por ubicación.
- Exporta **GeoJSON** (QGIS/ArcGIS/web), **KML** (Google Earth 3D), **CSV** y un
  **informe JSON** con controles de calidad.

**Motor propio:** Python 3.10+ puro, sin dependencias. La precisión se verificó
contra PROJ y la diferencia es menor que 10⁻⁸ m.

**Documento principal:** [docs/GUION_DE_FUNCIONAMIENTO.md](docs/GUION_DE_FUNCIONAMIENTO.md).
Explica qué hace el módulo, cómo funciona y cómo está implementado al detalle.

### Uso rápido

```bash
python -m tav0t.georef ejecutar ejemplos/proyecto_parametrico.json
```

```bash
python -m tav0t.georef ejecutar ejemplos/proyecto_puntos_control.json
```

```bash
python -m tav0t.georef utm 4.651 -74.055
```

Desde Python:

```python
from tav0t.georef import ejecutar_proyecto

informe = ejecutar_proyecto("ejemplos/proyecto_parametrico.json")
print(informe["cuadricula_utm"], informe["derivas"])
```

Los resultados quedan en `ejemplos/salida/`. Abra el `.kml` en Google Earth o el
`.geojson` en QGIS.

### Pruebas

```bash
python -m unittest discover -s tests -t .
```

### Estructura

```
tav0t/georef/      motor de georreferenciación
docs/              guion de funcionamiento (especificación)
ejemplos/          edificio de 3 pisos, proyectos de ejemplo y zonificación ficticia
tests/             pruebas automáticas
```
