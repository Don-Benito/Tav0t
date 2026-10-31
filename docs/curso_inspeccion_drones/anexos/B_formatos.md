# Anexo B. Formatos

Cuatro formatos acompañan cada operación: el plan de misión antes del vuelo, la bitácora durante, y la ficha de hallazgo con las escalas de severidad y confianza después.

## B.1 Plan de misión

| Campo | Contenido |
| --- | --- |
| Operación | Nombre, código, fechas |
| Encargo y pregunta | Quién pide, para qué, qué decisión se tomará con la inspección |
| Estructura | Tipo, sistema estructural, dimensiones, pisos, materiales, edad |
| Información previa | Planos, modelo estructural (elementos y pisos críticos: D/C, derivas), inspecciones anteriores |
| Entorno | Vías, andenes, vecinos, cables, árboles, helipuertos y aeródromos cercanos, fuentes de interferencia |
| Autorización y espacio aéreo | Número de autorización de la DGAC, condiciones, horario, altura máxima, restricciones |
| Equipo | Aeronaves (registro, masa, paracaídas), cámaras (gran angular y zoom), RTK o PPK, baterías |
| Resolución | Detalle mínimo a ver; GSD objetivo por superficie; distancias resultantes (calculadora del curso) |
| Malla y patrones | Por fachada y cubierta: distancia, solapes, número de pasadas y de fotos |
| Detalles prioritarios | Lista de puntos de detalle con zoom y su justificación (cobertura, modelo) |
| Puntos de control y chequeo | Número, ubicación, método de medición, marco (SIRGAS-Chile), huso, época y tipo de altura |
| Horario | Por fachada, según la luz |
| Límites | Viento máximo, batería de regreso, distancia mínima a la estructura, altura de RTH |
| Despegue | Punto principal y alterno (croquis) |
| Roles | Piloto al mando, observador, operador de cámara, coordinador |
| Riesgos | Matriz de riesgos (módulo 2) con mitigaciones y riesgo residual |
| Emergencias | Procedimientos específicos del sitio, teléfonos, hospital |
| Datos | Nombres de vuelos, respaldo, criterio de aceptación (nitidez, cobertura, exactitud) |
| Aprobación | Firma del piloto al mando y del profesional responsable |

## B.2 Ficha de hallazgo

| Campo | Contenido |
| --- | --- |
| Id | H\_\_ (único en toda la inspección) |
| Elemento | Id del modelo estructural, o descripción si no está modelado |
| Ubicación | Eje, piso, fachada, cara del elemento, zona (apoyo, centro, arranque) |
| Coordenadas | UTM + altura (tipo de altura declarado) y coordenadas de modelo |
| Tipo de daño | Fisura, desprendimiento, corrosión, humedad, deformación, faltante |
| Descripción | Observación: orientación, patrón, extensión, color, signos asociados |
| Medida | Valor, método (foto, ortomosaico, nube) e incertidumbre |
| Evidencia | Fotos de contexto y de detalle (nombres de archivo) |
| Causa probable | Interpretación, separada de la observación |
| Información del modelo | D/C del elemento, deriva del piso |
| Severidad | 0 a 4 (B.3) |
| Confianza | A, B o C (B.3) |
| Recomendación | Acción, responsable sugerido y plazo |
| Comparación | Estado en la inspección anterior, si existe |

**Ejemplo resuelto: H01.**

| Campo | Contenido |
| --- | --- |
| Id | H01 |
| Elemento | C1-02, pilar de 50 × 50 cm, primer piso |
| Ubicación | Esquina de los ejes C y 1 (x = 12 m, y = 0 m), cara exterior hacia el eje 1, tercio inferior |
| Coordenadas | UTM 19S (SIRGAS-Chile) E 345995.521, N 6298099.023, H 561.825 m · Modelo (12.00, −0.25, 1.83) m |
| Tipo de daño | Fisura |
| Descripción | Fisura única, inclinada unos 45°, de unos 0.9 m de largo, sin desplazamiento visible entre bordes, sin óxido ni eflorescencia |
| Medida | Ancho de unos 1.5 mm ± 0.4 mm en la foto frontal Z\_0143 (zoom, GSD 0.4 mm/px) |
| Evidencia | Contexto: foto de cobertura de la fachada del eje 1; detalle: Z\_0143.JPG |
| Causa probable | Patrón compatible con corte en el pilar (posible efecto sísmico o de pilar corto si hay antepecho); descartar en sitio que sea una fisura del estuco |
| Información del modelo | D/C = 0.86 en SISMO\_X (primer piso, donde están los pilares más exigidos del edificio); piso 1, deriva 0.00149, 75 % del límite de la NCh 433 |
| Severidad | 3 (severo): fisura de corte en pilar del primer piso muy exigido |
| Confianza | B: el patrón es claro, pero hay que confirmar en sitio que afecta al hormigón y no solo al estuco |
| Recomendación | Verificación de cerca (retirar estuco localmente, medir con fisurómetro, buscar fisuras en las otras caras) y evaluación estructural del pilar en semanas; instalar testigos para seguimiento |
| Comparación | Sin inspección anterior |

## B.3 Escalas de severidad y de confianza

**Severidad:**

| Nivel | Nombre | Criterio | Respuesta orientativa |
| --: | --- | --- | --- |
| 0 | Sin daño | Elemento observado sin daño visible | Registro |
| 1 | Leve | Daño estético o de durabilidad incipiente, sin efecto en la capacidad | Seguimiento en la próxima inspección rutinaria |
| 2 | Moderado | Afecta la durabilidad o el funcionamiento (corrosión activa, filtraciones, desprendimientos locales sin riesgo de caída a zonas de paso) | Reparación programada en meses |
| 3 | Severo | Compromete o puede comprometer la capacidad del elemento, o puede caer algo a una zona de paso | Verificación y evaluación de ingeniería en semanas; medidas preventivas |
| 4 | Crítico | Riesgo inmediato para personas o para la estabilidad | Acción inmediata: restringir el acceso o el uso, apuntalar, retirar elementos sueltos, avisar a la Dirección de Obras Municipales |

Los umbrales numéricos (anchos de fisura, pérdidas de sección, deformaciones) son datos del proyecto o de la norma aplicable, no de esta escala.

**Confianza de la observación:**

| Nivel | Significado | Consecuencia |
| --- | --- | --- |
| A | El daño se ve con detalle suficiente y sin ambigüedad | La severidad se puede usar para decidir |
| B | El daño es probable, pero la imagen no basta para confirmarlo o medirlo | Verificar de cerca antes de intervenir |
| C | Indicio (por ejemplo, una sombra o una mancha que puede ser otra cosa) | Requiere inspección de cerca o ensayo |

La combinación de severidad alta con confianza B o C genera una verificación prioritaria, no una conclusión.

## B.4 Bitácora de vuelo

Una fila por vuelo, en un archivo `bitacora_vuelos.csv`:

```csv
fecha;vuelo;piloto;observador;aeronave;bateria;despegue;aterrizaje;objetivo;viento_m_s;incidentes;observaciones
2026-11-05;20261105_EdA_F1_V01;[PILOTO];[OBSERVADOR];UA-01;B03;09:12;09:31;Cobertura fachada eje 1;3;Ninguno;Deriva de 0.5 m en el ensayo a 6 m
```

Toda emergencia o incidente, aunque no haya consecuencias, se anota en la columna de incidentes y se analiza en la revisión del día.
