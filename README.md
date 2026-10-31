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

## Curso de inspección de edificaciones y estructuras con drones

Curso de 40 horas, en 9 módulos, para planear, ejecutar y documentar
inspecciones con dron y llevar los hallazgos al modelo estructural, con
normativa chilena (DAN 151 de la DGAC, normas NCh, SIRGAS-Chile):
[docs/curso_inspeccion_drones/](docs/curso_inspeccion_drones/README.md).

Incluye una calculadora de misión (GSD, distancia, malla de fotos de fachada) y
un laboratorio que ubica los hallazgos de la inspección de un edificio en
Santiago (UTM 19S, límite de deriva de la NCh 433) en los elementos del modelo
con este módulo de georreferenciación:

```bash
python ejemplos/curso_drones/calculadora_mision.py fachada --camara gran_angular --ancho 30 --alto 24 --distancia 6
```

```bash
python ejemplos/curso_drones/ubicar_hallazgos.py
```

## Estructura del repositorio

```
tav0t/georef/                  motor de georreferenciación
docs/                          guion de funcionamiento (especificación)
docs/curso_inspeccion_drones/  curso de inspección con drones
ejemplos/                      edificio de 3 pisos, proyectos de ejemplo y zonificación ficticia
ejemplos/curso_drones/         calculadora de misión y laboratorio del curso
tests/                         pruebas automáticas
```
