# Módulo 7. Termografía aplicada

**Duración:** 3 h (2 h teoría + 1 h práctica) · **Competencias:** C3, C7

## Objetivos de aprendizaje

1. Explica qué mide una cámara térmica y qué la engaña.
2. Elige la ventana horaria y las condiciones para cada aplicación.
3. Interpreta un termograma junto con su foto visible y reporta diferencias de
   temperatura, no "temperaturas".

---

## 7.1 Qué mide una cámara térmica

Todo cuerpo emite radiación infrarroja según su temperatura. La cámara mide la
radiación que llega al sensor y la convierte en una **temperatura aparente**.
Esa radiación tiene tres orígenes:

1. La que **emite** la superficie, que depende de su temperatura y de su
   **emisividad** ε (0 a 1).
2. La que la superficie **refleja** de su entorno (cielo, edificios vecinos,
   el sol). Cuanto menor es ε, más refleja.
3. La que emite y absorbe el **aire** entre la superficie y la cámara (poco
   relevante a las distancias de inspección).

Por eso una superficie metálica brillante "parece" fría o caliente según lo
que refleja, no según su temperatura.

### Emisividad aproximada de materiales comunes

| Material | ε aproximada | Comentario |
|---|---|---|
| Concreto, pañete, mortero | 0.92-0.95 | Buen material para termografía |
| Ladrillo | 0.90-0.93 | |
| Pintura (no metálica) | 0.90-0.95 | |
| Vidrio | 0.90 aprox. | Opaco al infrarrojo térmico: se ve su superficie, **no lo que hay detrás**; refleja mucho a ángulos rasantes |
| Acero oxidado | 0.6-0.9 | Variable |
| Acero galvanizado, aluminio, metales pulidos | 0.05-0.3 | **Poco confiable**: domina el reflejo |

Son valores orientativos: dependen del acabado, la humedad y el ángulo.
Verifíquelos con las tablas del fabricante o con una referencia de emisividad
conocida (cinta de alta emisividad) en el sitio.

### Ángulo de visión

La emisividad cae a ángulos rasantes. Mantenga la cámara a **menos de unos
45° de la normal** a la superficie; en vidrios y metales, lo más frontal
posible.

### Resolución

El GSD térmico es mucho mayor que el visible: la cámara del curso tiene
9.2 mm/px a 10 m y 4.6 mm/px a 5 m. Para medir la temperatura de un detalle,
este debe ocupar **al menos 3 × 3 píxeles**. La termografía desde dron ve
manchas y zonas, no fisuras.

## 7.2 Contraste térmico: sin flujo de calor no hay imagen

Un defecto se ve en la térmica solo si **altera el flujo de calor** y si en ese
momento **hay flujo de calor**. Las fuentes de flujo en edificaciones son:

- **El sol** (termografía pasiva diurna): calienta la superficie durante el
  día; en la noche la superficie se enfría.
- **La diferencia de temperatura interior-exterior:** útil en climas con
  calefacción o aire acondicionado.
- **La evaporación de agua:** enfría las zonas húmedas.

| Aplicación | Qué se ve | Ventana horaria | Condiciones |
|---|---|---|---|
| **Desprendimiento de enchapes y recubrimientos** (vacío de aire bajo la pieza) | Durante el calentamiento solar, la zona hueca está **más caliente**; durante el enfriamiento nocturno, **más fría** | Mañana, en las horas de calentamiento de esa fachada, o noche despejada | Superficie seca, sin sombras cambiantes, viento bajo |
| **Humedad en muros y cubiertas** | Zonas más frías por evaporación; o con más inercia térmica (se calientan y enfrían más lento) | Tarde, o después de la puesta del sol en cubiertas | Sin lluvia reciente que moje toda la superficie |
| **Filtraciones en cubiertas planas** | El agua atrapada bajo la membrana guarda calor y se ve más caliente en la noche | Primeras horas de la noche tras un día soleado | Cubierta seca en superficie |
| **Delaminación del concreto** (tableros de puentes, losas) | Igual que los enchapes: la zona delaminada se calienta y enfría más rápido | Calentamiento de la mañana | Superficie seca |
| **Envolvente: aislamiento y puentes térmicos** | Pérdidas de calor | Noche o madrugada | Diferencia interior-exterior grande y estable; en clima tropical rara vez se cumple |
| **Instalaciones** (tableros, paneles solares) | Puntos calientes | Con el sistema en carga | Fuera del alcance de este curso |

Referencias de práctica: ISO 6781 (detección cualitativa de irregularidades
térmicas en la envolvente), ASTM D4788 (detección de delaminaciones en tableros
de puentes con termografía) y ASTM C1060 (inspección termográfica de
aislamiento en edificaciones). En clima tropical de altura como el de Bogotá,
la aplicación más útil es la de **desprendimientos con carga solar**.

## 7.3 Condiciones a evitar

- **Reflejos** del sol, del cielo y de edificios vecinos: cambie el ángulo y
  verifique si la "anomalía" se mueve con usted (si se mueve, es un reflejo).
- **Sombras recientes:** la sombra de un edificio vecino que acaba de pasar
  deja una "mancha fría" que no es un defecto.
- **Superficie mojada:** la evaporación domina la imagen.
- **Viento fuerte:** enfría la superficie de manera desigual.
- **Cambios de color o de material en la superficie:** distinta absorción
  solar o distinta ε; parecen anomalías. Por eso cada termograma lleva su foto
  visible.

## 7.4 Configuración de la cámara y del vuelo

- Guardado **radiométrico** y foto visible simultánea.
- Emisividad del material dominante y **temperatura reflejada** medida en el
  sitio (método del reflector difuso, como papel aluminio arrugado), o
  corregidas en posproceso.
- Rango de temperatura y paleta **fijos** para todas las fotos de una
  fachada, para que sean comparables. Paleta en escala de grises o "hierro";
  el rango manual, ajustado a la fachada.
- Registre en la bitácora: hora, temperatura y humedad del aire, nubosidad,
  viento, horas de sol sobre la fachada y lluvia de las últimas 24-48 h.
- Malla de fotos propia (la huella térmica es más pequeña): para la fachada
  de 30 × 24 m a 10 m, 486 fotos con solapes 80/70
  (`fachada --camara termica --ancho 30 --alto 24 --distancia 10`). En la
  práctica, la térmica se usa para barrer la fachada con menos solape y luego
  hacer detalle en las zonas sospechosas.

## 7.5 Interpretación y reporte

1. Compare siempre el termograma con su foto visible.
2. Busque **patrones**: una zona caliente con bordes nítidos en un enchape
   durante el calentamiento sugiere vacío; una zona fría con forma de mancha
   que baja desde una ventana sugiere humedad.
3. Reporte la **diferencia de temperatura** (ΔT) entre la zona anómala y la
   sana vecina, no la temperatura absoluta.
4. Asigne la confianza: la termografía sola casi nunca pasa de confianza B.
   Un desprendimiento sugerido por termografía se confirma con **percusión**
   en sitio antes de intervenir.

---

## Práctica (1 h)

Con la cámara térmica del curso:

1. Medir la temperatura reflejada con el reflector difuso.
2. Fotografiar un muro con enchape al sol y uno a la sombra; comparar.
3. Mostrar un reflejo en un vidrio y verificar que se mueve al cambiar de
   posición.
4. Identificar una zona sospechosa y marcarla para verificación por
   percusión.

## Errores frecuentes

- Volar la térmica a mediodía con la fachada en sombra: no hay contraste.
- Tomar un reflejo por una anomalía.
- Reportar "el muro está a 31.4 °C" sin emisividad ni temperatura reflejada.
- Cambiar el rango automático entre fotos y comparar colores que no
  significan lo mismo.
- Concluir que un enchape está desprendido solo con la térmica.

## Autoevaluación

1. ¿Por qué una lámina de aluminio brillante es un mal objeto para medir con
   termografía?
2. ¿En qué momento del día se busca el desprendimiento de enchapes en una
   fachada oriental, y cómo se ve?
3. ¿Qué tamaño mínimo debe tener una anomalía para medirla con la cámara del
   curso a 5 m?
4. ¿Cómo distingue un reflejo de una anomalía real?

Respuestas en el [anexo C](anexos/C_evaluacion.md#1-respuestas-de-las-autoevaluaciones).
