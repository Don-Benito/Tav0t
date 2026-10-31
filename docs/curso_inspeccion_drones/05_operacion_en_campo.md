# Módulo 5. Operación en campo cerca de estructuras

**Duración:** 7 h (1.5 h de teoría y 5.5 h de práctica) · **Competencia:** C5

Junto a una estructura la protección principal es la distancia (mínimo 5 m) y el observador, no los sensores del dron.

**Objetivos de aprendizaje.**

1. Prepara el sitio y ejecuta las listas de chequeo antes, durante y después del vuelo.
2. Reconoce y maneja los fenómenos propios del vuelo junto a estructuras: pérdida de GNSS, interferencia magnética, turbulencia, fallas de los sensores de obstáculos.
3. Ejecuta los procedimientos de emergencia del plan.
4. Controla la calidad de los datos antes de abandonar el sitio.

Las prácticas de vuelo las dirige un operador del curso con credencial RPAS vigente, dentro de una autorización de la DGAC y con el plan de misión aprobado. El participante sin credencial actúa como operador de cámara, observador o coordinador de sitio, o vuela en simulador.

## 5.1 Preparación del sitio

1. **Reconocimiento a pie** alrededor de la estructura: obstáculos (cables, antenas, árboles, grúas), personas, accesos, zonas de despegue y aterrizaje, fuentes de interferencia (subestaciones, antenas, estructuras de acero).
2. **Área de seguridad en tierra** bajo la zona de vuelo, con conos, cinta y vigías. Su tamaño depende de la altura de vuelo y del viento; como guía del curso, no menos que la altura de vuelo alrededor de la proyección de la ruta, y siempre sin personas ajenas a la operación a menos de 30 m horizontales, como exige la DAN 151.
3. **Punto de despegue** despejado, nivelado, lejos de acero, vehículos y tapas metálicas, con línea de vista a toda la ruta y una base de aterrizaje.
4. **Briefing** con todo el equipo: objetivo, ruta, roles, frases de comunicación, límites, emergencias, sitio alterno. Nadie despega sin briefing.

## 5.2 Comunicación en vuelo

Frases cortas y estandarizadas, repetidas por quien las recibe:

| Frase | Quién | Significado |
| --- | --- | --- |
| "Despegando" / "Aterrizando" | Piloto | Aviso a todo el equipo |
| "Área libre" / "Persona en el área" | Coordinador | Estado del área de seguridad |
| "Aeronave a las \[hora\]" | Observador | Tráfico tripulado; el piloto desciende |
| "Distancia" | Observador | El dron está más cerca de la estructura que el límite |
| "Foto" / "Repetir" | Operador de cámara | Captura o repetición de un punto |
| **"Alto"** | **Cualquiera** | **Se detiene la maniobra; se obedece sin discutir** |

## 5.3 Fenómenos del vuelo junto a estructuras

**GNSS degradado.** Junto a una fachada alta se ve la mitad del cielo y las señales rebotan en los muros (multitrayecto); bajo un puente no hay señal. La aeronave deriva lentamente aunque el control esté quieto, y la deriva puede ser hacia la fachada. El sistema puede pasar a modo de actitud (ATTI), sin posicionamiento: el dron no frena solo y se lo lleva el viento. El RTK pierde la solución fija.

- Mantenga la distancia mínima del curso, **5 m**, en vuelo con GNSS estable y viento bajo; más si hay ráfagas o la señal es pobre. Acercarse más solo con aeronaves con jaula diseñadas para contacto.
- **Ensayo de deriva:** a la distancia de trabajo, suelte los mandos 10 segundos y observe. Si deriva más de 1 m, aléjese.
- El piloto debe dominar el vuelo manual en ATTI (entrenado en simulador y en campo abierto) antes de volar junto a estructuras.
- Ante la pérdida de GNSS: alejarse de la estructura hacia el espacio abierto, ganar altura con cuidado y esperar la recuperación o aterrizar.

**Interferencia magnética.** El acero de las estructuras, la armadura de las losas, los vehículos y las instalaciones eléctricas desvían la brújula. Una brújula desviada hace que el dron no sepa hacia dónde mira y puede iniciar un vuelo en círculos crecientes.

- Calibre la brújula lejos de la estructura, solo si el sistema lo pide o cambió de sitio de forma importante.
- No despegue desde cubiertas metálicas, tapas, losas con mucha armadura expuesta ni junto a vehículos.
- Después de despegar, mantenga estacionario a unos 3 m y verifique que el rumbo del mapa coincide con el real antes de alejarse.

**Turbulencia y viento.** Hay remolinos a sotavento de la estructura y aceleración del viento en esquinas y bordes de cubierta; bajo puentes y en patios interiores el aire cambia de dirección sin aviso. Doble las esquinas lejos de la estructura, nunca pegado a ella.

**Sensores de obstáculos.** No ven bien el vidrio, los cables delgados, las mallas, las ramas finas ni los obstáculos con poca luz. Pueden impedir acercarse a la distancia de trabajo o frenar en medio de una pasada, y desactivarlos aumenta el riesgo: solo con la autorización del piloto al mando y en las maniobras planeadas. Nunca son la protección principal.

**Enlace de radio.** La estructura puede tapar la señal entre el control y el dron, sobre todo al pasar a la fachada opuesta. No vuele detrás de la estructura: cambie de posición de piloto para cada fachada.

## 5.4 Retorno automático (RTH) y fallas

- El RTH sube a la altura configurada y vuelve en línea recta. Junto a una fachada con balcones o voladizos, subir en vertical puede ser un choque.
- Antes de cada fachada, piense qué pasa si el RTH se dispara en ese punto. En algunos casos es mejor configurar la pérdida de enlace como estacionario o aterrizaje.
- La altura de RTH va por encima del obstáculo más alto del regreso.

## 5.5 Procedimientos de emergencia

| Situación | Acción inmediata |
| --- | --- |
| Pérdida de GNSS junto a la estructura | Alejarse hacia espacio abierto en ATTI, estabilizar, ganar altura con cuidado, esperar o aterrizar |
| Pérdida de enlace | Verificar el comportamiento configurado; mover la antena o la posición del piloto; avisar al equipo y vigilar la zona de regreso |
| Batería baja o falla de batería | Regreso inmediato o aterrizaje en el sitio seguro más cercano |
| Vuelo errático (brújula) | Alejarse de la estructura, cambiar a ATTI si el fabricante lo permite, aterrizar en zona despejada |
| Aeronave tripulada cerca | Descender y aterrizar; reportar si corresponde |
| Persona entra al área | "Alto": estacionario lejos de la persona o aterrizaje fuera de su vertical |
| Colisión o caída | Asegurar la zona, desconectar la batería si es seguro, vigilar humo o calor (bolsa ignífuga), fotografiar, registrar y reportar a la DGAC según la DAN 151 |
| Fuga (*fly-away*) | Intentar recuperar el control y el RTH; informar a la DGAC y al control de tránsito aéreo si se aleja del área |

Toda emergencia, aunque termine bien, se registra en la bitácora y se analiza al final del día.

## 5.6 Ejecución de la captura

1. **Vuelo de reconocimiento** alto y alejado: confirma obstáculos y toma fotos generales de contexto de cada fachada, que sirven después para ubicar cada foto de detalle.
2. **Cobertura sistemática** con la malla del plan, en modo automático si el software lo permite o manual con pasadas a distancia constante.
3. **Detalles** con zoom en estacionario, siguiendo la lista del plan y lo que el operador de cámara descubre en vivo.
4. Para cada detalle, una foto de contexto (que muestre dónde está) y una de detalle frontal. Cuando sea posible, incluya una referencia de tamaño (junta, ladrillo, ventana de dimensión conocida).

Nombre de los vuelos en la bitácora: `AAAAMMDD_estructura_fachada_vuelo`, por ejemplo `20261105_EdA_F1_V02`.

## 5.7 Control de calidad en sitio

Antes de recoger el equipo, en un computador portátil y no en la pantalla del control:

- [ ] Las fotos están nítidas al 100 % de ampliación (una muestra de cada pasada y todas las de detalle)
- [ ] La cobertura está completa: no faltan pasadas ni esquinas
- [ ] La exposición es correcta en sombras (aleros, fondos de losa)
- [ ] Los metadatos de posición están (EXIF/XMP) y, si hubo RTK, la solución fue fija
- [ ] Hay dos copias de los datos antes de formatear las tarjetas

Si algo falla, se repite en el sitio: volver otro día cuesta movilización, autorización y clima.

## Práctica (5.5 h)

1. **Simulador (1 h):** vuelo manual en ATTI, pasadas paralelas a un muro a distancia constante, recuperación ante pérdida de GNSS simulada.
2. **Chequeos y briefing (0.5 h):** cada grupo diligencia las listas del anexo A y hace el briefing.
3. **Vuelo de fachada (2 h):** ensayo de deriva, cobertura de un paño de fachada según el plan del módulo 4 y detalles con zoom, con rotación de roles.
4. **Fotos de detalle con zoom (1 h):** en estacionario, sobre la lista de detalles del plan, con foto de contexto y foto frontal de cada uno.
5. **Vuelo de cubierta (0.5 h):** malla nadir y órbita oblicua.
6. **Control de calidad y descarga (0.5 h).**

## Errores frecuentes

- Despegar desde la cubierta metálica "porque es más cerca".
- Confiar en que el sensor de obstáculos ve el vidrio.
- Volar la fachada opuesta sin cambiar de posición y perder el enlace.
- Revisar las fotos en la pantalla del control y descubrir en la oficina que estaban movidas.
- No registrar un incidente "porque no pasó nada".

## Autoevaluación

1. El dron deriva hacia la fachada con los mandos quietos. ¿Qué está pasando y qué hace?
2. ¿Por qué no se despega desde una losa con armadura expuesta?
3. ¿Qué riesgo tiene el RTH configurado a 30 m cuando el dron está junto a un balcón del piso 5?
4. Mencione cuatro verificaciones del control de calidad en sitio.

## Cómo explicar este módulo (guía del relator)

**Idea central que el grupo debe llevarse:** junto a una estructura el dron pierde sus ayudas (GNSS, brújula, sensores de obstáculos); lo que protege es la distancia, el observador y un equipo que se comunica con frases cortas y obedece el "Alto".

**Preparación:**

- Autorización de la DGAC vigente para el sitio de prácticas, permiso del propietario y área de seguridad diseñada.
- Pronóstico de viento y lluvia del día; plan B en simulador si se supera el límite.
- Teléfonos con una aplicación de GNSS y de brújula para las demostraciones.
- Tarjetas de emergencia para el simulacro (una por situación de la tabla 5.5).
- Listas de chequeo del anexo A impresas, radios, conos, cinta, chalecos y cascos.
- Un computador portátil por grupo para el control de calidad.

**Secuencia del módulo (420 min):**

| Min | Bloque | Qué hace el relator | Qué hacen los participantes |
| --- | --- | --- | --- |
| 0-15 | 5.1 Preparación del sitio | Recorre con el grupo un croquis del sitio de prácticas: obstáculos, despegue, alterno, área de seguridad con los 30 m de la DAN 151 | Marcan en el croquis cada elemento |
| 15-30 | 5.2 Comunicación | Hace un simulacro de voz con las frases de la tabla | Practican las frases en ronda; repiten cada orden recibida |
| 30-65 | 5.3 Fenómenos | Hace las demostraciones de GNSS junto a un muro y de brújula junto a acero; muestra un video de un sensor de obstáculos que no ve un cable | Leen en sus teléfonos la caída de satélites y el desvío de la brújula |
| 65-75 | 5.4 RTH | Plantea el experimento mental del RTH junto al balcón | Deciden la configuración ante pérdida de enlace para cada fachada |
| 75-90 | 5.5 Simulacro de emergencias | Saca tarjetas al azar en medio de una conversación | El grupo responde con la primera acción en menos de cinco segundos |
| 90-150 | Práctica: simulador | Supervisa el vuelo manual en ATTI y la recuperación ante pérdida de GNSS | Vuelan por turnos pasadas paralelas a un muro virtual |
| 150-180 | Práctica: chequeos y briefing | Exige las listas firmadas y escucha el briefing de cada grupo | Diligencian el anexo A y hacen el briefing |
| 180-300 | Práctica: vuelo de fachada | Coordina con el operador al mando (él mismo, si tiene credencial, o el operador invitado) y detiene la práctica ante cualquier desviación | Rotan roles: observador, operador de cámara, coordinador; hacen el ensayo de deriva, la cobertura y los detalles |
| 300-360 | Práctica: detalle con zoom | Revisa en vivo el encuadre y la nitidez de cada detalle | Fotografían la lista de detalles con foto de contexto y frontal |
| 360-390 | Práctica: cubierta | Dirige la malla nadir y la órbita | Rotan roles |
| 390-420 | Control de calidad y cierre | Revisa con cada grupo las fotos al 100 % en el portátil | Completan la lista 5.7, hacen dos copias y la revisión del día |

**Cómo explicar los puntos clave:**

- **GNSS degradado.** Pida a todos que miren en el teléfono el número de satélites en el patio y luego pegados a un muro alto: la caída se ve en segundos. Explique que el dron sufre lo mismo, y que la deriva hacia la fachada es la consecuencia.
- **Interferencia magnética.** Acerque un teléfono con la brújula abierta a una viga de acero o a una losa con armadura expuesta: la aguja se desvía. "Ahora imaginen que el dron cree que mira al norte y mira al este".
- **Ensayo de deriva.** En el campo, muestre el ensayo una vez a 6 m de la fachada: suelte los mandos 10 segundos y que el grupo mida cuánto se movió. Esa medida decide si se acerca o no.
- **RTH junto a voladizos.** Dibuje una fachada con balcones y el dron entre dos de ellos; pregunte qué pasa si pierde enlace y sube en vertical. La respuesta convence más que la regla.
- **Revisar en el portátil.** Muestre una foto que se ve nítida en la pantalla del control y movida al 100 % en el portátil. Es la mejor forma de que nadie vuelva a saltarse el paso.

**Reglas de seguridad de la práctica** (léalas en el briefing):

- El operador al mando es el relator, si tiene credencial RPAS vigente, o el operador invitado; puede tomar el control en cualquier momento.
- Nadie entra al área de seguridad sin autorización del coordinador.
- Cualquier persona puede decir "Alto" y se obedece sin discutir.
- Se suspende la práctica si el viento supera el límite del plan o si aparece una persona ajena dentro de los 30 m.
- Una falta grave reprueba el componente práctico (ver Evaluación).

**Preguntas para la clase (con respuesta esperada):**

- "¿Qué hace si el dron deriva hacia la fachada?" Se aleja hacia el espacio abierto, estabiliza y no se vuelve a acercar hasta que el ensayo de deriva sea aceptable.
- "¿Dónde se calibra la brújula?" Lejos de la estructura, el acero y los vehículos, y solo si el sistema lo pide.
- "¿Quién puede decir Alto?" Cualquier persona del equipo.

**Dificultades frecuentes y cómo abordarlas:**

- Exceso de confianza de quienes ya vuelan: asígneles primero el rol de observador; ver el vuelo desde afuera corrige la percepción de distancia.
- Frases improvisadas en vuelo: deténgase y pida repetir con la frase estándar.
- Prisa al final del día: el control de calidad es parte de la práctica y se evalúa.

**Verificación de cierre:** cada grupo entrega las listas firmadas, la bitácora y las fotos aceptadas en el control de calidad; en la revisión del día cada uno dice una cosa que cambiaría.
