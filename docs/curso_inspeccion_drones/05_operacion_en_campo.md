# Módulo 5. Operación en campo cerca de estructuras

**Duración:** 6 h (1.5 h teoría + 4.5 h práctica) · **Competencia:** C5

## Objetivos de aprendizaje

1. Prepara el sitio y ejecuta las listas de chequeo antes, durante y después
   del vuelo.
2. Reconoce y maneja los fenómenos propios del vuelo junto a estructuras:
   pérdida de GNSS, interferencia magnética, turbulencia, fallas de los
   sensores de obstáculos.
3. Ejecuta los procedimientos de emergencia del plan.
4. Controla la calidad de los datos antes de abandonar el sitio.

> Las prácticas de vuelo las dirige un piloto certificado del curso, dentro
> de una autorización vigente y con el plan de misión aprobado. El
> participante sin certificado actúa como operador de cámara, observador o
> coordinador de sitio, o vuela en simulador.

---

## 5.1 Preparación del sitio

1. **Reconocimiento a pie** alrededor de la estructura: obstáculos (cables,
   antenas, árboles, grúas), personas, accesos, zonas de despegue y
   aterrizaje, fuentes de interferencia (subestaciones, antenas, estructuras
   de acero).
2. **Área de seguridad en tierra** bajo la zona de vuelo: conos, cinta y
   vigías. Su tamaño depende de la altura de vuelo y del viento; como guía
   del curso, no menos que la altura de vuelo alrededor de la proyección de la
   ruta.
3. **Punto de despegue** despejado, nivelado, lejos de acero, vehículos y
   tapas metálicas, con línea de vista a toda la ruta. Use una base de
   aterrizaje.
4. **Briefing** con todo el equipo: objetivo, ruta, roles, frases de
   comunicación, límites, emergencias, sitio alterno. Nadie despega sin
   briefing.

## 5.2 Comunicación en vuelo

Frases cortas y estandarizadas, repetidas por quien las recibe:

| Frase | Quién | Significado |
|---|---|---|
| "Despegando" / "Aterrizando" | Piloto | Aviso a todo el equipo |
| "Área libre" / "Persona en el área" | Coordinador | Estado del área de seguridad |
| "Aeronave a las [hora]" | Observador | Tráfico tripulado; el piloto desciende |
| "Distancia" | Observador | El dron está más cerca de la estructura que el límite |
| "Foto" / "Repetir" | Operador de cámara | Captura o repetición de un punto |
| **"Alto"** | **Cualquiera** | **Se detiene la maniobra. Se obedece sin discutir.** |

## 5.3 Fenómenos del vuelo junto a estructuras

### GNSS degradado

Junto a una fachada alta se ve la mitad del cielo, y las señales rebotan en
los muros (multitrayecto). Bajo un puente no hay señal. Efectos:

- La aeronave **deriva** lentamente aunque el control esté quieto. La deriva
  puede ser **hacia la fachada**.
- El sistema puede pasar a modo de actitud (ATTI) sin posicionamiento: el dron
  no frena solo y se lo lleva el viento.
- El RTK pierde la solución fija.

Qué hacer:

- **Mantenga la distancia mínima del curso: 5 m** en vuelo con GNSS estable y
  viento bajo; más si hay ráfagas o la señal es pobre. Acercarse más solo con
  aeronaves con jaula diseñadas para contacto.
- Haga un **ensayo de deriva**: a la distancia de trabajo, suelte los mandos
  10 segundos y observe. Si deriva más de 1 m, aléjese.
- El piloto debe dominar el **vuelo manual en ATTI** (entrenado en simulador
  y en campo abierto) antes de volar junto a estructuras.
- Ante la pérdida de GNSS: alejarse de la estructura en dirección al espacio
  abierto, ganar altura con cuidado y esperar la recuperación o aterrizar.

### Interferencia magnética

El acero de las estructuras, el refuerzo de las losas, los vehículos y las
instalaciones eléctricas desvían la brújula. Una brújula desviada hace que el
dron "no sepa hacia dónde mira" y puede iniciar un vuelo en círculos
crecientes (*toilet bowl*).

- Calibre la brújula **lejos** de la estructura, solo si el sistema lo pide o
  cambió de sitio de forma importante.
- No despegue desde cubiertas metálicas, tapas, losas con mucho acero
  expuesto ni junto a vehículos.
- Después de despegar, mantenga estacionario a unos 3 m y verifique que el
  rumbo del mapa coincide con el real antes de alejarse.

### Turbulencia y viento

- Remolinos a sotavento de la estructura y aceleración del viento en esquinas
  y bordes de cubierta (módulo 4).
- Bajo puentes y en patios interiores el aire cambia de dirección sin aviso.
- Doble las esquinas lejos de la estructura, nunca pegado a ella.

### Sensores de obstáculos

- No ven bien el **vidrio**, los **cables delgados**, las mallas, las ramas
  finas ni los obstáculos en **poca luz**.
- Pueden impedir acercarse a la distancia de trabajo o frenar en medio de una
  pasada. Desactivarlos aumenta el riesgo: solo con la autorización del piloto
  al mando y en las maniobras planeadas.
- **Nunca son la protección principal.** La protección es la distancia y el
  observador.

### Enlace de radio

La estructura puede tapar la señal entre el control y el dron, sobre todo al
pasar a la fachada opuesta. **No vuele detrás de la estructura**: cambie de
posición de piloto para cada fachada.

## 5.4 Retorno automático (RTH) y fallas

- El RTH sube a la **altura configurada** y vuelve en línea recta. Junto a una
  fachada con balcones o voladizos, subir en vertical puede ser un choque.
- Antes de cada fachada, piense qué pasa si el RTH se dispara **en ese
  punto**. En algunos casos es mejor configurar la pérdida de enlace como
  estacionario o aterrizaje.
- Altura de RTH por encima del obstáculo más alto del regreso.

## 5.5 Procedimientos de emergencia

| Situación | Acción inmediata |
|---|---|
| Pérdida de GNSS junto a la estructura | Alejarse hacia espacio abierto en ATTI, estabilizar, ganar altura con cuidado, esperar o aterrizar |
| Pérdida de enlace | Verificar el comportamiento configurado; mover la antena o la posición del piloto; avisar al equipo y vigilar la zona de regreso |
| Batería baja o falla de batería | Regreso inmediato o aterrizaje en el sitio seguro más cercano |
| Vuelo errático (brújula) | Alejarse de la estructura, cambiar a ATTI si el fabricante lo permite, aterrizar en zona despejada |
| Aeronave tripulada cerca | Descender y aterrizar; reportar si corresponde |
| Persona entra al área | "Alto": estacionario lejos de la persona o aterrizaje fuera de su vertical |
| Colisión o caída | Asegurar la zona, desconectar la batería si es seguro, vigilar humo o calor de la batería (bolsa ignífuga), fotografiar, registrar, reportar según la norma |
| Fuga (*fly-away*) | Intentar recuperar control y RTH; informar a la autoridad y al control de tránsito aéreo si se aleja del área |

Toda emergencia, aunque termine bien, se registra en la bitácora y se
analiza al final del día.

## 5.6 Ejecución de la captura

1. **Vuelo de reconocimiento** alto y alejado: confirma obstáculos y toma
   fotos generales de contexto de cada fachada (sirven para ubicar después
   cada foto de detalle).
2. **Cobertura sistemática** con la malla del plan, en modo automático si el
   software lo permite o manual con pasadas a distancia constante.
3. **Detalles** con zoom en estacionario, siguiendo la lista del plan y lo que
   el operador de cámara descubre en vivo.
4. Para cada detalle, **una foto de contexto** (que muestre dónde está) y
   **una de detalle frontal**. Cuando sea posible, incluya una referencia de
   tamaño (junta, ladrillo, ventana de dimensión conocida).
5. Fotos térmicas en la ventana horaria del módulo 7.

Nombre de los vuelos en la bitácora: `AAAAMMDD_estructura_fachada_vuelo` (por
ejemplo `20261105_EdA_F1_V02`).

## 5.7 Control de calidad en sitio

Antes de recoger el equipo, en un computador portátil y no en la pantalla del
control:

- [ ] Las fotos están nítidas al 100 % de ampliación (revise una muestra de
      cada pasada y **todas** las de detalle).
- [ ] La cobertura está completa: no faltan pasadas ni esquinas.
- [ ] La exposición es correcta en sombras (aleros, fondos de losa).
- [ ] Los metadatos de posición están (EXIF/XMP) y, si hubo RTK, la solución
      fue fija.
- [ ] Las térmicas son radiométricas y tienen su par visible.
- [ ] Hay **dos copias** de los datos antes de formatear las tarjetas.

Si algo falla, se repite en el sitio. Volver otro día cuesta movilización,
autorización y clima.

---

## Práctica (4.5 h)

1. **Simulador** (1 h): vuelo manual en ATTI, pasadas paralelas a un muro a
   distancia constante, recuperación ante pérdida de GNSS simulada.
2. **Chequeos y briefing** (0.5 h): cada grupo diligencia las listas del
   anexo A y hace el briefing.
3. **Vuelo de fachada** (2 h): ensayo de deriva, cobertura de un paño de
   fachada según el plan del módulo 4 y detalles con zoom. Rotación de roles.
4. **Vuelo de cubierta** (0.5 h): malla nadir y órbita oblicua.
5. **Control de calidad y descarga** (0.5 h).

## Errores frecuentes

- Despegar desde la cubierta metálica "porque es más cerca".
- Confiar en que el sensor de obstáculos ve el vidrio.
- Volar la fachada opuesta sin cambiar de posición y perder el enlace.
- Revisar las fotos en la pantalla del control y descubrir en la oficina que
  estaban movidas.
- No registrar un incidente "porque no pasó nada".

## Autoevaluación

1. El dron deriva hacia la fachada con los mandos quietos. ¿Qué está pasando y
   qué hace?
2. ¿Por qué no se despega desde una losa con acero expuesto?
3. ¿Qué riesgo tiene el RTH configurado a 30 m cuando el dron está junto a un
   balcón del piso 5?
4. Mencione cuatro verificaciones del control de calidad en sitio.

Respuestas en el [anexo C](anexos/C_evaluacion.md#1-respuestas-de-las-autoevaluaciones).
