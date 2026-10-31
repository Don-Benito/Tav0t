# Módulo 3. Equipos y sensores

**Duración:** 2 h (1.5 h de teoría y 0.5 h de práctica con los equipos) · **Competencia:** C3

Para inspeccionar se elige un multirrotor con cámara de sensor de 1" o mayor, obturador mecánico y zoom óptico; el curso trabaja solo con cámara RGB.

**Objetivos de aprendizaje.**

1. Elige el tipo de aeronave adecuado para cada estructura.
2. Lee la ficha técnica de una cámara y extrae los datos que necesita para planear (sensor, focal, píxeles, obturador).
3. Decide cuándo hace falta zoom óptico, RTK o LiDAR.

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

## 3.3 Posicionamiento: GNSS, RTK y PPK

| Modo | Precisión típica de la posición de la cámara | Comentario |
| --- | --- | --- |
| GNSS autónomo | Metros | Suficiente para volar, no para georreferenciar con precisión |
| RTK (corrección en tiempo real desde una base o red) | Centímetros | Requiere enlace con la base durante el vuelo |
| PPK (corrección en posproceso) | Centímetros | No depende del enlace en vuelo; requiere datos de una base |

Cerca de fachadas altas y bajo puentes la señal GNSS se degrada: pocos satélites visibles y reflexiones en los muros. La posición RTK puede pasar de fija a flotante y empeorar a decímetros sin aviso evidente. Por eso, aun con RTK, el curso exige puntos de chequeo independientes (módulo 7).

## 3.4 Otros sensores

- **LiDAR aerotransportado:** nube de puntos directa; funciona con poca textura y atraviesa parcialmente la vegetación. Útil para geometría (desplomes, deformaciones de cubiertas grandes); no reemplaza la foto para ver fisuras.
- **Multiespectral:** pensado para vegetación; en estructuras su uso es marginal (por ejemplo, vegetación invasiva en cubiertas).
- **Sensores de contacto:** existen drones que apoyan un medidor de espesores por ultrasonido en estructuras de acero; son operaciones especializadas.

## 3.5 Accesorios y mantenimiento

- Baterías suficientes para la misión más un 50 % de reserva, con registro de ciclos de cada batería.
- Hélices de repuesto: una hélice con una muesca se cambia.
- Tarjetas de memoria rápidas, formateadas en la cámara antes de cada misión.
- Firmware actualizado antes del día de campo, nunca en el sitio; tras actualizar, un vuelo de prueba.
- Bitácora de mantenimiento por aeronave: horas, incidentes, cambios de piezas.

## Práctica (0.5 h)

Con los equipos del curso: identificar en la ficha técnica los datos de la tabla 3.2, revisar baterías y hélices, y configurar el formato de foto (RAW + JPEG), el modo de obturador y el enfoque.

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

## Cómo explicar este módulo (guía del relator)

**Idea central que el grupo debe llevarse:** el equipo se elige por la pregunta de la inspección y dentro de los límites de la DAN 151; de la ficha técnica solo importan unos pocos datos, y hay que saber leerlos.

**Preparación:**

- Los drones del curso (o fotos de un multirrotor, uno con jaula y un ala fija) y el módulo de paracaídas.
- La ficha técnica impresa de la cámara del curso, con la focal real y la equivalente.
- Un teléfono con una aplicación que muestre los satélites GNSS.
- Un ventilador pequeño para la demostración del obturador.

**Secuencia de la clase (120 min):**

| Min | Bloque | Qué hace el relator | Qué hacen los participantes |
| --- | --- | --- | --- |
| 0-10 | Apertura | Pone sobre la mesa tres equipos (o sus fotos) y pregunta cuál usarían para una fachada, el interior de un estanque y un canal de 5 km | Eligen y justifican |
| 10-35 | 3.1 Aeronaves | Explica los tipos y muestra el paracaídas; relaciona la masa de 9 kg y el paracaídas con la DAN 151 | Revisan el equipo y su placa de registro |
| 35-60 | 3.2 Cámaras | Proyecta la ficha técnica; hace la demostración del obturador y la del zoom digital | Subrayan sensor, focal real y píxeles; calculan un GSD con cada focal |
| 60-70 | 3.2 Zoom en terreno | Muestra con el zoom óptico una fisura del patio desde 10 m y la misma con la gran angular desde 3 m | Comparan detalle y distancia de seguridad |
| 70-85 | 3.3 GNSS, RTK y PPK | Compara en la aplicación los satélites junto a un muro y en un patio abierto | Leen la cantidad de satélites y la precisión |
| 85-90 | 3.4 y 3.5 | Repasa LiDAR, accesorios y mantenimiento | Preguntan |
| 90-120 | Práctica | Supervisa la configuración | Configuran RAW + JPEG, obturador y enfoque; revisan baterías y hélices |

**Cómo explicar los puntos clave:**

- **Focal real frente a equivalente.** Pida que calculen el GSD de la cámara del curso con 8.8 mm (real) y con 24 mm (equivalente). La segunda cifra da un GSD casi tres veces más fino: así descubren solos por qué la equivalente no sirve.
- **Obturador por líneas.** Fotografíe con un teléfono el ventilador encendido: las aspas salen curvas. Explique que el sensor se lee por líneas y que, si la aeronave se mueve, la fachada se deforma igual que las aspas.
- **Zoom óptico frente a digital.** Muestre la misma fisura con zoom óptico y con un recorte de la foto gran angular ampliado: en el recorte no aparece información nueva, solo píxeles más grandes.
- **RTK fijo frente a flotante.** Analogía: la solución fija es como medir con la huincha bien estirada; la flotante, con la huincha suelta. Junto a un muro alto la huincha se suelta sin avisar; por eso se chequea con puntos independientes.
- **Altura y densidad.** Si el curso se dicta en una faena de cordillera, muestre que la autonomía real es menor que la de la ficha (aire un 26 % menos denso a 3000 m).

**Preguntas para la clase (con respuesta esperada):**

- "¿Qué tres datos de la ficha necesito para planear?" Ancho del sensor, focal real y resolución en píxeles.
- "¿Qué gano con el zoom óptico?" El mismo GSD desde más lejos, es decir, más distancia de seguridad a la fachada.
- "¿Qué exige la DAN 151 a la aeronave?" Hasta 9 kg, paracaídas de emergencia y registro en la DGAC.

**Dificultades frecuentes y cómo abordarlas:**

- Fascinación por los equipos más caros: vuelva a la pregunta de la inspección; un equipo sobredimensionado también suma riesgo y requisitos.
- Confusión entre GSD y resolución en megapíxeles: aclare que dos cámaras de 20 MP pueden dar GSD muy distintos según el sensor y la focal.

**Verificación de cierre:** cada participante entrega la ficha de la cámara del caso conductor con los tres datos subrayados y el GSD a 6 m calculado a mano.
