# Anexo C. Evaluación

Este anexo trae las respuestas de las autoevaluaciones, el banco de preguntas del examen escrito (15 % de la nota) y el enunciado y la rúbrica del proyecto final (40 %).

## C.1 Respuestas de las autoevaluaciones

**Módulo 1.**

1. Inicial (¿qué hay y en qué estado está?), rutinaria (¿qué cambió?), especial (¿qué causa el daño y qué tan grave es?), posevento (¿es seguro usarla?), de recibo (¿se construyó como se diseñó?).
2. Detecta bien desprendimientos, fisuras visibles, manchas de óxido, piezas faltantes y apozamientos. No confirma sin contacto o ensayo la corrosión de la armadura sin manifestación externa, la delaminación, la adherencia de un enchape, la resistencia del hormigón ni la pérdida de sección real de una barra.
3. Volar junto a una fachada exige atención completa a la distancia, la deriva y el entorno; encuadrar y leer el daño divide esa atención.
4. Los elementos con mayor relación demanda/capacidad y los pisos con mayor deriva: van a la lista de detalles prioritarios, verificando si son visibles desde el exterior.

**Módulo 2.**

1. La DAN 151, porque la operación es sobre un área poblada. Como la empresa cobra por el servicio, necesita AOC (con seguro aprobado por la JAC), además de operador con credencial, RPA registrado y autorización de la DGAC.
2. Cuatro de estos: autorización de la DGAC, credencial de operador y tarjeta de registro, AOC o CEO con seguro, autorización del propietario o del condominio, permiso municipal si se ocupa la vereda, plan de misión con matriz de riesgos, contrato con el tratamiento de datos.
3. R = 16, zona roja: no se vuela así. Se definen mitigaciones que bajen la probabilidad o la severidad y se recalifica; si no sale de la zona roja, se cambia el método (otro horario, cierre del área, otra técnica).
4. Aviso previo a residentes, cortinas cerradas, encuadre sobre los elementos, difuminado de rostros e interiores, control de acceso a las imágenes y tiempo de conservación acordado. La protege la Ley 19.628 y, desde su entrada en vigor, la Ley 21.719.

**Módulo 3.**

1. Lee el sensor por líneas: con la aeronave en movimiento, cada línea se toma en una posición distinta y la imagen se deforma. El programa de fotogrametría supone una toma instantánea, así que aparecen errores geométricos.
2. No. Se necesita la focal real (mm) y el ancho del sensor (mm) o el tamaño del píxel.
3. Logra un GSD fino desde más lejos: más distancia de seguridad a la estructura.
4. Junto a una fachada alta se ve medio cielo y las señales rebotan en los muros; la solución RTK puede pasar de fija a flotante y degradarse a decímetros.

**Módulo 4.**

1. 2.74 mm/px; ancho mínimo medible 3 × 2.74, unos 8.2 mm.
2. D = 0.5 × 40 × 4000 / 6.4 = 12 500 mm = 12.5 m.
3. Foto cada 1.80 m y pasada cada 1.80 m: ⌈12 / 1.8⌉ + 1 = 8 fotos por pasada y ⌈10 / 1.8⌉ + 1 = 7 pasadas, 56 fotos.
4. Porque la huella es muy pequeña (1.60 × 1.20 m a 10 m): la fachada de 30 × 24 m necesitaría 6460 fotos. Se cubre con la gran angular y el zoom se usa para los detalles.
5. v < 0.5 × 0.4 mm / 0.001 s = 200 mm/s = 0.2 m/s. En la práctica, foto en estacionario.

**Módulo 5.**

1. GNSS degradado (multitrayecto y cielo obstruido), con posible paso a modo ATTI. Se aleja hacia el espacio abierto, estabiliza, aumenta la distancia y no se vuelve a acercar hasta que el ensayo de deriva sea aceptable.
2. El acero desvía la brújula: la aeronave interpreta mal su rumbo y puede volar de forma errática.
3. Al dispararse, el RTH sube en vertical hasta 30 m y puede chocar con el balcón del piso de arriba. Hay que pensar el RTH en cada punto y, si es necesario, configurar estacionario o aterrizaje ante la pérdida de enlace.
4. Cuatro de estos: nitidez al 100 %, cobertura completa, exposición en sombras, metadatos de posición (y RTK fija), dos copias antes de formatear.

**Módulo 6.**

1. Corte.
2. Manchas de óxido, fisuras paralelas a las barras (a menudo en esquinas), delaminación y desprendimiento con armadura expuesta.
3. Corte cíclico en el plano del muro, típico de un sismo; si las grietas penetran en los pilares de confinamiento, el daño es grave.
4. 2 px × 1.64 mm/px dan unos 3.3 mm de ancho aparente, por debajo del mínimo medible (3 px, unos 4.9 mm). Se reporta como "fisura detectada, ancho aparente de unos 3 mm, no medible con esta imagen", confianza B, y se pide medición con fisurómetro.
5. Porque puede caer sobre peatones: la consecuencia para las personas eleva la severidad (3 o 4 según el estado) y obliga a medidas preventivas como cerrar la vereda.

**Módulo 7.**

1. Si entran al ajuste, el programa los ajusta y su error deja de ser una medida independiente de la exactitud.
2. Queda mal controlada: los errores de escala e inclinación crecen hacia arriba porque el modelo se extrapola fuera de la zona de control.
3. Del orden de 1 a 3 veces el GSD: unos 1.6 a 4.9 mm.
4. Que ambos modelos estén en el mismo marco de referencia (la misma red de puntos de control), que se conozca su exactitud y que el cambio detectado supere la incertidumbre combinada.

**Módulo 8.**

1. Alturas mezcladas: no se aplicó la ondulación geoidal (h = H + N; en el laboratorio N = 30 m).
2. Porque está en un elemento que no se modeló (albañilería de relleno, enchape, cubierta liviana). También porque el modelo trabaja con ejes y el daño está en la cara del elemento; por eso existe la tolerancia.
3. Para que el modelo 3D y el modelo estructural queden en el mismo marco: los hallazgos caen sobre los elementos sin transformaciones adicionales y los errores de dos georreferencias distintas no se suman.
4. Cuanto mayor es la D/C, menor es la reserva de capacidad del elemento: el mismo daño es más preocupante y sube la prioridad de verificación.

**Módulo 9.**

1. "Se observa en la cara exterior del pilar C1-02 una fisura inclinada unos 45°, de 0.9 m de largo y ancho estimado de 1.5 mm ± 0.4 mm (observación). El patrón es compatible con corte, posiblemente de origen sísmico (interpretación). Severidad 3, confianza B."
2. El GSD logrado y el RMS en los puntos de chequeo.
3. Tres copias de los datos, en dos medios distintos, una de ellas fuera del sitio.
4. Porque condicionan la lectura de todo lo demás: el lector debe saber qué no se pudo ver antes de leer las conclusiones.

## C.2 Banco de preguntas del examen

El examen tiene 15 preguntas de selección múltiple tomadas de este banco y 2 preguntas abiertas, en 45 minutos.

| N.º | Pregunta | Opciones | Respuesta |
| --: | --- | --- | --- |
| 1 | ¿Qué dato no sirve para calcular el GSD? | a) Ancho del sensor · b) Focal real · c) Resolución en píxeles · d) Focal equivalente a 35 mm | d |
| 2 | El GSD de la cámara gran angular del curso a 6 m es | a) 0.40 mm/px · b) 1.64 mm/px · c) 2.74 mm/px · d) 5.54 mm/px | b |
| 3 | Para medir con confianza el ancho de una fisura, esta debe ocupar al menos | a) 1 px · b) 3 px · c) 10 px · d) Basta con que se vea | b |
| 4 | Una inspección comercial de fachada en una zona urbana de Chile se rige por | a) DAN 91 · b) DAN 151 · c) Ley 21.442 · d) No requiere norma | b |
| 5 | Una fisura es | a) Paralela a la tracción que la abrió · b) Perpendicular a la tracción que la abrió · c) Siempre vertical · d) Independiente de los esfuerzos | b |
| 6 | Fisuras paralelas a las barras con manchas de óxido indican | a) Retracción plástica · b) Corrosión de la armadura · c) Flexión · d) Asentamiento | b |
| 7 | Grietas en X en un muro de albañilería indican | a) Retracción · b) Corte cíclico (sismo) · c) Corrosión · d) Humedad | b |
| 8 | Para fotografiar una fisura fina desde 10 m conviene usar | a) Zoom digital · b) Zoom óptico · c) Acercarse a 2 m · d) Subir el ISO | b |
| 9 | Un enchape abombado sobre una vereda se confirma | a) Con una foto más cercana · b) Con percusión en sitio · c) Con el ortomosaico · d) No hace falta confirmarlo | b |
| 10 | La exactitud de un modelo fotogramétrico se reporta con | a) El RMS de los GCP · b) El error de reproyección · c) El RMS de puntos de chequeo independientes · d) El número de fotos | c |
| 11 | Todos los hallazgos aparecen 30 m más abajo que en la realidad; lo más probable es | a) Huso UTM equivocado · b) Alturas elipsoidales y ortométricas mezcladas · c) Norte de cuadrícula · d) Error de GSD | b |
| 12 | Junto a una fachada alta, el dron deriva con los mandos quietos; la causa más probable es | a) Batería baja · b) GNSS degradado · c) Cámara mal configurada · d) Tarjeta llena | b |
| 13 | No se despega desde una losa con mucha armadura expuesta porque | a) Hay polvo · b) El acero desvía la brújula · c) Se calienta · d) No hay problema | b |
| 14 | A 3000 m de altitud (faenas de cordillera), el aire es aproximadamente | a) 5 % menos denso · b) 26 % menos denso · c) 50 % menos denso · d) Igual de denso que a nivel del mar | b |
| 15 | Con v = 1 m/s, exposición de 1/500 s y GSD de 1.64 mm/px, el desplazamiento en la imagen es | a) 0.3 px · b) 0.6 px · c) 1.2 px · d) 2.4 px | c |
| 16 | Un hallazgo queda a 1.3 m del elemento más cercano del modelo; se debe | a) Descartarlo · b) Asignarlo al elemento más cercano sin comentario · c) Revisar si está en un elemento no modelado y reportarlo asociado al marco · d) Volver a volar | c |
| 17 | Confianza B significa | a) Daño confirmado · b) Daño probable, hay que verificar de cerca · c) Indicio que requiere ensayo · d) Sin daño | b |
| 18 | La distancia mínima del curso a una fachada con GNSS estable y viento bajo es | a) 1 m · b) 3 m · c) 5 m · d) 30 m | c |
| 19 | La fachada de 30 × 24 m con la gran angular a 6 m y solapes de 80/70 necesita | a) 56 fotos · b) 270 fotos · c) 486 fotos · d) 6460 fotos | b |
| 20 | ¿Qué no va en el resumen ejecutivo del informe? | a) La conclusión · b) Los hallazgos de severidad 3 y 4 · c) Las acciones inmediatas · d) La configuración detallada de la cámara | d |

**Preguntas abiertas (se eligen 2):**

- **A.** Construya la matriz de riesgos de la inspección de la cubierta de un centro comercial en funcionamiento, con al menos cuatro peligros y sus mitigaciones.
- **B.** Para detectar fisuras de 1 mm en una fachada de 20 pisos, compare acercarse con la gran angular frente a usar el zoom desde más lejos. Justifique con cálculos de GSD, distancia y número de fotos.
- **C.** El hallazgo H05 del laboratorio no cae en ningún elemento del modelo. Explique por qué, cómo lo reporta y qué verificación pide.
- **D.** Una foto muestra manchas de óxido y fisuras paralelas a las barras en una viga de borde de un edificio en la costa. Describa cómo la reporta (observación, causa probable, severidad y confianza) y qué verificación pide.

Criterio de las preguntas abiertas: respuesta correcta y justificada, 100 %; correcta sin justificación suficiente, 60 %; con errores de concepto, 20 %; sin respuesta, 0 %.

## C.3 Proyecto final

Cada grupo de 3 o 4 participantes inspecciona el caso conductor y entrega:

1. Plan de misión completo (anexo B) con matriz de riesgos.
2. Datos de vuelo: fotos de cobertura y de detalle, bitácora y listas de chequeo diligenciadas. En modalidad virtual se usa el conjunto de datos del curso.
3. Productos fotogramétricos: ortomosaico de al menos una fachada e informe de calidad con RMS en puntos de chequeo.
4. Al menos 8 hallazgos con ficha completa, severidad y confianza.
5. Ubicación de los hallazgos en el modelo estructural (archivo de hallazgos y tabla hallazgo-elemento-D/C), o con el edificio de ejemplo en modalidad virtual.
6. Informe de inspección con la estructura del módulo 9.
7. Presentación de 15 minutos con preguntas del jurado.

**Rúbrica:**

| Criterio | Peso | Excelente (100 %) | Adecuado (75 %) | Insuficiente (40 %) |
| --- | --: | --- | --- | --- |
| Seguridad y cumplimiento | 20 % | Plan, permisos, listas y matriz completos y específicos del sitio; operación sin observaciones | Completos, con observaciones menores | Documentos genéricos o incompletos; una falta grave reprueba el componente |
| Calidad de los datos | 20 % | GSD del plan logrado, cobertura completa, fotos nítidas, RMS en chequeo dentro del criterio | Pequeñas zonas sin cubrir o GSD algo mayor, declarado | Fotos movidas, zonas importantes sin cubrir o exactitud no reportada |
| Lectura de daños | 25 % | Hallazgos bien identificados, causas justificadas por el patrón, mediciones con incertidumbre, severidad y confianza coherentes | Errores menores de clasificación | Confusiones de concepto o mediciones por debajo de la resolución presentadas como válidas |
| Integración con el modelo | 15 % | Todos los hallazgos ubicados; los no modelados explicados; priorización con D/C y derivas | Ubicados sin priorización | Hallazgos sin ubicar o con errores de coordenadas sin detectar |
| Informe y comunicación | 20 % | Observación separada de interpretación, limitaciones al principio, recomendaciones con plazo, presentación clara | Estructura completa con fallas de redacción | Álbum de fotos sin conclusión o sin limitaciones |

Nota del proyecto = suma de peso × nivel alcanzado en cada criterio. El proyecto vale el 40 % de la nota del curso.

## Cómo conducir el proyecto final (guía del relator)

**Idea central:** el proyecto final demuestra que el grupo puede recorrer solo el flujo completo, del plan al informe; la evaluación mira el criterio, no la cantidad de fotos.

**Antes del día 5:**

- Entregue el enunciado y la rúbrica el día 3, junto con la lista de entregables y la hora límite (una carpeta compartida por grupo, 30 minutos antes de la jornada).
- Pida que la presentación siga este orden: pregunta del encargo, método, hallazgos principales, prioridad con D/C y deriva, recomendaciones y limitaciones.
- Forme el jurado con el relator y, si es posible, uno o dos invitados: un ingeniero civil calculista (quien recibe los hallazgos para evaluarlos), el operador RPAS de las prácticas o un administrador de condominio (quien lee estos informes).
- Reúna las observaciones de seguridad de las prácticas de cada grupo: alimentan el primer criterio de la rúbrica.

**Secuencia de la jornada (240 min, para seis grupos):**

| Min | Bloque | Qué se hace |
| --- | --- | --- |
| 0-45 | Examen escrito | 15 preguntas del banco y 2 abiertas (15 % de la nota) |
| 45-195 | Presentaciones | 15 minutos por grupo y 10 de preguntas del jurado |
| 195-210 | Pausa y deliberación | Cada jurado califica solo con la rúbrica; luego comparan |
| 210-235 | Retroalimentación | Un punto fuerte y una mejora por grupo; cierre general del curso |
| 235-240 | Cierre | Encuesta de satisfacción y entrega de constancias |

Con más grupos, reduzca las preguntas a 5 minutos o divida el jurado en dos salas con la misma rúbrica.

**Preguntas sugeridas para el jurado:**

- "¿Qué no pudieron ver y cómo lo resolverían?"
- "¿Por qué este hallazgo es severidad 3 y no 2? ¿Qué confianza tiene y qué verificación piden?"
- "¿Cuánto dio el RMS en los puntos de chequeo y qué significa para sus mediciones?"
- "¿Qué cambiarían del plan de vuelo si volvieran mañana?"
- "¿Qué norma de la DGAC rigió su operación y qué autorizaciones necesitaron?"

**Uso de la rúbrica:**

- Cada jurado califica cada criterio por separado en uno de los niveles (100 %, 75 % o 40 %) y anota una frase que lo justifique.
- Si dos jurados difieren en más de un nivel en un criterio, lo discuten antes de promediar.
- La nota del proyecto es la suma de peso por nivel; luego se combina con los demás componentes (anexo C y sección Evaluación).
- Una falta grave de seguridad en las prácticas reprueba el componente práctico aunque el informe sea excelente.

**Retroalimentación:** sea concreto y use el lenguaje de la rúbrica ("el hallazgo H01 está bien descrito, pero el ancho de 0.3 mm está bajo el GSD y no se puede informar como medido"). Cierre recordando los tres mensajes del curso: el dron detecta, prioriza y documenta; la seguridad no se negocia; el informe dice lo que se vio y lo que falta verificar.
