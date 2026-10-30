# Módulo 6. Patologías y lectura de daños desde la imagen

**Duración:** 6 h (4 h de teoría y 2 h de taller) · **Competencia:** C6

La orientación de una fisura indica la dirección de la tracción que la abrió: la fisura es perpendicular a esa tracción, y es la herramienta más útil para leer un daño.

**Objetivos de aprendizaje.**

1. Reconoce en imágenes los daños más comunes de estructuras de hormigón armado, acero y albañilería, de fachadas y de techumbres.
2. Relaciona el patrón de un daño con sus causas posibles.
3. Mide lo que la imagen permite medir y declara lo que no.
4. Convierte cada daño en un hallazgo con severidad y confianza (anexo B).

## 6.1 Cómo se lee un daño

Para cada daño, el inspector responde en este orden:

1. **Qué es:** fisura, desprendimiento, mancha, corrosión, deformación, faltante.
2. **Dónde está:** elemento, cara y zona del elemento (apoyo, centro de la luz, arranque, nudo, borde de muro). La posición dice mucho sobre la causa.
3. **Cómo es:** orientación, ancho, longitud, extensión, patrón (aislada, paralelas, en malla, en X), color, presencia de óxido o eflorescencia.
4. **Desde cuándo y si avanza:** comparación con inspecciones anteriores.
5. **Por qué puede ser:** causas compatibles con el patrón. El dron sugiere; la causa se confirma con más información.
6. **Qué tan grave es y qué tan seguro estoy:** severidad y confianza.

## 6.2 Hormigón armado

**Fisuras estructurales en vigas:**

| Patrón | Dónde | Causa probable |
| --- | --- | --- |
| Verticales, perpendiculares al eje, más anchas en la cara inferior | Centro de la luz, cara inferior | Flexión (momento positivo) |
| Verticales, más anchas en la cara superior | Sobre los apoyos, cara superior | Flexión (momento negativo); desde el dron se ven en techumbres o desde arriba |
| Inclinadas cerca de 45°, que suben desde el apoyo hacia el centro de la luz | Cerca de los apoyos, en el alma | Corte |
| Helicoidales que rodean el elemento | Vigas de borde, vigas que reciben otras de un solo lado | Torsión |
| Paralelas a las barras, a lo largo del elemento | Esquinas y caras inferiores, siguiendo la armadura | Corrosión de la armadura |

**Fisuras y daños estructurales en pilares y muros:**

| Patrón | Causa probable |
| --- | --- |
| Horizontales en el arranque o bajo la viga | Flexión (sismo, empuje lateral) |
| Diagonales en una dirección, o en X (dos familias cruzadas) | Corte; en X, corte cíclico de un sismo |
| Verticales paralelas a la carga, con desprendimiento del recubrimiento y abombamiento | Compresión excesiva (aplastamiento): señal grave |
| Aplastamiento del borde de muros de hormigón en los pisos inferiores, con pandeo de las barras verticales | Flexocompresión en muros esbeltos; fue un daño característico en edificios de muros durante el terremoto del Maule de 2010 |
| Daño concentrado en un pilar que quedó más corto por un muro o antepecho | Pilar corto: corte sísmico concentrado |
| Daño en nudos viga-pilar o en dinteles entre muros | Corte en el nudo o en el dintel, anclaje deficiente |

En Chile predominan los edificios de muros de hormigón armado: en ellos se mira con prioridad la base de los muros, los bordes, los dinteles y las discontinuidades de muros entre pisos.

**Fisuras de origen no estructural:**

| Patrón | Causa probable |
| --- | --- |
| Fisuras cortas, superficiales, paralelas o en malla, en losas recién hormigonadas | Retracción plástica |
| Fisuras regularmente espaciadas que atraviesan el elemento, en muros o losas largas restringidos | Retracción por secado o efectos térmicos sin juntas suficientes |
| Malla fina en la superficie, sin profundidad | Terminación y curado deficientes |
| Fisuras en malla con gel o eflorescencia, a veces con expansión | Reacción álcali-árido (requiere ensayo) |

**Corrosión de la armadura.** El hormigón protege el acero mientras su recubrimiento esté sano. La carbonatación o los cloruros (borde costero, sales) destruyen esa protección; el óxido ocupa más volumen que el acero y revienta el recubrimiento. En la costa chilena es un daño frecuente. La secuencia visible desde el dron es:

1. Manchas de óxido que escurren por la superficie.
2. Fisuras paralelas a las barras, a menudo en las esquinas.
3. Delaminación: el recubrimiento suena hueco; desde el aire se puede sospechar con termografía (módulo 7).
4. Desprendimiento con armadura expuesta y pérdida de sección visible.

La pérdida de sección real no se mide desde una foto: se mide en sitio, limpiando la barra.

**Otros daños del hormigón:**

- **Nidos de piedra y segregación:** zonas porosas sin pasta, de origen constructivo.
- **Eflorescencias:** depósitos blancos de sales arrastradas por agua; indican que el agua atraviesa el elemento.
- **Erosión y desgaste:** en estructuras expuestas a flujo de agua, oleaje o abrasión.
- **Daño por fuego:** cambios de color, desprendimientos explosivos.
- **Impacto:** desconches localizados en esquinas y bordes.

**Anchos de fisura de referencia.** La normativa chilena (NCh 430 y DS 60) no fija anchos de fisura admisibles para evaluar estructuras existentes. Como la NCh 430 adopta el ACI 318, el curso usa como referencia técnica los anchos del informe ACI 224R, que son una guía de durabilidad y no un límite de aceptación:

| Exposición | Ancho de referencia (mm) |
| --- | --: |
| Aire seco o membrana protectora | 0.41 |
| Humedad, aire húmedo, suelo | 0.30 |
| Químicos descongelantes | 0.18 |
| Agua de mar, ciclos de humedecimiento y secado | 0.15 |
| Estructuras que retienen agua | 0.10 |

La mayoría de estos anchos no se miden desde el dron con el GSD habitual (módulo 4): se detectan y se miden después con fisurómetro.

## 6.3 Acero estructural

| Daño | Qué buscar en la imagen | Limitación del dron |
| --- | --- | --- |
| Corrosión generalizada | Pintura perdida, óxido extendido, escamas | La pérdida de espesor requiere ultrasonido |
| Corrosión localizada | Picaduras, corrosión en rendijas, en uniones, bajo apoyos y donde se acumula agua | Zonas ocultas |
| Pandeo y deformaciones | Alas o almas onduladas, elementos curvados, diagonales flojas | Deformaciones pequeñas: comparar con la geometría (módulo 8) |
| Uniones | Pernos faltantes, tuercas sueltas, marcas de óxido que delatan movimiento, placas deformadas | El apriete y el estado interno no se ven |
| Soldaduras | Grietas visibles en el cordón o en el metal adyacente, óxido en la raíz | Las grietas finas requieren ensayos no destructivos (tintas, partículas magnéticas, ultrasonido) |
| Recubrimientos | Ampollas, desprendimiento de pintura, galvanizado consumido | — |

En torres, galpones y estructuras de acero se revisan especialmente las conexiones, los elementos con agua estancada y las placas base. La referencia de diseño es la NCh 427/1.

## 6.4 Albañilería

En Chile la albañilería es sobre todo **confinada** (NCh 2123: paños de ladrillo o bloque enmarcados por pilares y cadenas de hormigón armado) o **armada** (NCh 1928); en edificios de marcos aparece también como **relleno**.

| Patrón | Causa probable |
| --- | --- |
| Grietas diagonales en X en paños de muro | Corte sísmico en el plano |
| Grietas diagonales que atraviesan el paño y penetran en los pilares o cadenas de confinamiento | Corte sísmico que ya dañó el confinamiento: señal grave |
| Grietas diagonales en una dirección que suben hacia la zona que desciende, atravesando piezas y juntas | Asentamiento diferencial (confirmar con nivelación y seguimiento) |
| Separación en el contorno del muro con el marco (grieta perimetral) | Muro de relleno que trabajó contra el marco, o retracción en la junta |
| Grietas horizontales en la base o a media altura, con desplazamiento fuera del plano | Flexión fuera del plano (sismo, empuje) |
| Grietas verticales en encuentros de muros o en esquinas | Falta de traba entre muros, sismo |
| Grietas escalonadas por las juntas | Movimientos térmicos o de retracción, asentamiento leve |
| Piezas desprendidas, pérdida de mortero | Envejecimiento, humedad, sismo |

Un muro de relleno no siempre está en el modelo estructural, pero interactúa con el marco en un sismo: su daño puede indicar un problema en el marco vecino (pilar corto, deriva alta). El laboratorio del módulo 9 tiene un caso así.

## 6.5 Fachadas

- **Enchapes cerámicos y de piedra:** piezas faltantes, fisuras, canterías abiertas, abombamiento y desprendimiento, el riesgo más serio para los peatones. La adherencia no se ve en la foto: la termografía sugiere zonas huecas y la percusión en sitio las confirma.
- **Fachadas ventiladas:** anclajes corroídos o faltantes, placas desalineadas.
- **Muros cortina y vidrio:** vidrios rotos, sellos deteriorados, perfiles deformados.
- **Estucos y pinturas:** fisuras en malla (retracción), ampollas, manchas de humedad, hongos.
- **Elementos en voladizo:** balcones, cornisas, aleros, marquesinas, letreros y antenas, con fisuras en el arranque, corrosión de fijaciones o deformación. Son críticos porque caen sobre zonas de paso.
- **Juntas de dilatación sísmica:** sellos perdidos, cubrejuntas sueltos, golpeteo entre edificios (desconches enfrentados).

## 6.6 Techumbres

- **Losas de techumbre:** fisuras, impermeabilización deteriorada o ausente, apozamientos (huellas de agua estancada, vegetación), desagües obstruidos.
- **Tejas:** rotas, desplazadas, faltantes; cumbreras y limahoyas.
- **Cubiertas livianas metálicas:** corrosión de planchas y tornillos, fijaciones sueltas, deformación de costaneras (se ve como ondulación de la cubierta), canaletas colapsadas.
- **Elementos sobre la techumbre:** estanques, equipos, antenas y sus bases; sobrecargas no previstas en el diseño.

## 6.7 Daños posteriores a un sismo u otro evento

Después de un sismo, un incendio, una inundación o un aluvión, el dron permite mirar sin exponer personas. La prioridad es la seguridad: elementos a punto de caer, inclinaciones evidentes, daño en muros y pilares de los pisos inferiores, colapso parcial, golpeteo con edificios vecinos. La evaluación del daño y de la habitabilidad la hace el evaluador competente con los instrumentos oficiales (fichas de catastro del MINVU y, para el proyecto de recuperación, el Anexo A de la NCh 433); las imágenes del dron son evidencia para esa decisión.

## 6.8 Medir desde la imagen

- **Ancho de fisura:** píxeles a lo ancho × GSD, en una foto frontal, con incertidumbre de ±1 px. Si la fisura ocupa menos de 3 px, se reporta como "menor de 3 × GSD" y se pide medición en sitio.
- **Longitud y área:** en ortomosaicos de fachada o en el modelo 3D (módulo 8), que tienen escala real. En fotos sueltas, con una referencia de tamaño conocido en el mismo plano.
- **Inclinación o desaplome:** en el modelo 3D, no en una foto (la perspectiva engaña).
- Siempre se informa con qué se midió (foto, ortomosaico, nube de puntos) y la incertidumbre.

## 6.9 Severidad y confianza

Cada hallazgo recibe dos calificaciones (escalas completas en el anexo B): **severidad** de 0 (sin daño) a 4 (crítico, acción inmediata), y **confianza** A (el daño se ve con detalle suficiente), B (probable, hay que verificar de cerca) o C (indicio, requiere ensayo). Un hallazgo de severidad 3 con confianza B es un probable daño serio que se debe verificar pronto; esa combinación es la que más vale reportar bien.

La severidad sube cuando:

- El elemento es crítico para la estabilidad: muros y pilares de los pisos inferiores, elementos de transferencia, voladizos sobre zonas de paso.
- El modelo estructural indica una relación demanda/capacidad alta o una deriva cercana al límite de la NCh 433 en ese elemento o piso (módulo 9).
- El daño avanza respecto a la inspección anterior.
- Hay riesgo de caída de objetos sobre personas.

## Taller (2 h)

Cada grupo recibe 30 imágenes (del vuelo del módulo 5 o del banco del curso) y, para cada una:

1. Identifica el daño, el elemento y la zona del elemento.
2. Propone la causa probable y la justifica con el patrón.
3. Mide lo que se puede medir y declara la incertidumbre.
4. Asigna severidad y confianza, y dice qué verificación pide.

Las clasificaciones se comparan entre grupos y las diferencias se discuten. El taller vale el 15 % de la nota.

## Errores frecuentes

- Diagnosticar la causa con una sola foto y sin conocer la estructura.
- Confundir fisuras de retracción con fisuras estructurales, o al revés.
- Reportar anchos de fisura menores que el GSD como si fueran medidos.
- No relacionar el daño del muro de relleno con el marco.
- Calificar la severidad sin considerar quién pasa debajo.

## Autoevaluación

1. Una viga muestra fisuras inclinadas a 45° cerca de los apoyos. ¿Qué esfuerzo las produjo?
2. ¿Qué secuencia de signos visibles indica corrosión de la armadura?
3. En un muro de albañilería confinada aparecen grietas en X que penetran en los pilares. ¿Qué indican?
4. Con GSD de 1.64 mm/px, una fisura ocupa 2 px. ¿Cómo la reporta?
5. ¿Por qué un enchape abombado en el piso 6 sobre una vereda sube de severidad?

## Cómo explicar este módulo (guía del instructor)

**Idea central que el grupo debe llevarse:** una fisura es perpendicular a la tracción que la abrió; primero se observa (qué, dónde, cómo), después se interpreta (por qué) y al final se califica (severidad y confianza).

**Preparación:**

- El banco de imágenes ordenado por material y tipo de daño, con casos chilenos: edificios de muros dañados en el terremoto del Maule de 2010, viviendas de albañilería confinada, corrosión en el borde costero.
- Una viga de goma espuma con una cuadrícula dibujada, una tiza y una hoja de papel para las demostraciones.
- Un visor de imágenes que muestre la posición en píxeles, para el ejercicio de medición.
- Las 30 imágenes del taller y una planilla de clasificación por grupo.

**Secuencia del módulo (360 min):**

| Min | Bloque | Qué hace el instructor | Qué hacen los participantes |
| --- | --- | --- | --- |
| 0-20 | Apertura: "la fisura habla" | Hace las demostraciones de la viga de espuma, la tiza y el papel | Predicen dónde y cómo aparecerá la fisura |
| 20-90 | 6.1 y 6.2 Hormigón armado | Proyecta una foto por patrón: flexión, corte, torsión, compresión, pilar corto, borde de muro, corrosión, retracción. Antes de explicar, pregunta | Para cada foto dicen qué, dónde, cómo y proponen la causa |
| 90-105 | Pausa |  |  |
| 105-130 | 6.3 Acero | Muestra corrosión, pandeo, uniones y soldaduras; marca lo que el dron no puede confirmar | Clasifican cada daño |
| 130-165 | 6.4 Albañilería | Explica albañilería confinada, armada y de relleno con fotos de viviendas chilenas | Distinguen grieta en el paño de grieta que entra en los pilares |
| 165-195 | 6.5 a 6.7 Fachadas, techumbres y daños posteriores a un sismo | Muestra enchapes, voladizos, techumbres; presenta las fichas del MINVU y el Anexo A de la NCh 433 | Discuten qué aporta el dron a cada ficha |
| 195-225 | 6.8 Medir desde la imagen | Da una foto frontal con su GSD | Cuentan los píxeles de una fisura, calculan el ancho y su incertidumbre |
| 225-240 | 6.9 Severidad y confianza | Presenta cinco casos | Cada uno califica en silencio; se comparan y se discuten las diferencias |
| 240-360 | Taller | Circula, pide justificar cada causa con el patrón | Clasifican las 30 imágenes; puesta en común final |

**Demostraciones para explicar la regla de la tracción:**

- **Viga de espuma.** Fléxela apoyada en sus extremos: la cuadrícula se estira abajo y se acorta arriba. Las fisuras de flexión aparecen abajo, verticales, donde la espuma se estira.
- **Tiza en torsión.** Gire una tiza con las dos manos hasta romperla: la fractura es helicoidal, igual que las fisuras de torsión en vigas de borde.
- **Hoja de papel.** Tire de una hoja desde dos esquinas opuestas: se rasga en diagonal, perpendicular al tirón. Así se explican las fisuras de corte a 45° y las grietas en X de un muro sometido a sismo en ambos sentidos.

**Cómo explicar los puntos clave:**

- **Observación primero.** Exija que nadie diga una causa antes de describir qué es, dónde está y cómo es. Anote las tres respuestas en la pizarra y solo después pida la causa.
- **Corrosión como secuencia.** Ordene en la pizarra cuatro fotos (mancha, fisura paralela a la barra, delaminación, armadura expuesta) y pida al grupo ordenarlas en el tiempo.
- **Albañilería confinada.** Dibuje un paño con sus pilares y cadenas: una grieta en X que se queda en el paño es daño importante; si entra en los pilares, el confinamiento ya falló y es grave.
- **Edificios de muros.** Use fotos de 2010: el daño se concentró en la base y en los bordes de los muros, con aplastamiento del hormigón y pandeo de las barras. Es lo primero que se mira en un edificio chileno de muros.
- **Medir.** Ancho = píxeles × GSD, con ±1 píxel. Si salen 2 píxeles, el ancho no se reporta como medido: "menor de 3 × GSD, medir en sitio".
- **Severidad y confianza son independientes.** Un daño puede ser grave y estar poco confirmado (3 B): eso no se baja de severidad, se manda a verificar pronto.

**Preguntas para la clase (con respuesta esperada):**

- "Si la fisura es vertical en el centro de la luz de una viga, ¿dónde estaba la tracción?" Horizontal, en la cara inferior: flexión.
- "¿Por qué la corrosión agrieta el hormigón?" Porque el óxido ocupa más volumen que el acero y revienta el recubrimiento.
- "¿Qué sube la severidad de un enchape suelto?" Que esté sobre una vereda o un acceso.

**Dificultades frecuentes y cómo abordarlas:**

- Saltar a la causa sin describir: aplique la regla de observación primero en cada foto.
- Inflar la severidad por prudencia: recuerde que la confianza es la herramienta para expresar la duda.
- Anchos menores que el GSD reportados como medidos: corrija con el ejercicio de conteo de píxeles.
- Diferencias grandes entre grupos en la misma imagen: úselas; la discusión calibra el criterio del grupo.

**Verificación de cierre:** la planilla del taller (15 % de la nota) y una imagen final que cada participante clasifica solo, con la causa justificada por el patrón.
