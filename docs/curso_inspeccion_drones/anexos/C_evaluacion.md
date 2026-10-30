# Anexo C. Evaluación

## 1. Respuestas de las autoevaluaciones

### Módulo 1

1. Inicial (¿qué hay y en qué estado está?), rutinaria (¿qué cambió?),
   especial (¿qué causa el daño y qué tan grave es?), posevento (¿es seguro
   usarla?), de recibo (¿se construyó como se diseñó?).
2. Detecta bien: desprendimientos, fisuras visibles, manchas de óxido,
   piezas faltantes, encharcamientos. No confirma sin contacto o ensayo: la
   corrosión del refuerzo sin manifestación externa, la delaminación, la
   adherencia de un enchape, la resistencia del concreto, la pérdida de
   sección real de una barra.
3. Volar junto a una fachada exige atención completa a la distancia, la deriva
   y el entorno. Encuadrar y leer el daño divide esa atención.
4. Los elementos con mayor relación demanda/capacidad y los pisos con mayor
   deriva: van a la lista de detalles prioritarios. También se verifica si son
   visibles desde el exterior.

### Módulo 2

1. En la categoría **específica**: es una operación comercial y se vuela a
   menos de 30 m de la edificación, fuera de las condiciones de la categoría
   abierta. Requiere explotador, piloto certificado, registro y autorización
   de vuelo.
2. Cuatro de estos: autorización de vuelo, permiso del propietario o de la
   administración, plan de misión con matriz de riesgos, póliza, certificado
   del piloto y registro de la aeronave, contrato con el tratamiento de datos.
3. R = 16, zona roja: no se vuela así. Se definen mitigaciones para bajar la
   probabilidad o la severidad y se recalifica. Si no sale de la zona roja,
   se cambia el método (otro horario, cierre del área, otra técnica).
4. Aviso previo a residentes, cortinas cerradas, encuadre sobre los elementos,
   difuminado de rostros e interiores, control de acceso a las imágenes y
   tiempo de conservación acordado.

### Módulo 3

1. Lee el sensor por líneas: con la aeronave en movimiento, cada línea se
   toma en una posición distinta y la imagen se deforma. El programa de
   fotogrametría supone una toma instantánea, así que aparecen errores
   geométricos.
2. No. Se necesita la focal real (mm) y el ancho del sensor (mm) o el tamaño
   del píxel.
3. Logra un GSD fino desde más lejos: más distancia de seguridad a la
   estructura.
4. Junto a una fachada alta se ve medio cielo y las señales rebotan en los
   muros. La solución RTK puede pasar de fija a flotante y degradarse a
   decímetros.

### Módulo 4

1. 2.74 mm/px; ancho mínimo medible 3 × 2.74 ≈ 8.2 mm.
2. D = 0.5 × 40 × 4000 / 6.4 = 12 500 mm = **12.5 m**.
3. Foto cada 1.80 m y pasada cada 1.80 m: ⌈12 / 1.8⌉ + 1 = 8 fotos por pasada,
   ⌈10 / 1.8⌉ + 1 = 7 pasadas: **56 fotos**.
4. Porque la huella es muy pequeña (1.60 × 1.20 m a 10 m): la fachada de
   30 × 24 m necesitaría 6460 fotos. Se cubre con la gran angular y se usa el
   zoom para los detalles.
5. v < 0.5 × 0.4 mm / 0.001 s = 200 mm/s = **0.2 m/s**. En la práctica, foto
   en estacionario.

### Módulo 5

1. GNSS degradado (multitrayecto y cielo obstruido), con posible paso a modo
   ATTI. Se aleja hacia el espacio abierto, estabiliza, aumenta la distancia y
   no se vuelve a acercar hasta que el ensayo de deriva sea aceptable.
2. El acero desvía la brújula: la aeronave interpreta mal su rumbo y puede
   volar de forma errática.
3. Al dispararse, el RTH sube en vertical hasta 30 m: puede chocar con el
   balcón del piso de arriba. Hay que pensar el RTH en cada punto y, si es
   necesario, configurar estacionario o aterrizaje ante la pérdida de enlace.
4. Cuatro de estos: nitidez al 100 %, cobertura completa, exposición en
   sombras, metadatos de posición (y RTK fija), pares térmica-visible, dos
   copias antes de formatear.

### Módulo 6

1. Cortante.
2. Manchas de óxido, fisuras paralelas a las barras (a menudo en esquinas),
   delaminación y desprendimiento con acero expuesto.
3. Cortante cíclico en el plano del muro, típico de un sismo.
4. 2 px × 1.64 mm/px ≈ 3.3 mm de ancho aparente, por debajo del mínimo medible
   (3 px ≈ 4.9 mm). Se reporta como "fisura detectada, ancho aparente ≈ 3 mm,
   no medible con esta imagen", confianza B, y se pide medición con
   fisurómetro.
5. Porque puede caer sobre peatones: la consecuencia para las personas eleva
   la severidad (3 o 4 según el estado) y obliga a medidas preventivas como
   cerrar el andén.

### Módulo 7

1. Su emisividad es muy baja: refleja la radiación del entorno y la
   temperatura aparente no representa la de la lámina.
2. En la mañana, mientras el sol calienta la fachada oriental. Las zonas con
   vacío bajo el enchape se ven más calientes que las adheridas.
3. 3 × 3 px a 4.62 mm/px: unos **14 × 14 mm**.
4. Cambiando la posición o el ángulo de la cámara: un reflejo se mueve, una
   anomalía real no. Además se compara con la foto visible.

### Módulo 8

1. Si entran al ajuste, el programa los ajusta y su error deja de ser una
   medida independiente de la exactitud.
2. Queda mal controlada: los errores de escala e inclinación crecen hacia
   arriba porque el modelo se extrapola fuera de la zona de control.
3. Del orden de 1 a 3 veces el GSD: unos 1.6 a 4.9 mm.
4. Que ambos modelos estén en el mismo marco de referencia (la misma red de
   puntos de control), que se conozca su exactitud y que el cambio detectado
   supere la incertidumbre combinada.

### Módulo 9

1. Alturas mezcladas: no se aplicó la ondulación geoidal (h = H + N; en el
   ejemplo N = 4 m).
2. Porque está en un elemento que no se modeló (mampostería de relleno,
   enchape, cubierta liviana). También porque el modelo trabaja con ejes y el
   daño está en la cara del elemento (por eso la tolerancia).
3. Para que el modelo 3D y el modelo estructural queden en el mismo marco:
   los hallazgos caen sobre los elementos sin transformaciones adicionales y
   los errores de dos georreferencias distintas no se suman.
4. Cuanto mayor la D/C, menor la reserva de capacidad del elemento: el mismo
   daño es más preocupante y sube la prioridad de verificación.

### Módulo 10

1. "Se observa en la cara exterior de la columna C1-02 una fisura inclinada
   unos 45°, de 0.9 m de largo y ancho estimado de 1.5 mm ± 0.4 mm
   (observación). El patrón es compatible con cortante, posiblemente de origen
   sísmico (interpretación). Severidad 3, confianza B."
2. El GSD logrado y el RMS en los puntos de chequeo.
3. Tres copias de los datos, en dos medios distintos, una de ellas fuera del
   sitio.
4. Porque condicionan la lectura de todo lo demás: el lector debe saber qué no
   se pudo ver antes de leer las conclusiones.

---

## 2. Banco de preguntas del examen

Examen de 15 preguntas de selección múltiple tomadas de este banco y 2
preguntas abiertas. Tiempo: 45 minutos. La respuesta correcta está en
**negrilla**.

1. ¿Qué dato **no** sirve para calcular el GSD?
   a) Ancho del sensor · b) Focal real · c) Resolución en píxeles ·
   **d) Focal equivalente a 35 mm**
2. El GSD de la cámara gran angular del curso a 6 m es:
   a) 0.40 mm/px · **b) 1.64 mm/px** · c) 2.74 mm/px · d) 5.54 mm/px
3. Para medir con confianza el ancho de una fisura, esta debe ocupar al menos:
   a) 1 px · **b) 3 px** · c) 10 px · d) Basta con que se vea
4. Una inspección comercial de fachada a 6 m de la edificación, en Colombia,
   corresponde normalmente a la categoría:
   a) Abierta · **b) Específica** · c) Certificada · d) No requiere categoría
5. Una fisura es:
   a) Paralela a la tracción que la abrió · **b) Perpendicular a la tracción
   que la abrió** · c) Siempre vertical · d) Independiente de los esfuerzos
6. Fisuras paralelas a las barras con manchas de óxido indican:
   a) Retracción plástica · **b) Corrosión del refuerzo** · c) Flexión ·
   d) Asentamiento
7. Grietas en X en un muro de mampostería indican:
   a) Retracción · **b) Cortante cíclico (sismo)** · c) Corrosión ·
   d) Humedad
8. Sobre una lámina de aluminio pulido, la cámara térmica:
   a) Mide bien su temperatura · **b) Mide sobre todo el reflejo del entorno**
   · c) Siempre la muestra fría · d) Necesita emisividad 0.95
9. Para buscar desprendimientos de enchape con carga solar en una fachada
   oriental, se vuela:
   **a) En la mañana, durante el calentamiento** · b) A mediodía, con la
   fachada en sombra · c) Después de la lluvia · d) A cualquier hora
10. La exactitud de un modelo fotogramétrico se reporta con:
    a) El RMS de los GCP · b) El error de reproyección · **c) El RMS de
    puntos de chequeo independientes** · d) El número de fotos
11. Todos los hallazgos aparecen 4 m más abajo que en la realidad. Lo más
    probable es:
    a) Zona UTM equivocada · **b) Alturas elipsoidales y ortométricas
    mezcladas** · c) Norte de cuadrícula · d) Error de GSD
12. Junto a una fachada alta, el dron deriva con los mandos quietos. La causa
    más probable es:
    a) Batería baja · **b) GNSS degradado** · c) Cámara mal configurada ·
    d) Tarjeta llena
13. No se despega desde una losa con mucho acero expuesto porque:
    a) Hay polvo · **b) El acero desvía la brújula** · c) Se calienta ·
    d) No hay problema
14. A 2600 m de altitud, el aire es, aproximadamente:
    a) 5 % menos denso · **b) 23 % menos denso** · c) 50 % menos denso ·
    d) Igual de denso que a nivel del mar
15. Con v = 1 m/s, exposición de 1/500 s y GSD de 1.64 mm/px, el
    desplazamiento en la imagen es:
    a) 0.3 px · b) 0.6 px · **c) 1.2 px** · d) 2.4 px
16. Un hallazgo queda a 1.3 m del elemento más cercano del modelo. Se debe:
    a) Descartarlo · b) Asignarlo al elemento más cercano sin comentario ·
    **c) Revisar si está en un elemento no modelado y reportarlo asociado al
    pórtico** · d) Volver a volar
17. Confianza B significa:
    a) Daño confirmado · **b) Daño probable, hay que verificar de cerca** ·
    c) Indicio que requiere ensayo · d) Sin daño
18. La distancia mínima del curso a una fachada con GNSS estable y viento
    bajo es:
    a) 1 m · b) 3 m · **c) 5 m** · d) 30 m
19. La fachada de 30 × 24 m con la gran angular a 6 m y solapes 80/70
    necesita:
    a) 56 fotos · **b) 270 fotos** · c) 486 fotos · d) 6460 fotos
20. ¿Qué **no** va en el resumen ejecutivo del informe?
    a) La conclusión · b) Los hallazgos de severidad 3 y 4 · c) Las acciones
    inmediatas · **d) La configuración detallada de la cámara**

### Preguntas abiertas (se eligen 2)

- **A.** Construya la matriz de riesgos de la inspección de la cubierta de un
  centro comercial en funcionamiento, con al menos cuatro peligros y sus
  mitigaciones.
- **B.** Para detectar fisuras de 1 mm en una fachada de 20 pisos, compare
  acercarse con la gran angular frente a usar el zoom desde más lejos.
  Justifique con cálculos de GSD, distancia y número de fotos.
- **C.** El hallazgo H05 del laboratorio no cae en ningún elemento del
  modelo. Explique por qué, cómo lo reporta y qué verificación pide.
- **D.** Un termograma muestra una zona caliente en un enchape a las 9:00 en
  una fachada oriental. Describa cómo confirma si es un desprendimiento.

**Criterio de las preguntas abiertas:** respuesta correcta y justificada
(100 %), correcta sin justificación suficiente (60 %), con errores de concepto
(20 %), sin respuesta (0 %).

---

## 3. Proyecto final

### Enunciado

Cada grupo (3 o 4 participantes) inspecciona el caso conductor y entrega:

1. **Plan de misión** completo (anexo B), con matriz de riesgos.
2. **Datos de vuelo:** fotos de cobertura y detalle, térmicas si aplican,
   bitácora y listas de chequeo diligenciadas. En modalidad virtual se usa el
   conjunto de datos del curso.
3. **Productos fotogramétricos:** ortomosaico de al menos una fachada e
   informe de calidad con RMS en puntos de chequeo.
4. **Al menos 8 hallazgos** con ficha completa, severidad y confianza.
5. **Ubicación en el modelo estructural** con Tav0t (archivo de hallazgos y
   tabla hallazgo-elemento-D/C), o con el edificio de ejemplo en modalidad
   virtual.
6. **Informe de inspección** con la estructura del módulo 10.
7. **Presentación** de 15 minutos con preguntas del jurado.

### Rúbrica

| Criterio | Peso | Excelente (100 %) | Adecuado (75 %) | Insuficiente (40 %) |
|---|---|---|---|---|
| **Seguridad y cumplimiento** | 20 % | Plan, permisos, listas y matriz completos y específicos del sitio; operación sin observaciones | Completos con observaciones menores | Documentos genéricos o incompletos (una falta grave reprueba el componente) |
| **Calidad de los datos** | 20 % | GSD del plan logrado, cobertura completa, fotos nítidas, RMS en chequeo dentro del criterio | Pequeñas zonas sin cubrir o GSD algo mayor, declarado | Fotos movidas, zonas importantes sin cubrir o exactitud no reportada |
| **Lectura de daños** | 25 % | Hallazgos bien identificados, causas justificadas por el patrón, mediciones con incertidumbre, severidad y confianza coherentes | Errores menores de clasificación | Confusiones de concepto o mediciones por debajo de la resolución presentadas como válidas |
| **Integración con el modelo** | 15 % | Todos los hallazgos ubicados; los no modelados explicados; priorización con D/C y derivas | Ubicados sin priorización | Hallazgos sin ubicar o con errores de coordenadas sin detectar |
| **Informe y comunicación** | 20 % | Observación separada de interpretación, limitaciones al principio, recomendaciones con plazo, presentación clara | Estructura completa con fallas de redacción | Álbum de fotos sin conclusión o sin limitaciones |

Nota del proyecto = Σ (peso × nivel). El proyecto vale el 40 % de la nota del
curso.
