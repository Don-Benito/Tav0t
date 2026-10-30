# Módulo 4. Planificación de la misión

**Duración:** 4 h (2 h teoría + 2 h taller de cálculo) · **Competencia:** C4

## Objetivos de aprendizaje

1. Calcula el GSD, la distancia de vuelo y la huella de la foto para un
   objetivo de inspección.
2. Diseña la malla de fotos de una fachada y la ruta de una cubierta, una
   torre y un puente.
3. Considera la luz, el viento, la nitidez y las contingencias en el plan.
4. Diligencia el plan de misión (anexo B).

Todos los ejemplos se pueden reproducir con
`ejemplos/curso_drones/calculadora_mision.py`.

---

## 4.1 Del objetivo a la resolución

La pregunta del encargo fija **el detalle más pequeño que hay que ver**. De ese
detalle sale la resolución necesaria, de la resolución sale la distancia, y de
la distancia salen la ruta, el número de fotos y el tiempo de vuelo.

| Objetivo de la inspección | Detalle que hay que ver | GSD orientativo |
|---|---|---|
| Inventario general, estado de cubierta | Elementos, manchas, encharcamientos | 5-20 mm/px |
| Desprendimientos, fisuras anchas, corrosión | Fisuras de varios mm, óxido, faltantes | 1-3 mm/px |
| Fisuras finas en concreto | Fisuras de décimas de mm | ≤ 0.5 mm/px (con zoom) |
| Pernos, soldaduras, uniones | Tuercas, cordones, grietas en uniones | ≤ 0.5 mm/px |
| Modelo 3D para geometría (desplomes) | Aristas y esquinas | 2-10 mm/px |

### Detectar no es medir

- **Detectar:** una fisura más delgada que un píxel a veces se ve, porque su
  sombra oscurece el píxel. Pero su ancho aparente es el de un píxel completo:
  la imagen **sobrestima** el ancho.
- **Medir:** para estimar el ancho con confianza, la fisura debe ocupar al
  menos **3 píxeles** a lo ancho (criterio del curso). El ancho medible
  mínimo es entonces 3 × GSD.
- Para fisuras de menos de 1 mm, lo realista es que el dron **detecte,
  localice y describa el patrón**, y que el ancho se mida con fisurómetro en
  una verificación de cerca. El informe lo dice así (confianza B, anexo B).

**Calibración en campo:** pegue una tarjeta comparadora de fisuras en un muro
de prueba y fotografíela a varias distancias con la cámara del proyecto. La
distancia a la que deja de distinguir la línea que le interesa es su límite
real, que depende del contraste, la luz y la nitidez, no solo del GSD.

## 4.2 Fórmulas

Con la cámara perpendicular a la superficie, a una distancia *D*:

```math
\text{GSD} = \frac{s_w \cdot D}{f \cdot N_w}
```

- *s<sub>w</sub>*: ancho del sensor (mm); *f*: focal **real** (mm);
  *N<sub>w</sub>*: ancho de la imagen (px). Con *D* en mm, el GSD sale en mm/px.

Despejando, la distancia para un GSD objetivo:

```math
D = \frac{\text{GSD} \cdot f \cdot N_w}{s_w}
```

Huella de la foto (área cubierta):

```math
A = \frac{s_w \cdot D}{f} \qquad H = \frac{s_h \cdot D}{f}
```

Separación entre fotos y entre pasadas para un solape frontal *p* y lateral *q*:

```math
\Delta_{\text{fotos}} = A\,(1 - p) \qquad \Delta_{\text{pasadas}} = H\,(1 - q)
```

**Efecto de la inclinación.** Si la cámara forma un ángulo θ con la normal a
la superficie, el píxel se alarga en la dirección de la inclinación en
aproximadamente 1 / cos θ: un 15 % a 30° y un 41 % a 45°. Para medir, la foto
debe ser lo más frontal posible.

**Nitidez en movimiento.** El desplazamiento de la imagen durante la
exposición, en píxeles, es:

```math
b = \frac{v \cdot t}{\text{GSD}}
```

con *v* la velocidad de la aeronave y *t* el tiempo de exposición. Se busca
*b* < 0.5 px.

## 4.3 Ejemplos resueltos

Cámaras del módulo 3. Comandos desde la raíz del repositorio.

### Ejemplo 1. ¿Qué GSD tengo a 6 m con la gran angular?

```bash
python ejemplos/curso_drones/calculadora_mision.py gsd --camara gran_angular --distancia 6
```

GSD = 13.2 × 6000 / (8.8 × 5472) = **1.64 mm/px**. Huella 9.00 × 6.00 m.
Ancho medible mínimo ≈ 4.9 mm. Sirve para desprendimientos, fisuras de varios
milímetros y corrosión; no para medir fisuras finas.

### Ejemplo 2. Quiero 1 mm/px con la gran angular

```bash
python ejemplos/curso_drones/calculadora_mision.py distancia --camara gran_angular --gsd 1
```

D = 1 × 8.8 × 5472 / 13.2 = **3.6 m**. Es demasiado cerca de una fachada para
la seguridad del curso (mínimo 5 m, módulo 5). Conclusión: **cambie de
cámara, no de distancia**.

### Ejemplo 3. El zoom a 40 mm desde 10 m

```bash
python ejemplos/curso_drones/calculadora_mision.py gsd --camara zoom --distancia 10
```

GSD = **0.40 mm/px** a 10 m, con una huella de solo 1.60 × 1.20 m. Para
0.3 mm/px bastan 7.5 m (`distancia --camara zoom --gsd 0.3`). El zoom da
detalle con distancia de seguridad, pero cada foto cubre poco.

### Ejemplo 4. Malla de fotos de una fachada de 30 × 24 m

Fachada de 8 pisos, 30 m de ancho y 24 m de alto, gran angular a 6 m, solape
frontal 80 % y lateral 70 %:

```bash
python ejemplos/curso_drones/calculadora_mision.py fachada --camara gran_angular --ancho 30 --alto 24 --distancia 6
```

| Resultado | Valor |
|---|---|
| GSD | 1.64 mm/px |
| Huella | 9.00 × 6.00 m |
| Foto cada | 9.00 × (1 − 0.8) = 1.80 m |
| Pasada cada | 6.00 × (1 − 0.7) = 1.80 m |
| Fotos por pasada | ⌈30 / 1.80⌉ + 1 = 18 |
| Pasadas | ⌈24 / 1.80⌉ + 1 = 15 |
| **Total** | **270 fotos** |

Los centros de las fotos van de borde a borde de la fachada para que los
bordes tengan el mismo solape que el centro.

Si la misma fachada se quisiera cubrir entera con el zoom a 10 m, saldrían
6460 fotos (`fachada --camara zoom --ancho 30 --alto 24 --distancia 10`):
inviable. **Estrategia del curso: cobertura completa con la gran angular y
fotos de detalle con zoom donde la cobertura muestra algo o donde el modelo
estructural indica elementos críticos.**

### Ejemplo 5. Nitidez

Con GSD de 1.64 mm/px y la aeronave a 1 m/s:

| Exposición | Desplazamiento | En píxeles | ¿Aceptable? |
|---|---|---|---|
| 1/500 s | 2.0 mm | 1.2 px | No |
| 1/1000 s | 1.0 mm | 0.6 px | Límite |
| 1/2000 s | 0.5 mm | 0.3 px | Sí |

Con el zoom (0.4 mm/px) el problema es 4 veces mayor: las fotos de detalle se
toman **en estacionario**, y con la aeronave estabilizada.

### Ejemplo 6. Densidad del aire en Bogotá

```bash
python ejemplos/curso_drones/calculadora_mision.py densidad --altitud 2600
```

0.947 kg/m³, un 23 % menos que a nivel del mar. Planee menos autonomía y más
margen de viento que lo que dice la ficha técnica.

## 4.4 Patrones de vuelo

| Estructura | Patrón | Notas |
|---|---|---|
| **Fachada** | Pasadas horizontales (o verticales) paralelas a la fachada, cámara frontal | Pasadas verticales: más fáciles de mantener a distancia constante. Agregue fotos oblicuas (±30°) en esquinas, balcones y cornisas para el modelo 3D |
| **Cubierta plana** | Malla con cámara nadir (hacia abajo) + una órbita oblicua (45°) alrededor del borde | Solapes 75-80 % / 65-70 % |
| **Cubierta inclinada o compleja** | Malla nadir + pasadas oblicuas por cada agua | Mire canales, limahoyas, encuentros con muros y chimeneas |
| **Torre, chimenea, pila** | Columnas verticales por cara, o espiral descendente a distancia constante | En torres de telecomunicaciones considere las antenas (interferencia y exposición a RF) |
| **Puente** | Pasadas laterales a cada lado + pasadas bajo el tablero con cámara hacia arriba | Bajo el tablero no hay GNSS: vuelo manual o con posicionamiento visual |
| **Detalle** | Puntos de interés en estacionario con zoom | Lista de puntos tomada de la cobertura y del modelo estructural |

### Prioridades de detalle desde el modelo estructural

Antes de volar, revise los resultados del análisis en Tav0t: los elementos con
mayor relación demanda/capacidad y los pisos con mayor deriva. En el edificio
de ejemplo, la columna `C1-11` (planta baja, interior) tiene D/C = 1.00 y las
columnas de planta baja tienen las relaciones más altas de su tipo. Si son
visibles desde el exterior, van a la lista de detalle; si no lo son, el
informe dice que no se pudieron ver.

## 4.5 Luz y meteorología

### Luz

- **Cielo nublado uniforme:** la mejor luz para ver fisuras, sin sombras
  duras. El sol rasante resalta relieves, pero la sombra de un alero puede
  ocultar media fachada.
- **Contraluz:** evítelo; planee la hora según la orientación de cada
  fachada. En latitudes tropicales (Bogotá, 4.6° N) el sol pasa casi por el
  cenit: las fachadas este reciben sol en la mañana y las oeste en la tarde, y
  las fachadas norte reciben sol aproximadamente de mediados de abril a
  finales de agosto (el sol pasa al norte del cenit) y las sur el resto del
  año.
- **Exposición:** compense para el elemento, no para el cielo. Use RAW cuando
  vaya a recuperar sombras.

### Viento

- Respete el límite del fabricante **y** el del plan de misión, que debe ser
  más bajo cerca de estructuras. El viento a la altura de la cubierta es mayor
  que en la calle.
- Los edificios aceleran el viento en esquinas, bordes de cubierta y entre
  edificios cercanos, y generan remolinos a sotavento. No se acerque a una
  esquina en un día con ráfagas.
- Mida el viento en sitio antes de despegar y vigílelo durante el vuelo.

### Lluvia y humedad

- No se vuela con lluvia (salvo equipo y autorización que lo permitan) y las
  superficies mojadas cambian el aspecto de las fisuras y anulan la
  termografía.
- Para termografía hay condiciones propias (módulo 7).

## 4.6 Tiempo, baterías y contingencias

- **Tiempo de captura:** en estacionario cuente unos 3 s por foto. Las 270 fotos
  del ejemplo 4 son unos 14 minutos de captura, más los traslados entre
  pasadas.
- **Baterías:** planee cada vuelo para aterrizar con al menos 25-30 % de carga
  (más en frío y en altura) y lleve un 50 % de baterías de reserva.
- **Punto de despegue y aterrizaje:** despejado, con buena vista del área de
  vuelo, lejos de acero y de equipos que interfieran la brújula.
- **Aterrizaje alterno:** al menos un sitio alterno conocido por todo el
  equipo.
- **Altura de RTH:** por encima del obstáculo más alto del recorrido de
  regreso, y revisada contra balcones y voladizos si el RTH se dispara junto
  a la fachada (módulo 5).
- **Pérdida de enlace:** comportamiento configurado (RTH, estacionario o
  aterrizaje) según el sitio.

## 4.7 El plan de misión

El plan se escribe en el formato del [anexo B](anexos/B_formatos.md#1-plan-de-misión)
e incluye: objetivo y pregunta, estructura y entorno, autorización y
restricciones del espacio aéreo, equipo y sensores, GSD objetivo y distancia,
ruta y patrones, lista de detalles prioritarios, horario y meteorología
esperada, límites (viento, batería, distancia), roles, matriz de riesgos,
procedimientos de emergencia y criterio de aceptación de los datos.

---

## Taller (2 h)

Para el caso conductor:

1. Defina el detalle más pequeño que tiene que ver y el GSD objetivo.
2. Calcule distancia, huella y malla de fotos para cada fachada y la cubierta.
3. Defina la estrategia cobertura + detalle y la lista de detalles
   prioritarios con ayuda del modelo estructural.
4. Elija el horario por fachada según la luz.
5. Diligencie el plan de misión. Se califica (20 % de la nota).

## Errores frecuentes

- Elegir la distancia por comodidad y descubrir después que el GSD no
  alcanza.
- Usar la focal equivalente en la fórmula.
- Volar en movimiento con el zoom: fotos movidas que parecen buenas en la
  pantalla del control.
- Planear la fachada oeste en la mañana (contraluz y sombra).
- RTH por defecto a 30 m junto a un edificio de 40 m.

## Autoevaluación

1. Calcule el GSD de la cámara gran angular a 10 m y el ancho mínimo medible.
2. ¿A qué distancia debe estar la cámara zoom (40 mm) para lograr 0.5 mm/px?
3. ¿Cuántas fotos necesita una fachada de 12 × 10 m con la gran angular a 6 m
   y solapes 80/70?
4. ¿Por qué no se cubre una fachada completa con el zoom?
5. Con GSD de 0.4 mm/px y 1/1000 s, ¿a qué velocidad máxima puede moverse
   el dron para que el desplazamiento sea menor de 0.5 px?

Respuestas en el [anexo C](anexos/C_evaluacion.md#1-respuestas-de-las-autoevaluaciones).
