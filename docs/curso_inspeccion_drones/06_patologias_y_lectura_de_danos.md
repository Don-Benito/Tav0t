# Módulo 6. Patologías y lectura de daños desde la imagen

**Duración:** 6 h (4 h teoría + 2 h taller) · **Competencia:** C6

## Objetivos de aprendizaje

1. Reconoce en imágenes los daños más comunes de estructuras de concreto,
   acero y mampostería, de fachadas y de cubiertas.
2. Relaciona el patrón de un daño con sus causas posibles.
3. Mide lo que la imagen permite medir y declara lo que no.
4. Convierte cada daño en un hallazgo con severidad y confianza (anexo B).

---

## 6.1 Cómo se lee un daño

Para cada daño, el inspector responde en este orden:

1. **Qué es:** fisura, desprendimiento, mancha, corrosión, deformación,
   faltante.
2. **Dónde está:** elemento, cara, zona del elemento (apoyo, centro de la
   luz, arranque, nudo). La posición dice mucho sobre la causa.
3. **Cómo es:** orientación, ancho, longitud, extensión, patrón (aislada,
   paralelas, en malla, en X), color, presencia de óxido o eflorescencia.
4. **Desde cuándo y si avanza:** comparación con inspecciones anteriores.
5. **Por qué puede ser:** causas compatibles con el patrón. El dron sugiere;
   la causa se confirma con más información.
6. **Qué tan grave es y qué tan seguro estoy:** severidad y confianza.

> **La orientación de una fisura indica la dirección de la tracción que la
> abrió:** la fisura es perpendicular a esa tracción. Esta es la herramienta
> más útil de lectura de daños.

## 6.2 Concreto reforzado

### Fisuras estructurales en vigas

| Patrón | Dónde | Causa probable |
|---|---|---|
| Verticales, perpendiculares al eje, más anchas en la cara inferior | Centro de la luz, cara inferior | **Flexión** (momento positivo) |
| Verticales, más anchas en la cara superior | Sobre los apoyos, cara superior | **Flexión** (momento negativo); desde el dron se ven en cubiertas o desde arriba |
| Inclinadas cerca de 45°, que suben desde el apoyo hacia el centro de la luz | Cerca de los apoyos, en el alma | **Cortante** |
| Helicoidales que rodean el elemento | Vigas de borde, vigas que reciben otras de un solo lado | **Torsión** |
| Paralelas a las barras, a lo largo del elemento | Esquinas y caras inferiores, siguiendo el refuerzo | **Corrosión** del refuerzo (ver abajo) |

### Fisuras estructurales en columnas y muros

| Patrón | Causa probable |
|---|---|
| Horizontales en el arranque o bajo la viga | Flexión (sismo, empuje lateral) |
| Diagonales en una dirección, o en **X** (dos familias cruzadas) | **Cortante**; en X, cortante cíclico de un sismo |
| Verticales paralelas a la carga, con desprendimiento del recubrimiento y abombamiento | **Compresión excesiva** (aplastamiento). Señal grave |
| Daño concentrado en una columna que quedó más corta por un muro o antepecho | **Columna corta**: cortante sísmico concentrado |
| Daño en nudos viga-columna | Cortante en el nudo, anclaje deficiente |

### Fisuras no estructurales (o de origen no estructural)

| Patrón | Causa probable |
|---|---|
| Fisuras cortas, superficiales, paralelas o en malla, en losas recién vaciadas | **Retracción plástica** |
| Fisuras regularmente espaciadas que atraviesan el elemento, en muros o losas largas restringidos | **Retracción por secado** o **efectos térmicos** sin juntas suficientes |
| Malla fina en la superficie (*crazing*), sin profundidad | Acabado y curado deficientes |
| Fisuras en malla con gel o eflorescencia, a veces con expansión | Reacción álcali-agregado (requiere ensayo) |

### Corrosión del refuerzo

El concreto protege el acero mientras su recubrimiento esté sano. La
carbonatación o los cloruros (ambiente marino, sales) destruyen esa
protección; el óxido ocupa más volumen que el acero y **revienta el
recubrimiento**.

Secuencia visible desde el dron:

1. Manchas de óxido que escurren por la superficie.
2. Fisuras **paralelas a las barras**, a menudo en las esquinas.
3. Delaminación (el recubrimiento suena hueco; desde el aire se puede
   sospechar con termografía, módulo 7).
4. Desprendimiento con **acero expuesto** y pérdida de sección visible.

La pérdida de sección real no se mide desde una foto: se mide en sitio,
limpiando la barra.

### Otros daños del concreto

- **Hormigueros y segregación:** zonas porosas sin pasta, de construcción.
- **Eflorescencias:** depósitos blancos de sales arrastradas por agua; indican
  que el agua atraviesa el elemento.
- **Erosión y desgaste:** en estructuras expuestas a flujo de agua o abrasión.
- **Daño por fuego:** cambios de color, desprendimientos explosivos.
- **Impacto:** desportillamientos localizados en esquinas y bordes.

### Anchos de fisura de referencia

Para la durabilidad del concreto reforzado, el informe ACI 224R presenta
anchos de fisura considerados razonables según la exposición, como guía y no
como límite de aceptación: del orden de 0.41 mm en aire seco, 0.30 mm en aire
húmedo o suelo, 0.18 mm con químicos descongelantes, 0.15 mm con agua de mar y
ciclos de humedecimiento y secado, y 0.10 mm en estructuras que retienen agua.
Verifique la edición vigente y la norma aplicable al proyecto. Tenga presente
el módulo 4: la mayoría de estos anchos **no se miden** desde el dron con el
GSD habitual; se detectan y se miden después con fisurómetro.

## 6.3 Acero estructural

| Daño | Qué buscar en la imagen | Limitación del dron |
|---|---|---|
| **Corrosión generalizada** | Pintura perdida, óxido extendido, escamas | La pérdida de espesor requiere ultrasonido |
| **Corrosión localizada** | Picaduras, corrosión en rendijas, en uniones, bajo apoyos y donde se acumula agua | Zonas ocultas |
| **Pandeo y deformaciones** | Alas o almas onduladas, elementos curvados, diagonales flojas | Deformaciones pequeñas: comparar con la geometría (módulo 8) |
| **Uniones** | Pernos faltantes, tuercas sueltas, marcas de óxido que delatan movimiento en la unión, placas deformadas | Apriete y estado interno no se ven |
| **Soldaduras** | Grietas visibles en el cordón o en el metal adyacente, óxido en la raíz | Las grietas finas requieren ensayos no destructivos (tintas, partículas magnéticas, ultrasonido) |
| **Recubrimientos** | Ampollas, desprendimiento de pintura, galvanizado consumido | — |

En torres y estructuras de acero, revise especialmente las conexiones, los
elementos con agua estancada y las bases.

## 6.4 Mampostería

| Patrón | Causa probable |
|---|---|
| Grietas diagonales en **X** en paños de muro | Cortante sísmico en el plano |
| Grietas diagonales en una dirección, que **suben hacia la zona que desciende**, atravesando piezas y juntas | **Asentamiento diferencial** (confirmar con nivelación y seguimiento) |
| Separación en el contorno del muro con el pórtico (grieta perimetral) | Muro de relleno que trabajó contra el pórtico, o retracción en la junta |
| Grietas horizontales en la base o a media altura, con desplazamiento fuera del plano | Flexión fuera del plano (sismo, empuje) |
| Grietas verticales en encuentros de muros o en esquinas | Falta de traba entre muros, sismo |
| Grietas escalonadas por las juntas | Movimientos térmicos o de retracción, asentamiento leve |
| Piezas desprendidas, pérdida de mortero | Envejecimiento, humedad, sismo |

En Colombia es común la **mampostería de relleno** en pórticos de concreto.
Aunque no se modele, interactúa con el pórtico en un sismo: un daño en un muro
de relleno puede indicar un problema en el pórtico vecino (columna corta,
deriva alta). El laboratorio del módulo 9 tiene un caso así.

## 6.5 Fachadas

- **Enchapes cerámicos y de piedra:** piezas faltantes, fisuras, juntas
  abiertas, **abombamiento y desprendimiento** (el riesgo más serio para los
  peatones). La adherencia no se ve en la foto: la termografía sugiere zonas
  huecas y la percusión en sitio las confirma.
- **Fachadas ventiladas:** anclajes corroídos o faltantes, placas desalineadas.
- **Muros cortina y vidrio:** vidrios rotos, sellos deteriorados, perfiles
  deformados.
- **Pañetes y pinturas:** fisuras en malla (retracción), ampollas, manchas de
  humedad, moho.
- **Elementos en voladizo:** balcones, cornisas, aleros, marquesinas, avisos y
  antenas: fisuras en el arranque, corrosión de fijaciones, deformación.
  Son críticos porque caen sobre zonas de paso.
- **Juntas de dilatación y sísmicas:** sellos perdidos, tapajuntas sueltos,
  golpeteo entre edificios (desportillamientos enfrentados).

## 6.6 Cubiertas

- **Losas de cubierta:** fisuras, impermeabilización deteriorada o ausente,
  **encharcamientos** (huellas de agua estancada, vegetación), drenajes
  obstruidos.
- **Tejas:** rotas, desplazadas, faltantes; caballetes y limahoyas.
- **Cubiertas livianas metálicas:** corrosión de láminas y tornillos,
  fijaciones sueltas, deformación de correas (se ve como ondulación de la
  cubierta), canales colapsadas.
- **Elementos sobre la cubierta:** tanques, equipos, antenas y sus bases;
  sobrecargas no previstas en el diseño.

## 6.7 Daños posteriores a un evento

Después de un sismo, una inundación o un impacto, el dron permite mirar sin
exponer personas. La prioridad es la **seguridad**: elementos a punto de caer,
inclinaciones evidentes, daño en columnas de planta baja, colapso parcial,
golpeteo con edificios vecinos. La clasificación de habitabilidad (verde,
amarillo, rojo) sigue la guía oficial y la hace el evaluador competente; las
imágenes del dron son evidencia para esa decisión.

## 6.8 Medir desde la imagen

- **Ancho de fisura:** píxeles a lo ancho × GSD, en una foto frontal. Con
  incertidumbre de ±1 px. Si la fisura ocupa menos de 3 px, se reporta como
  "menor de 3 × GSD" y se pide medición en sitio.
- **Longitud y área:** en ortomosaicos de fachada o en el modelo 3D (módulo 8),
  que tienen escala real. En fotos sueltas, con una referencia de tamaño
  conocido en el mismo plano.
- **Inclinación o desplome:** en el modelo 3D, no en una foto (la perspectiva
  engaña).
- Siempre se informa **con qué se midió** (foto, ortomosaico, nube de puntos)
  y **la incertidumbre**.

## 6.9 Severidad y confianza

Cada hallazgo recibe dos calificaciones (escala completa en el
[anexo B](anexos/B_formatos.md#3-escala-de-severidad-y-de-confianza)):

- **Severidad (0 a 4):** de "sin daño" a "crítico, acción inmediata".
- **Confianza (A, B, C):** A = el daño se ve con detalle suficiente; B =
  probable, hay que verificar de cerca; C = indicio, requiere ensayo.

Un hallazgo puede ser severidad 3 con confianza B: probable daño serio que se
debe verificar pronto. Esa combinación es la que más vale reportar bien.

La severidad sube cuando:

- El elemento es crítico para la estabilidad (columnas de planta baja,
  elementos de transferencia, voladizos sobre zonas de paso).
- El modelo estructural indica una relación demanda/capacidad alta o una
  deriva alta en ese elemento o piso (módulo 9).
- El daño avanza respecto a la inspección anterior.
- Hay riesgo de caída de objetos sobre personas.

---

## Taller (2 h)

Cada grupo recibe 30 imágenes (del vuelo del módulo 5 o del banco del curso)
y para cada una:

1. Identifica el daño, el elemento y la zona del elemento.
2. Propone la causa probable y la justifica con el patrón.
3. Mide lo que se puede medir y declara la incertidumbre.
4. Asigna severidad y confianza, y dice qué verificación pide.

Se comparan las clasificaciones entre grupos: las diferencias se discuten. El
taller vale el 15 % de la nota.

## Errores frecuentes

- Diagnosticar la causa con una sola foto y sin conocer la estructura.
- Confundir fisuras de retracción con fisuras estructurales (o al revés).
- Reportar anchos de fisura menores que el GSD como si fueran medidos.
- No relacionar el daño del muro de relleno con el pórtico.
- Calificar severidad sin considerar quién pasa debajo.

## Autoevaluación

1. Una viga muestra fisuras inclinadas a 45° cerca de los apoyos. ¿Qué
   esfuerzo las produjo?
2. ¿Qué secuencia de signos visibles indica corrosión del refuerzo?
3. En un muro de mampostería aparecen grietas en X. ¿Qué indican?
4. Con GSD de 1.64 mm/px, una fisura ocupa 2 px. ¿Cómo la reporta?
5. ¿Por qué un enchape abombado en el piso 6 sobre un andén sube de severidad?

Respuestas en el [anexo C](anexos/C_evaluacion.md#1-respuestas-de-las-autoevaluaciones).
