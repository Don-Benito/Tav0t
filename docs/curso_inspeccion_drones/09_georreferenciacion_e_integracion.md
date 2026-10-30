# Módulo 9. Georreferenciación de hallazgos e integración con el modelo estructural

**Duración:** 2 h (0.5 h de teoría y 1.5 h de laboratorio) · **Competencia:** C9

Un hallazgo ubicado en un elemento del modelo sirve para decidir: "fisura de corte en el pilar C1-02, D/C 0.86" dice más que "fisura en la fachada norte, piso 1".

**Objetivos de aprendizaje.**

1. Evita los errores de marco de referencia, de proyección y de alturas que mueven un hallazgo de piso o de elemento.
2. Lleva los hallazgos de la inspección al sistema del modelo estructural y los asigna a elementos.
3. Usa los resultados del análisis (demanda/capacidad, derivas frente al límite de la NCh 433) para priorizar los hallazgos.

## 9.1 Por qué ubicar el hallazgo en el modelo

- Relaciona el daño con la demanda calculada: un daño en un elemento muy exigido es más preocupante.
- Permite volver al mismo elemento en la siguiente inspección y comparar.
- Pone los hallazgos en el mismo mapa que el modelo (GeoJSON en QGIS, KML en Google Earth).

## 9.2 El marco de referencia en Chile

- **SIRGAS-Chile** es el sistema de referencia oficial, mantenido por el Instituto Geográfico Militar (IGM) en la Red Geodésica Nacional. La realización publicada por el IGM usa la época 2021.0 y el elipsoide GRS80.
- En Chile continental se usa la proyección **UTM, husos 18 Sur y 19 Sur**. Santiago está en el huso 19 Sur.
- **Chile se mueve.** Los grandes terremotos desplazan la red geodésica: después del terremoto del Maule de 2010 hubo puntos que se movieron metros. Por eso toda coordenada se declara con su marco y su época, y los puntos de control de una inspección se vuelven a medir después de un sismo fuerte.

## 9.3 Los tres errores que mueven un hallazgo

**1. Alturas elipsoidales y ortométricas mezcladas.** El GNSS y muchos programas de fotogrametría trabajan con altura elipsoidal h; los planos y la topografía, con altura ortométrica H. Se relacionan con la ondulación geoidal N del sitio:

```latex
h = H + N
```

Si los puntos de control se dieron con H y los hallazgos salen con h (o al revés), todo se mueve N metros en vertical. En el laboratorio se usa N = 30 m, un valor ilustrativo: en un proyecto real N se obtiene en el punto con el modelo geoidal oficial del IGM o con EGM2008. Treinta metros son unos diez pisos.

**2. Marco, huso o época distintos.** Verifique que los hallazgos y el proyecto están en el mismo marco (SIRGAS-Chile), en el mismo huso UTM y en la misma época. Una obra en el límite entre los husos 18 y 19 debe trabajarse completa en uno de ellos.

**3. Norte verdadero y norte de cuadrícula.** Si el acimut del modelo se tomó de un plano en UTM y se declaró como verdadero, el modelo queda girado la convergencia de meridianos. En Santiago, lejos del meridiano central del huso 19, la convergencia es de 0.91°: 16 cm en 10 m. El software lo corrige si se declara `"norte": "cuadricula"`.

## 9.4 Flujo de integración

1. Una red de puntos de control se mide en terreno con GNSS RTK o estación total, en SIRGAS-Chile.
2. Esa misma red georreferencia el modelo fotogramétrico (módulo 8) y el modelo estructural.
3. De la fotogrametría salen los hallazgos con coordenadas UTM y altura ortométrica.
4. El script del laboratorio lleva cada hallazgo al sistema del modelo y lo asigna al elemento más cercano.
5. Cada hallazgo se completa con la D/C del elemento y la deriva del piso, y pasa a la ficha y al informe.

Como la misma red de puntos georreferencia los dos modelos, ambos quedan en el mismo marco y los errores de dos georreferencias distintas no se suman.

## 9.5 Laboratorio

**Edificio de ejemplo:** marco de hormigón armado de 3 pisos en Santiago, 12 × 10 m, con pilares en los ejes A-B-C (x = 0, 6, 12 m) y 1-2-3 (y = 0, 5, 10 m), pisos a 3.5, 6.5 y 9.5 m y albañilería de relleno en las fachadas. Los resultados del análisis son sintéticos, solo para el curso. Los hallazgos de `ejemplos/curso_drones/hallazgos.json` simulan lo que entrega el modelo fotogramétrico: coordenadas UTM 19S y altura ortométrica en SIRGAS-Chile, con un error de un par de centímetros.

**Nomenclatura de elementos:** `C{piso}-{iy}{ix}` pilares, `VX{piso}-{iy}{ix}` y `VY{piso}-{iy}{ix}` vigas en dirección X y Y, `L{piso}-{iy}{ix}` losas, donde `ix` e `iy` son los índices de los ejes (0, 1, 2).

**Paso 1. Georreferenciar el modelo con los puntos de control y revisar las derivas.**

```bash
python -m tav0t.georef ejecutar ejemplos/curso_drones/proyecto_santiago.json
```

Revise en la salida el huso (UTM 19S), el RMS del ajuste (1.7 mm en horizontal y 3.1 mm en vertical) y las derivas, verificadas con el límite de la NCh 433 (0.002 de la altura de entrepiso):

| Piso | Cotas (m) | Deriva máxima | Uso del límite |
| --- | --- | --: | --: |
| 1 | 0.00-3.50 | 0.00149 | 75 % |
| 2 | 3.50-6.50 | 0.00191 | 96 % |
| 3 | 6.50-9.50 | 0.00156 | 78 % |

La NCh 433 mide la deriva en el centro de masas (0.002) y permite en cualquier punto hasta 0.001 más; el laboratorio verifica la deriva máxima contra 0.002, del lado de la seguridad. El piso 2 queda al 96 % del límite. Abra `ejemplos/salida/curso_santiago/georref.kml` en Google Earth.

**Paso 2. Ubicar los hallazgos.**

```bash
python ejemplos/curso_drones/ubicar_hallazgos.py
```

Salida esperada:

```
Hallazgo        x       y       z  Elemento    d (m)  Tipo
H01         12.00   -0.25    1.83  C1-02        0.25  Fisura diagonal
H02          3.00   -0.15    6.11  VX2-00       0.42  Fisura vertical
H03         12.14    1.20    9.16  VY3-02       0.37  Desprendimiento con armadura expuesta
H04          9.21    2.58    9.55  L3-01        0.05  Mapa de fisuras
H05          2.99   10.14    5.21  ¿VX2-20?     1.29  Anomalía térmica
H06         -0.26   10.03    0.33  C1-20        0.26  Fisura horizontal
```

El script:

1. Ejecuta la georreferencia del proyecto y la reconstruye.
2. Convierte cada hallazgo de UTM + H a coordenadas geodésicas y suma N para obtener h.
3. Lo lleva al sistema del modelo.
4. Calcula la distancia a cada barra (segmento) y a cada losa (polígono) y se queda con el elemento más cercano.
5. Si la distancia supera la tolerancia (0.6 m: medio lado de la sección más grande más el error del modelo fotogramétrico), lo marca entre signos de interrogación.

La distancia de 0.25 m de H01 es la mitad del lado del pilar de 50 cm: la fisura está en la cara exterior, y el modelo trabaja con ejes.

**Paso 3. Interpretar el hallazgo sin elemento.** H05 es una anomalía térmica en el muro de albañilería de la fachada del eje 3, piso 2. El muro de relleno no está en el modelo, por eso queda a 1.29 m de la viga más cercana. No se descarta: se reporta asociado al marco del eje 3 entre los ejes A y B, en el piso que está al 96 % del límite de deriva. La pregunta para la verificación en sitio es si la anomalía es humedad (lo que sugiere su forma) o daño del muro por interacción con el marco (sección 6.4).

**Paso 4. Priorizar con el análisis.** Relación D/C del caso SISMO\_X (archivo `ejemplos/curso_drones/edificio_santiago.json`, sección `resultados`):

| Hallazgo | Elemento | D/C | Comentario |
| --- | --- | --: | --- |
| H01 | C1-02 | 0.86 | Fisura de corte en pilar esquinero del primer piso, elemento muy exigido |
| H02 | VX2-00 | 0.78 | Fisura de flexión en viga de fachada |
| H03 | VY3-02 | 0.38 | Corrosión: problema de durabilidad más que de demanda |
| H04 | L3-01 | — | Losa de techumbre: retracción y falta de impermeabilización |
| H05 | Muro, eje 3 | — | Piso al 96 % del límite de deriva |
| H06 | C1-20 | 0.92 | Fisura horizontal en el arranque de un pilar esquinero del primer piso |

Ejercicio: ¿qué hallazgos irían primero a verificación de cerca? Justifique con la severidad, la confianza, la D/C y la deriva.

**Paso 5. Provocar el error de alturas.** Suponga que los hallazgos se convierten sin sumar la ondulación geoidal:

```bash
python ejemplos/curso_drones/ubicar_hallazgos.py --ondulacion 0
```

```
Hallazgo        x       y       z  Elemento    d (m)  Tipo
H01         12.00   -0.25  -28.17  ¿C1-02?     28.17  Fisura diagonal
H02          3.00   -0.15  -23.89  ¿C1-01?     24.08  Fisura vertical
H03         12.14    1.20  -20.84  ¿C1-02?     20.87  Desprendimiento con armadura expuesta
H04          9.21    2.58  -20.45  ¿C1-12?     20.78  Mapa de fisuras
H05          2.99   10.14  -24.79  ¿C1-20?     24.97  Anomalía térmica
H06         -0.26   10.03  -29.67  ¿C1-20?     29.67  Fisura horizontal
```

Todos los hallazgos bajan exactamente N = 30 m y quedan bajo el terreno, mientras la planta (x, y) no cambia. **Si todos los hallazgos se desplazan lo mismo en vertical, sospeche de las alturas antes que de la fotogrametría.** Si el error es en planta, revise el huso UTM, el marco y su época, o el norte.

**Paso 6. Llevar los hallazgos a las fichas.** Para H01 y H06, complete la ficha de hallazgo del anexo B, que trae H01 como ejemplo resuelto.

**Variaciones:**

- Ejecute `python -m tav0t.georef utm -33.4455 -70.657`, lea la convergencia de meridianos en el sitio (0.91°) y calcule cuánto se movería el pilar más alejado del amarre si se confundiera el norte.
- Cambie la tolerancia (`--tolerancia 0.3`) y discuta qué hallazgos cambian y por qué.

## Errores frecuentes

- Usar alturas elipsoidales en unos datos y ortométricas en otros.
- Mezclar coordenadas de antes y después de un terremoto sin declarar la época.
- Georreferenciar el modelo estructural y la fotogrametría con redes de puntos distintas.
- Descartar un hallazgo porque "no cae en ningún elemento".
- Olvidar que el modelo trabaja con ejes y los daños están en las caras.

## Autoevaluación

1. Todos los hallazgos aparecen 30 m más abajo que en la realidad. ¿Qué error sospecha?
2. ¿Por qué un hallazgo puede quedar lejos de todo elemento del modelo sin que haya error?
3. ¿Por qué conviene usar la misma red de puntos de control para la fotogrametría y para el modelo estructural?
4. ¿Cómo cambian la prioridad de una fisura la relación D/C del elemento y la deriva del piso?

## Cómo explicar este módulo (guía del instructor)

**Idea central que el grupo debe llevarse:** un hallazgo bien ubicado se asigna a un elemento del modelo y se prioriza con la D/C y la deriva; si todos los hallazgos se desplazan lo mismo en vertical, el error está en las alturas.

**Preparación:**

- En cada computador: Python 3.10 o posterior, el repositorio del curso y Google Earth. Pruebe los dos comandos del laboratorio el día anterior en todos los equipos.
- Un esquema impreso del edificio de ejemplo con los ejes A-B-C y 1-2-3 y los nombres de los elementos.
- Un dibujo del elipsoide, el geoide y el terreno para explicar h, H y N.
- Un mapa de Chile con los husos UTM 18 y 19.

**Secuencia del módulo (120 min):**

| Min | Bloque | Qué hace el instructor | Qué hacen los participantes |
| --- | --- | --- | --- |
| 0-10 | Apertura | Muestra una fisura que, por un error de alturas, aparece 30 m bajo el terreno; pregunta qué pudo pasar | Proponen causas |
| 10-30 | 9.2 y 9.3 Marco y errores | Explica SIRGAS-Chile, los husos, el movimiento de la red después de un terremoto y los tres errores con dibujos | Ubican Santiago en el huso 19 y calculan cuánto se mueve un punto con 0.91° a 10 m |
| 30-40 | Paso 1 | Proyecta la salida y lee con el grupo el RMS y las derivas | Ejecutan la georreferencia y abren el KML |
| 40-55 | Paso 2 | Explica qué hace el script, paso por paso | Ejecutan el script y comparan con la salida esperada |
| 55-65 | Paso 3 | Pregunta por qué H05 no cae en un elemento | Discuten y concluyen que es un muro no modelado |
| 65-80 | Paso 4 | Pide ordenar los hallazgos por prioridad | Completan la tabla y justifican el orden |
| 80-95 | Paso 5 | Pide provocar el error de alturas | Ejecutan con N = 0 y explican el resultado |
| 95-110 | Paso 6 | Revisa las fichas | Completan las fichas de H01 y H06 |
| 110-120 | Cierre | Resume las señales de cada error | Responden la autoevaluación |

**Cómo explicar los puntos clave:**

- **h, H y N.** Dibuje tres líneas: el elipsoide (una superficie matemática lisa), el geoide (el nivel medio del mar prolongado bajo los continentes) y el terreno. El GNSS mide desde el elipsoide (h); los planos, desde el geoide (H); la separación entre ambos es N. Si se mezclan, todo se mueve N metros.
- **Chile se mueve.** Cuente que después del terremoto del Maule de 2010 hubo puntos de la red geodésica que se movieron metros. Una coordenada sin su época puede ser de "otro Chile".
- **Por qué 0.25 m en H01.** El modelo trabaja con el eje del pilar y la fisura está en la cara: la mitad de 50 cm. Muestre el esquema del pilar visto en planta.
- **El hallazgo sin elemento.** Insista en que H05 no es un error: los muros de relleno no siempre se modelan, pero su daño importa, y está en el piso más cercano al límite de deriva de la NCh 433.
- **La prioridad.** Pida que ordenen los hallazgos con tres criterios a la vez (severidad, D/C y deriva) y que defiendan el primero de la lista frente al grupo.

**Preguntas para la clase (con respuesta esperada):**

- "Todos los hallazgos aparecen 30 m más abajo. ¿Qué revisa primero?" El tipo de altura y la ondulación geoidal.
- "Si el error fuera en planta, ¿qué revisaría?" El huso UTM, el marco y su época, o el norte.
- "¿Qué hallazgo iría primero a verificación?" H06 o H01: fisuras en pilares esquineros del primer piso con D/C de 0.92 y 0.86.

**Dificultades frecuentes y cómo abordarlas:**

- Problemas de instalación: trabaje en parejas y deje un computador del instructor listo para proyectar los resultados.
- Ansiedad ante la consola: dicte los comandos, uno a la vez, y lea la salida en voz alta.
- Interpretar H05 como un error del programa: vuelva al esquema del edificio y muestre que el muro está entre los pilares, no sobre un elemento modelado.

**Verificación de cierre:** la tabla de prioridad completa y las fichas de H01 y H06, que pasan al informe del módulo 10.
