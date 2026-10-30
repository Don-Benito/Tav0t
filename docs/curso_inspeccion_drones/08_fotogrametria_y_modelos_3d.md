# Módulo 8. Fotogrametría y modelos 3D

**Duración:** 5 h (2.5 h de teoría y 2.5 h de procesamiento) · **Competencia:** C8

La exactitud de un modelo fotogramétrico se mide en puntos de chequeo independientes; con buena captura se espera del orden de 1 a 3 veces el GSD.

**Objetivos de aprendizaje.**

1. Explica el flujo de la fotogrametría con dron (SfM) y sus requisitos de captura.
2. Diseña la red de puntos de control y de chequeo de una estructura.
3. Procesa un bloque de fotos y controla la calidad del resultado.
4. Usa la nube de puntos y el ortomosaico de fachada para medir y comparar.

## 8.1 De las fotos al modelo

La fotogrametría por estructura a partir del movimiento (*Structure from Motion*, SfM) reconstruye la geometría a partir de muchas fotos solapadas:

1. **Puntos homólogos:** el programa encuentra el mismo detalle en varias fotos. Requiere textura (las superficies lisas, el vidrio y el agua fallan) y solape.
2. **Ajuste de haces** (*bundle adjustment*): calcula la posición y la orientación de cada foto y la calibración de la cámara.
3. **Georreferenciación:** los puntos de control (GCP) o las posiciones RTK de las fotos dan escala, posición y orientación reales.
4. **Nube densa, malla y textura:** el modelo 3D.
5. **Productos:** ortomosaicos (también de fachada, proyectados sobre un plano vertical), modelos de superficie, secciones y mediciones.

## 8.2 Requisitos de captura

- **Solape:** 80 % frontal y 70 % lateral en fachadas (módulo 4); 75-80 % y 65-70 % en cubiertas. Cada punto de la superficie debe verse en al menos 3 fotos, mejor más.
- **Fotos convergentes y oblicuas** en esquinas, cornisas, balcones y cambios de plano. Un bloque con todas las fotos paralelas reconstruye mal la profundidad y la calibración.
- **Focal y enfoque fijos** dentro de un bloque. Las fotos de zoom de detalle se procesan aparte o no se incluyen.
- **Obturador mecánico** o fotos en estacionario, con nitidez mejor de 0.5 px.
- **Iluminación pareja:** evite mezclar fotos de sol y de sombra de la misma zona.
- **Superficies problemáticas:** vidrio, metal pulido, superficies uniformes sin textura. Se complementan con LiDAR o con mediciones topográficas.

## 8.3 Puntos de control y de chequeo

| Tipo | Para qué | Cuántos (guía del curso) |
| --- | --- | --- |
| GCP (control) | Entran al ajuste: fijan escala, posición y orientación | Mínimo 5, distribuidos en todo el objeto y a distintas alturas |
| Puntos de chequeo | No entran al ajuste: miden la exactitud real del modelo | Mínimo 3, independientes de los GCP |

- Se usan dianas en el terreno y en la cubierta, o puntos naturales bien definidos en la fachada (esquinas de ventanas, aristas) medidos con estación total sin prisma desde una base georreferenciada.
- Las coordenadas se toman con GNSS RTK o con estación total en el mismo sistema que el proyecto (SIRGAS-Chile, con su huso UTM y su época), con su tipo de altura declarado (módulo 9).
- Con fotos RTK o PPK se pueden reducir los GCP, pero nunca los puntos de chequeo: junto a fachadas la solución RTK se degrada (módulo 3).
- Si el modelo estructural se georreferenció con puntos de control, conviene que la fotogrametría use la misma red: así el modelo 3D y el modelo estructural quedan en el mismo marco.

## 8.4 Control de calidad

El informe de procesamiento debe mostrar, como mínimo:

| Indicador | Qué revisar | Criterio orientativo |
| --- | --- | --- |
| Fotos alineadas | Porcentaje de fotos que entraron al modelo | Más de 95 %; revise dónde están las que faltan |
| Error de reproyección | Coherencia interna del ajuste | Del orden de 1 px o menos |
| RMS en GCP | Ajuste a los puntos de control | Pocos GSD |
| **RMS en puntos de chequeo** | **Exactitud real** | **El indicador que se reporta** |
| GSD logrado | Resolución real del producto | El del plan |
| Cobertura | Zonas sin datos o con pocas fotos | Ninguna zona de interés sin cubrir |

Si los puntos de chequeo dan mucho más que 1 a 3 GSD, algo falla: GCP mal identificados, alturas mezcladas (h y H, módulo 9), fotos movidas o poca convergencia.

## 8.5 Productos y usos en inspección

- **Ortomosaico de fachada:** imagen única y a escala de toda la fachada. Permite mapear daños (polígonos de desprendimientos, líneas de fisuras), medir longitudes y áreas, y cuantificar para el presupuesto de reparación.
- **Nube de puntos y malla:** geometría medible para el desplome o la inclinación (ajuste de líneas a las aristas verticales y comparación con la vertical), la deformación de cubiertas y losas (perfiles y mapas de desviación respecto a un plano) y secciones para verificar dimensiones contra planos.
- **Comparación multitemporal:** dos modelos de fechas distintas, en el mismo marco de referencia (los mismos GCP), se comparan nube contra nube (por ejemplo con el método M3C2 de CloudCompare) para detectar cambios mayores que la incertidumbre. Es la base del seguimiento de daños en el tiempo.
- **Insumo para BIM y gemelo digital:** los hallazgos se ubican sobre el modelo 3D y sobre el modelo estructural (módulo 9).

## 8.6 Software

- **Comercial:** Agisoft Metashape, Pix4D, Bentley iTwin Capture (antes ContextCapture), entre otros.
- **Libre:** OpenDroneMap/WebODM y Meshroom para la reconstrucción; CloudCompare para nubes de puntos y comparaciones; QGIS para ortomosaicos y mapas.

El curso no depende de un programa: los conceptos de captura, control y calidad son los mismos.

## Práctica (2.5 h)

Con las fotos del vuelo de fachada del módulo 5 (o el conjunto del curso):

1. Alinear las fotos y revisar las que no entran.
2. Marcar los GCP en las fotos y dejar los puntos de chequeo fuera del ajuste.
3. Generar la nube densa y el ortomosaico de fachada.
4. Leer el informe de calidad y llenar la tabla 8.4.
5. Medir el área de un desprendimiento y la longitud de una fisura en el ortomosaico, y la inclinación de una arista en la nube.

## Errores frecuentes

- Reportar el RMS de los GCP como exactitud del modelo.
- Poner todos los GCP en el suelo para un edificio alto: la parte alta queda mal controlada.
- Mezclar alturas elipsoidales y ortométricas entre la fotogrametría y la topografía.
- Incluir fotos de zoom en el mismo bloque que la gran angular.
- Medir inclinaciones sobre una foto oblicua.

## Autoevaluación

1. ¿Por qué los puntos de chequeo no deben entrar al ajuste?
2. ¿Qué pasa con la exactitud de la parte alta de una fachada si todos los GCP están en el suelo?
3. Si el GSD es 1.64 mm/px, ¿qué exactitud relativa puede esperar?
4. ¿Qué condición hace válida la comparación de dos modelos de fechas distintas?

## Cómo explicar este módulo (guía del instructor)

**Idea central que el grupo debe llevarse:** el modelo 3D vale lo que dicen sus puntos de chequeo; una buena captura (solape, convergencia, nitidez) y una red de control bien distribuida dan una exactitud del orden de 1 a 3 veces el GSD.

**Preparación:**

- El programa de fotogrametría instalado en todos los computadores, con un proyecto pequeño de prueba ya procesado por si el tiempo no alcanza.
- Dos conjuntos de fotos de una misma fachada: uno solo con fotos paralelas y otro con fotos convergentes en las esquinas.
- Coordenadas de los puntos de control y de chequeo del vuelo del módulo 5, en SIRGAS-Chile, con su huso, su época y su tipo de altura.
- Un informe de procesamiento real impreso.
- CloudCompare con dos nubes de fechas distintas para mostrar la comparación M3C2.

**Secuencia del módulo (300 min):**

| Min | Bloque | Qué hace el instructor | Qué hacen los participantes |
| --- | --- | --- | --- |
| 0-15 | Apertura | Muestra el modelo 3D de una fachada y lo gira; pregunta cómo se obtiene profundidad a partir de fotos planas | Proponen explicaciones |
| 15-45 | 8.1 De las fotos al modelo | Explica la visión con dos ojos; toma tres fotos de un objeto del salón desde posiciones distintas y muestra los puntos homólogos | Hacen el ejercicio de un ojo y dos ojos |
| 45-75 | 8.2 Requisitos de captura | Procesa en vivo los dos conjuntos (paralelo y convergente) o muestra sus resultados | Comparan la nube de cada conjunto en las esquinas |
| 75-105 | 8.3 Puntos de control y de chequeo | Dibuja una fachada alta con todos los GCP en el suelo y explica el efecto de palanca | Proponen una red mejor distribuida para el caso conductor |
| 105-120 | Pausa |  |  |
| 120-135 | 8.4 Control de calidad | Recorre el informe impreso | Encuentran el RMS en GCP y el RMS en chequeo y dicen cuál se reporta |
| 135-150 | 8.5 y 8.6 Productos y software | Muestra un ortomosaico de fachada y la comparación M3C2 | Preguntan |
| 150-300 | Práctica | Asiste el procesamiento; revisa que los chequeos queden fuera del ajuste | Alinean, marcan GCP, generan nube y ortomosaico, llenan la tabla 8.4 y miden en el ortomosaico |

**Cómo explicar los puntos clave:**

- **SfM con los ojos.** Pida que extiendan un brazo con el pulgar arriba y lo miren cerrando un ojo y después el otro: el pulgar "salta" contra el fondo. Ese salto (paralaje) es lo que el programa mide entre fotos para calcular la profundidad; por eso hace falta solape y fotos desde posiciones distintas.
- **Fotos convergentes.** Con solo fotos paralelas el programa ve la fachada como con un ojo: la profundidad y la calibración quedan mal resueltas. Las fotos oblicuas en esquinas son el "segundo ojo".
- **Puntos de chequeo.** Analogía del examen: si el examen trae las mismas preguntas que la guía de estudio, la nota no dice cuánto se aprendió. Los GCP son la guía; los puntos de chequeo, el examen.
- **Distribución en altura.** Dibuje un edificio de 24 m con los GCP solo en el suelo: un error pequeño de inclinación abajo se convierte en un error mayor arriba, como una palanca. Por eso hay puntos en distintas alturas, medidos con estación total sin prisma.
- **Exactitud esperada.** Con GSD de 1.64 mm/px, el modelo debería dar del orden de 1.6 a 4.9 mm en los chequeos. Si da mucho más, el grupo debe buscar la causa antes de usar el modelo.

**Preguntas para la clase (con respuesta esperada):**

- "¿Qué RMS se informa?" El de los puntos de chequeo.
- "¿Por qué se procesan aparte las fotos con zoom?" Porque cambian la focal y la calibración dentro del bloque.
- "¿Qué se necesita para comparar dos modelos de fechas distintas?" El mismo marco (la misma red de control), exactitud conocida y cambios mayores que la incertidumbre.

**Dificultades frecuentes y cómo abordarlas:**

- Procesos lentos que consumen la práctica: trabaje con un subconjunto de fotos y tenga listo el proyecto de respaldo.
- Mezcla de alturas elipsoidales y ortométricas: pida que escriban el tipo de altura junto a cada coordenada antes de importarlas.
- Puntos de chequeo usados como control por error: revíselo en la pantalla de cada grupo antes del ajuste.

**Verificación de cierre:** cada grupo entrega la tabla 8.4 completa, el ortomosaico de fachada y una medición de área y de longitud con su incertidumbre.
