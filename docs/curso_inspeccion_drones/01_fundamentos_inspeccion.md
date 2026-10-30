# Módulo 1. Fundamentos de la inspección de estructuras con drones

**Duración:** 2 h de teoría · **Competencia:** C1

El dron lleva la cámara a donde el inspector no llega fácil, rápido o seguro; detecta, prioriza y documenta, pero el diagnóstico se confirma de cerca o con ensayos.

**Objetivos de aprendizaje.** Al terminar el módulo, el participante:

1. Explica para qué se inspecciona una estructura y qué tipos de inspección existen.
2. Identifica en qué partes de una inspección aporta un dron y en cuáles no.
3. Describe el flujo completo de una inspección con dron, desde el encargo hasta el informe.

## 1.1 Para qué se inspecciona una estructura

Una inspección busca evidencia del estado actual de una estructura para decidir algo: seguir usándola, mantenerla, repararla, reforzarla, restringir su uso o estudiarla más a fondo. Toda inspección parte de una pregunta; sin pregunta, el resultado es un álbum de fotos.

| Tipo de inspección | Pregunta que responde | Ejemplo |
| --- | --- | --- |
| Inicial o de inventario | ¿Qué hay y en qué estado está? | Línea base de un edificio recién adquirido |
| Rutinaria (periódica) | ¿Qué cambió desde la última vez? | Revisión anual de fachadas y cubiertas |
| Especial o de diagnóstico | ¿Qué causa este daño y qué tan grave es? | Fisuras en vigas tras una remodelación |
| Posevento | ¿Es seguro ocupar o usar la estructura? | Después de un sismo, incendio, inundación o impacto |
| De recibo o de obra | ¿Se construyó como se diseñó? | Control de avance o de calidad de fachadas |

## 1.2 Qué aporta un dron y qué no

| Aporta | No aporta (o aporta poco) |
| --- | --- |
| Acceso a fachadas, cubiertas, aleros, torres, chimeneas y tableros de puentes sin andamios, alzahombres ni trabajo en altura | Contacto: no percute, no toca, no raspa, no mide espesores ni durezas |
| Cobertura completa y sistemática: cada metro cuadrado queda registrado | Ver dentro del material: corrosión de la armadura sin manifestación externa, vacíos internos |
| Registro objetivo y repetible, que se puede volver a mirar y comparar en el tiempo | Ensayos: núcleos, esclerometría, ultrasonido, carbonatación, cloruros |
| Modelos 3D y ortomosaicos medibles | Juicio estructural: la imagen no dice si el elemento es suficiente |
| Termografía de grandes superficies | Zonas sin línea de vista: detrás de equipos, interiores cerrados, juntas ocultas |
| Rapidez en emergencias y en zonas de riesgo para personas | Operación con lluvia, viento fuerte o sin autorización de vuelo |

La regla del curso: **el dron detecta, prioriza y documenta; el diagnóstico se confirma con la inspección de cerca o con ensayos cuando el hallazgo lo amerita.** El informe debe decir con claridad qué se observó desde el aire y qué falta verificar (módulo 10).

**Beneficios y costos frente a la inspección tradicional:**

- **Seguridad:** reduce el trabajo en altura y la exposición en zonas dañadas, pero introduce un riesgo nuevo, la caída de la aeronave, que se gestiona en el módulo 2.
- **Tiempo:** una fachada de 30 × 24 m se fotografía completa en menos de una hora de vuelo (módulo 4). Procesar y revisar las fotos puede tardar más que el vuelo, y hay que presupuestarlo.
- **Costo:** evita andamios, canastas y cierres prolongados, pero exige personal certificado, autorización, seguros y equipo.
- **Datos:** genera cientos o miles de fotos por estructura. Sin un método de nombres, respaldo y revisión (módulo 10), la información se pierde.

## 1.3 Estructuras que se inspeccionan con dron

- **Edificaciones:** fachadas (enchapes, albañilería, muros cortina, balcones, cornisas), techumbres (losas, membranas, tejas, cubiertas livianas, canaletas y bajadas de aguas lluvias), elementos de hormigón o acero expuestos, juntas de dilatación sísmica, estanques elevados.
- **Puentes:** tablero, vigas, apoyos, juntas de expansión, pilas, estribos, cables y pendolones. Requieren cámara que mire hacia arriba o un dron con cámara superior, y vuelo sin GNSS bajo el tablero.
- **Estructuras industriales y de servicios:** torres de telecomunicaciones y de transmisión, chimeneas, silos, estanques, galpones industriales, estadios.
- **Patrimonio:** registro sin contacto de fachadas y cubiertas históricas.

## 1.4 Flujo de una inspección con dron

```mermaid
flowchart LR
    A[Encargo] --> B[Información<br/>previa]
    B --> C[Plan de<br/>misión]
    C --> D[Vuelo y<br/>captura]
    D --> E[Control de<br/>calidad]
    E -->|faltan datos: se vuelve a volar| D
    E -->|datos completos| F[Procesamiento]
    F --> G[Lectura de<br/>daños]
    G --> H[Ubicación en<br/>el modelo]
    H --> I[Informe]
```

El control de calidad en sitio es la única vuelta atrás barata del flujo: si falta algo, se vuela de nuevo antes de recoger el equipo.

1. **Encargo:** quién pide la inspección, para qué, con qué alcance y qué entregables. Se fija la pregunta.
2. **Información previa:** planos, modelo estructural, inspecciones anteriores, reparaciones, eventos (sismos, impactos). Del modelo se toman los elementos más exigidos (relación demanda/capacidad y derivas): son los primeros que hay que mirar.
3. **Plan de misión:** qué se fotografía, con qué sensor, a qué resolución, por qué ruta, con qué riesgos y qué permisos (módulos 2 y 4).
4. **Vuelo y captura** (módulo 5).
5. **Control de calidad en sitio:** antes de recoger el equipo se revisa que las fotos estén nítidas y que no falten zonas. Si falta algo, se vuelve al paso 4: volver otro día cuesta mucho más.
6. **Procesamiento:** selección de fotos, modelo 3D, ortomosaicos, termogramas (módulos 7 y 8).
7. **Lectura de daños:** cada daño se convierte en un hallazgo con ficha (módulo 6 y anexo B).
8. **Ubicación en el modelo:** cada hallazgo se asigna a un elemento estructural (módulo 9).
9. **Informe:** hallazgos, severidad, limitaciones y recomendaciones (módulo 10).

## 1.5 El equipo de inspección

| Rol | Responsabilidad | ¿Puede ser la misma persona? |
| --- | --- | --- |
| Piloto al mando | Seguridad del vuelo, cumplimiento de la autorización, decisión final de volar o no | No debe ser el operador de cámara en vuelos cerca de estructuras |
| Observador visual | Vigila el espacio aéreo, la distancia a obstáculos y las personas | No |
| Operador de cámara o inspector | Encuadre, exposición y decisión de qué fotografiar; reconoce el daño en vivo | Puede ser el ingeniero |
| Ingeniero responsable | Define la pregunta, interpreta y firma el informe | Puede ser el inspector |
| Coordinador de sitio | Cierre de áreas, comunicación con ocupantes y administración | Puede ser el observador en operaciones pequeñas |

Volar y mirar el daño a la vez divide la atención; cerca de una fachada es la receta de un accidente. Por eso el curso trabaja con equipos de al menos dos personas y, de preferencia, tres.

## Errores frecuentes

- Salir a volar sin una pregunta clara: se vuela mucho y se responde poco.
- Creer que el dron reemplaza la inspección de cerca: el informe termina afirmando cosas que la imagen no puede probar.
- No revisar las fotos antes de irse del sitio.
- No consultar el modelo estructural antes de volar: se pasa por alto el elemento más exigido.

## Autoevaluación

1. Nombre tres tipos de inspección y la pregunta que responde cada uno.
2. Cite dos daños que un dron puede detectar bien y dos que no puede confirmar sin contacto o ensayo.
3. ¿Por qué el piloto no debe ser el operador de cámara cuando se vuela cerca de una fachada?
4. ¿Qué información del modelo estructural conviene revisar antes de planear el vuelo y por qué?
