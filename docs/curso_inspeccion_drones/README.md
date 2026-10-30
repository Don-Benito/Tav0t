# Curso de inspección de edificaciones y estructuras con drones

**Proyecto:** Tav0t · **Versión del curso:** 0.1 · **Intensidad:** 40 horas (20 h de teoría y 20 h de práctica)

El curso forma equipos capaces de planear, ejecutar y documentar la inspección
visual y termográfica de edificaciones y estructuras con aeronaves no
tripuladas (UAS, drones), y de llevar los hallazgos al modelo estructural para
evaluarlos. Combina tres oficios que en una inspección real trabajan juntos:
el **piloto**, el **inspector** (que sabe leer el daño) y el **especialista en
datos** (fotogrametría y georreferenciación).

> **Qué no es este curso.** No reemplaza el certificado de idoneidad de piloto
> UAS ni la autorización de la autoridad aeronáutica. Tampoco convierte a nadie
> en evaluador estructural: el dron es un instrumento de observación, y el
> diagnóstico lo firma un profesional competente.

---

## 1. A quién va dirigido

- Ingenieros civiles y estructurales, arquitectos, tecnólogos en construcción.
- Inspectores de mantenimiento de edificaciones, puentes e infraestructura.
- Pilotos UAS que quieren especializarse en inspección.
- Topógrafos y especialistas en fotogrametría que trabajan con equipos de
  ingeniería.

**Requisitos de entrada:** nociones de sistemas estructurales (pórticos,
muros, losas) y manejo básico de computador. Para los vuelos de práctica, el
participante sin certificado de piloto actúa como inspector, operador de cámara
u observador; los vuelos los ejecuta un piloto certificado del curso.

## 2. Objetivo general

Al terminar, el participante es capaz de **planear y ejecutar con seguridad una
inspección con dron de una edificación o estructura, identificar y clasificar
los daños visibles, ubicarlos en el modelo estructural y entregar un informe
trazable** que sirva de base para la evaluación de ingeniería.

## 3. Competencias

| # | Competencia | Módulos |
|---|---|---|
| C1 | Distinguir qué puede y qué no puede observar un dron, y cuándo hace falta inspección táctil o ensayos | 1, 6 |
| C2 | Cumplir la normativa aeronáutica, de datos personales y de seguridad, y gestionar el riesgo de la operación | 2, 5 |
| C3 | Elegir el equipo y el sensor adecuados para el objetivo de la inspección | 3, 7 |
| C4 | Planear la misión: resolución (GSD), distancia, solapes, ruta, meteorología y contingencias | 4 |
| C5 | Operar cerca de estructuras: GNSS degradado, interferencia magnética, turbulencia | 5 |
| C6 | Reconocer y clasificar patologías en concreto, acero, mampostería, fachadas y cubiertas | 6 |
| C7 | Interpretar termografía y sus límites | 7 |
| C8 | Producir y controlar modelos fotogramétricos (nubes de puntos, ortomosaicos de fachada) | 8 |
| C9 | Georreferenciar los hallazgos y asignarlos a elementos del modelo estructural | 9 |
| C10 | Redactar un informe de inspección claro, trazable y con sus limitaciones | 10 |

## 4. Contenido y cronograma

| Módulo | Tema | Horas (T + P) |
|---|---|---|
| [1](01_fundamentos_inspeccion.md) | Fundamentos de la inspección de estructuras con drones | 2 (2 + 0) |
| [2](02_normativa_seguridad_y_riesgos.md) | Normativa, seguridad y gestión del riesgo | 4 (3 + 1) |
| [3](03_equipos_y_sensores.md) | Equipos y sensores | 2 (1.5 + 0.5) |
| [4](04_planificacion_de_mision.md) | Planificación de la misión | 4 (2 + 2) |
| [5](05_operacion_en_campo.md) | Operación en campo cerca de estructuras | 6 (1.5 + 4.5) |
| [6](06_patologias_y_lectura_de_danos.md) | Patologías y lectura de daños desde la imagen | 6 (4 + 2) |
| [7](07_termografia.md) | Termografía aplicada | 3 (2 + 1) |
| [8](08_fotogrametria_y_modelos_3d.md) | Fotogrametría y modelos 3D | 5 (2.5 + 2.5) |
| [9](09_georreferenciacion_e_integracion.md) | Georreferenciación de hallazgos e integración con el modelo estructural | 2 (0.5 + 1.5) |
| [10](10_informe_de_inspeccion.md) | Informe de inspección y gestión de datos | 2 (1 + 1) |
| [PF](anexos/C_evaluacion.md#3-proyecto-final) | Proyecto final integrador | 4 (0 + 4) |
| | **Total** | **40 (20 + 20)** |

Las horas de práctica incluyen vuelos, procesamiento en computador y talleres
de lectura de daños sobre imágenes reales.

### Cronograma sugerido (5 días de 8 horas)

| Día | Mañana (4 h) | Tarde (4 h) |
|---|---|---|
| 1 | M1 Fundamentos · M3 Equipos | M2 Normativa, seguridad y riesgo |
| 2 | M4 Planificación (cálculo de la misión del proyecto final) | M5 Operación: simulador, chequeos y vuelo básico |
| 3 | M5 Operación: vuelo de fachada y cubierta | M6 Patologías (taller de lectura de daños) |
| 4 | M6 Patologías (cierre) · M7 Termografía | M8 Fotogrametría: procesamiento y control de calidad |
| 5 | M9 Integración con el modelo · M10 Informe | Proyecto final: presentación y evaluación |

En modalidad de 10 sesiones de 4 horas se usa la misma secuencia, una columna
por sesión. Los vuelos se programan en la franja de mejor luz y menor viento,
aunque eso obligue a mover la teoría.

## 5. Metodología

1. **Caso conductor.** Todo el curso gira alrededor de una edificación real
   (o del edificio de ejemplo de Tav0t, `ejemplos/edificio_3p.json`, en
   modalidad virtual). Cada módulo deja un entregable que se usa en el
   siguiente: el plan de misión (M4) alimenta el vuelo (M5), las fotos alimentan
   la lectura de daños (M6) y el modelo 3D (M8), los hallazgos se ubican en el
   modelo (M9) y todo termina en el informe (M10).
2. **Aprender del error.** Cada módulo incluye una sección de *errores
   frecuentes* y el laboratorio del módulo 9 provoca un error de alturas a
   propósito para aprender a detectarlo.
3. **Seguridad primero.** Ningún vuelo de práctica se hace sin plan de misión
   aprobado, lista de chequeo firmada y área asegurada (anexo A).

## 6. Evaluación

| Componente | Peso | Cuándo |
|---|---|---|
| Autoevaluaciones por módulo | 10 % | Al cierre de cada módulo ([respuestas](anexos/C_evaluacion.md#1-respuestas-de-las-autoevaluaciones)) |
| Plan de misión del caso conductor | 20 % | Día 2 |
| Taller de clasificación de daños | 15 % | Día 3-4 |
| Examen escrito | 15 % | Día 5 ([banco de preguntas](anexos/C_evaluacion.md#2-banco-de-preguntas-del-examen)) |
| Proyecto final integrador | 40 % | Día 5 ([rúbrica](anexos/C_evaluacion.md#3-proyecto-final)) |

**Aprobación:** nota total ≥ 70 % y, sin excepción, cero faltas graves de
seguridad durante las prácticas de vuelo. Una falta grave (despegar sin lista
de chequeo, volar sobre personas no participantes, ignorar una orden de
detener la operación) reprueba el componente práctico.

## 7. Recursos

**Equipo por grupo de 4 participantes (práctica):**

- 1 dron multirrotor con cámara RGB de sensor 1" (o mayor) y obturador
  mecánico, de preferencia con zoom óptico.
- Acceso compartido a 1 cámara térmica radiométrica aerotransportada.
- 6 baterías de vuelo, cargador múltiple, bolsa ignífuga para baterías.
- Conos, cinta de demarcación, radios, chalecos, botiquín, extintor.
- 5 dianas de control (puntos de apoyo) y acceso a un GNSS RTK o estación total.
- Tarjeta comparadora de fisuras (fisurómetro) y metro.

**Software:** un programa de fotogrametría (comercial o libre, p. ej.
OpenDroneMap/WebODM), CloudCompare, QGIS, Google Earth y Python 3.10+ con
Tav0t para el laboratorio del módulo 9.

**Material del repositorio:**

| Archivo | Uso |
|---|---|
| [`ejemplos/curso_drones/calculadora_mision.py`](../../ejemplos/curso_drones/calculadora_mision.py) | GSD, distancia, huella, malla de fotos de fachada y densidad del aire (módulo 4) |
| [`ejemplos/curso_drones/hallazgos.json`](../../ejemplos/curso_drones/hallazgos.json) | Hallazgos simulados de la inspección del edificio de ejemplo (módulo 9) |
| [`ejemplos/curso_drones/ubicar_hallazgos.py`](../../ejemplos/curso_drones/ubicar_hallazgos.py) | Ubica los hallazgos en los elementos del modelo estructural (módulo 9) |
| [`docs/GUION_DE_FUNCIONAMIENTO.md`](../GUION_DE_FUNCIONAMIENTO.md) | Sistemas de coordenadas, alturas y georreferenciación (módulo 9) |

## 8. Anexos

- [A. Listas de chequeo](anexos/A_listas_de_chequeo.md): antes de salir, en
  sitio, durante y después del vuelo, y emergencias.
- [B. Formatos](anexos/B_formatos.md): plan de misión, ficha de hallazgo,
  escala de severidad y de confianza, bitácora de vuelo.
- [C. Evaluación](anexos/C_evaluacion.md): respuestas de las autoevaluaciones,
  banco de preguntas y proyecto final con rúbrica.

## 9. Mantenimiento del curso

La normativa aeronáutica y los equipos cambian más rápido que la ingeniería.
Antes de cada cohorte, el coordinador revisa la tabla *Datos que se verifican
antes de cada cohorte* del [módulo 2](02_normativa_seguridad_y_riesgos.md#25-datos-que-se-verifican-antes-de-cada-cohorte)
y actualiza este material. Como en el módulo de georreferenciación, los valores
de norma son **datos** del curso y no se dan por sentados.

## 10. Glosario breve

- **UAS / dron:** sistema de aeronave no tripulada: aeronave, estación de
  control en tierra y enlace.
- **VLOS:** operación con la aeronave dentro del alcance visual directo del
  piloto.
- **GSD (*ground sampling distance*):** tamaño en el objeto de un píxel de la
  imagen. En una fachada, mm por píxel.
- **GCP (punto de control) y punto de chequeo:** puntos con coordenadas
  conocidas. Los de control ajustan el modelo; los de chequeo, independientes,
  miden su exactitud.
- **RTK / PPK:** posicionamiento GNSS de precisión centimétrica en tiempo real
  o en posproceso.
- **RTH:** retorno automático al punto de despegue.
- **Hallazgo:** observación registrada de un daño o anomalía, con ubicación,
  evidencia y clasificación.
- **Severidad / confianza:** qué tan grave es el hallazgo / qué tan seguro
  está el inspector de lo que ve en la imagen (anexo B).
