# Módulo 3. Equipos y sensores

**Duración:** 2 h (1.5 h de teoría y 0.5 h de práctica con los equipos) · **Competencia:** C3

Para inspeccionar se elige un multirrotor con cámara de sensor de 1" o mayor, obturador mecánico y zoom óptico, y una térmica radiométrica cuando la pregunta lo pide.

**Objetivos de aprendizaje.**

1. Elige el tipo de aeronave adecuado para cada estructura.
2. Lee la ficha técnica de una cámara y extrae los datos que necesita para planear (sensor, focal, píxeles, obturador).
3. Decide cuándo hace falta zoom, térmica, RTK o LiDAR.

## 3.1 Tipos de aeronave

| Tipo | Ventajas | Limitaciones | Uso en inspección |
| --- | --- | --- | --- |
| Multirrotor (4, 6 u 8 rotores) | Vuelo estacionario, se acerca a la superficie, despega en espacios pequeños | Autonomía de 20 a 45 min | El estándar para fachadas, cubiertas, puentes y torres |
| Multirrotor con jaula de protección | Tolera contactos; vuela en espacios confinados y sin GNSS | Menor autonomía, cámara con menos resolución, la jaula aparece en algunas fotos | Interiores de estanques, chimeneas, ductos, bajo tableros de puentes |
| Ala fija o VTOL | Gran autonomía y cobertura | No hace estacionario ni se acerca | Corredores y cartografía del entorno; poco útil para el detalle |
| Multirrotor pesado | Lleva LiDAR o varios sensores | Más riesgo y más requisitos de autorización | Levantamientos 3D de alta precisión |

Características que importan en inspección:

- **Gimbal con giro amplio:** que la cámara pueda mirar al frente, abajo y, para puentes, hacia arriba (cámara superior o gimbal con inclinación positiva).
- **Redundancia:** GNSS doble, IMU y brújula redundantes, aterrizaje de emergencia con batería baja.
- **Sensores de obstáculos:** ayudan, pero fallan ante vidrio, cables delgados, mallas y poca luz (módulo 5).
- **Iluminación auxiliar:** necesaria en espacios oscuros (bajo puentes, interiores).
- **Resistencia al agua y al polvo (IP):** amplía la ventana de operación, pero no autoriza a volar con lluvia si la autorización o el fabricante no lo permiten.
- **Desempeño en altura:** en faenas de la cordillera, a 3000 m, el aire es un 26 % menos denso que a nivel del mar; en Santiago (unos 560 m) la diferencia es de un 5 %. Los rotores rinden menos, la autonomía baja y el margen ante el viento se reduce. Use hélices de altitud si el fabricante las ofrece.

**Requisitos de la DAN 151 para la aeronave:** masa máxima de despegue de 9 kg, paracaídas de emergencia y registro en la DGAC (módulo 2). El equipo del curso se elige dentro de esos límites.

## 3.2 Cámaras RGB

Datos de la ficha técnica que se necesitan para planear:

| Dato | Para qué sirve | Ejemplo (cámara gran angular del curso) |
| --- | --- | --- |
| Ancho y alto del sensor (mm) | GSD y huella | 13.2 × 8.8 mm (sensor de 1") |
| Focal real (mm), no la equivalente a 35 mm | GSD y huella | 8.8 mm |
| Resolución (px) | GSD | 5472 × 3648 px (20 MP) |
| Tipo de obturador | Distorsión en movimiento | Mecánico |
| Exposición mínima, ISO, apertura | Nitidez | 1/2000 s, ISO 100-3200 |
|  |  |  |

- **Tamaño del sensor:** un sensor grande capta más luz y da imágenes más limpias en sombra (aleros, fondos de losa). Para inspección, mínimo 1".
- **Obturador mecánico frente a electrónico:** el obturador electrónico de la mayoría de estas cámaras (*rolling shutter*) lee el sensor por líneas, y con la aeronave en movimiento deforma la imagen. Para fotogrametría use obturador mecánico o fotografíe en estacionario.
- **Zoom óptico:** permite lograr un GSD fino desde más lejos, lo que aumenta la seguridad. La cámara gran angular necesita estar a 3.6 m para lograr 1 mm/px, mientras que el zoom a 40 mm logra 0.3 mm/px desde 7.5 m (módulo 4). El zoom digital no agrega información: no se usa para medir.
- **Focal fija o calibrada:** para fotogrametría, la focal no debe cambiar entre fotos de un mismo bloque.

**Cámaras de ejemplo del curso.** Son cámaras genéricas, no de un fabricante, con valores realistas, cargadas en la calculadora de misión:

| Clave | Sensor | Focal | Resolución |
| --- | --- | --- | --- |
| `gran_angular` | 1": 13.2 × 8.8 mm | 8.8 mm | 5472 × 3648 px |
| `zoom` | 1/2": 6.4 × 4.8 mm | 40 mm (se cambia con `--focal`) | 4000 × 3000 px |
| `termica` | Píxel de 12 µm: 7.68 × 6.14 mm | 13 mm | 640 × 512 px |

## 3.3 Cámaras térmicas

- **Radiométrica** (guarda la temperatura de cada píxel) frente a no radiométrica (solo imagen). Para inspección, siempre radiométrica: permite corregir la emisividad y medir diferencias de temperatura después del vuelo.
- **Resolución:** 640 × 512 px es lo usual en equipos profesionales; con menos resolución hay que volar más cerca.
- **Sensibilidad térmica (NETD):** la diferencia de temperatura más pequeña que distingue; 50 mK o menos es adecuado para edificaciones.
- **Cámara doble (RGB + térmica):** facilita interpretar, porque cada termograma tiene su foto visible de la misma vista.

## 3.4 Posicionamiento: GNSS, RTK y PPK

| Modo | Precisión típica de la posición de la cámara | Comentario |
| --- | --- | --- |
| GNSS autónomo | Metros | Suficiente para volar, no para georreferenciar con precisión |
| RTK (corrección en tiempo real desde una base o red) | Centímetros | Requiere enlace con la base durante el vuelo |
| PPK (corrección en posproceso) | Centímetros | No depende del enlace en vuelo; requiere datos de una base |

Cerca de fachadas altas y bajo puentes la señal GNSS se degrada: pocos satélites visibles y reflexiones en los muros. La posición RTK puede pasar de fija a flotante y empeorar a decímetros sin aviso evidente. Por eso, aun con RTK, el curso exige puntos de chequeo independientes (módulo 8).

## 3.5 Otros sensores

- **LiDAR aerotransportado:** nube de puntos directa; funciona con poca textura y atraviesa parcialmente la vegetación. Útil para geometría (desplomes, deformaciones de cubiertas grandes); no reemplaza la foto para ver fisuras.
- **Multiespectral:** pensado para vegetación; en estructuras su uso es marginal (por ejemplo, vegetación invasiva en cubiertas).
- **Sensores de contacto:** existen drones que apoyan un medidor de espesores por ultrasonido en estructuras de acero; son operaciones especializadas.

## 3.6 Accesorios y mantenimiento

- Baterías suficientes para la misión más un 50 % de reserva, con registro de ciclos de cada batería.
- Hélices de repuesto: una hélice con una muesca se cambia.
- Tarjetas de memoria rápidas, formateadas en la cámara antes de cada misión.
- Firmware actualizado antes del día de campo, nunca en el sitio; tras actualizar, un vuelo de prueba.
- Bitácora de mantenimiento por aeronave: horas, incidentes, cambios de piezas.

## Práctica (0.5 h)

Con los equipos del curso: identificar en la ficha técnica los datos de la tabla 3.2, revisar baterías y hélices, y configurar el formato de foto (RAW + JPEG), el modo de obturador y el guardado radiométrico de la térmica.

## Errores frecuentes

- Usar la focal equivalente a 35 mm en la fórmula del GSD: el resultado sale varias veces más fino de lo real.
- Fotografiar con zoom digital y creer que se ganó resolución.
- Confiar en la precisión RTK pegado a la fachada.
- Actualizar el firmware en el sitio y descubrir que cambió el comportamiento del RTH.

## Autoevaluación

1. ¿Por qué el obturador electrónico es un problema en fotogrametría?
2. Una cámara anuncia "24 mm equivalente". ¿Sirve ese dato para calcular el GSD? ¿Qué dato necesita?
3. ¿Qué ventaja de seguridad tiene una cámara con zoom óptico?
4. ¿Por qué hay que verificar la precisión del RTK cerca de una fachada alta?
