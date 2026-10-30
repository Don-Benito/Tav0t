# Anexo B. Formatos

## 1. Plan de misión

| Campo | Contenido |
|---|---|
| **Operación** | Nombre, código, fechas |
| **Encargo y pregunta** | Quién pide, para qué, qué decisión se tomará con la inspección |
| **Estructura** | Tipo, sistema estructural, dimensiones, pisos, materiales, edad |
| **Información previa** | Planos, modelo estructural (elementos y pisos críticos: D/C, derivas), inspecciones anteriores |
| **Entorno** | Vías, andenes, vecinos, cables, árboles, helipuertos y aeródromos cercanos, fuentes de interferencia |
| **Autorización y espacio aéreo** | Número de autorización, condiciones, horario, altura máxima, restricciones |
| **Equipo** | Aeronave(s), cámara(s), térmica, RTK/PPK, baterías |
| **Resolución** | Detalle mínimo a ver; GSD objetivo por superficie; distancias resultantes (calculadora del curso) |
| **Malla y patrones** | Por fachada y cubierta: distancia, solapes, número de pasadas y de fotos |
| **Detalles prioritarios** | Lista de puntos de detalle con zoom y su justificación (cobertura, modelo) |
| **Térmica** | Aplicación, ventana horaria por fachada, condiciones exigidas |
| **Puntos de control y chequeo** | Número, ubicación, método de medición, sistema y tipo de altura |
| **Horario** | Por fachada, según luz y térmica |
| **Límites** | Viento máximo, batería de regreso, distancia mínima a la estructura, altura de RTH |
| **Despegue** | Punto principal y alterno (croquis) |
| **Roles** | Piloto al mando, observador, operador de cámara, coordinador |
| **Riesgos** | Matriz de riesgos (módulo 2) con mitigaciones y riesgo residual |
| **Emergencias** | Procedimientos específicos del sitio, teléfonos, hospital |
| **Datos** | Nombres de vuelos, respaldo, criterio de aceptación (nitidez, cobertura, exactitud) |
| **Aprobación** | Firma del piloto al mando y del ingeniero responsable |

## 2. Ficha de hallazgo

| Campo | Contenido |
|---|---|
| **Id** | H__ (único en toda la inspección) |
| **Elemento** | Id del modelo estructural, o descripción si no está modelado |
| **Ubicación** | Eje, piso, fachada, cara del elemento, zona (apoyo, centro, arranque) |
| **Coordenadas** | UTM + altura (tipo de altura declarado) y coordenadas de modelo |
| **Tipo de daño** | Fisura, desprendimiento, corrosión, humedad, deformación, faltante… |
| **Descripción** | Observación: orientación, patrón, extensión, color, signos asociados |
| **Medida** | Valor, método (foto, ortomosaico, nube) e incertidumbre |
| **Evidencia** | Fotos de contexto y de detalle (nombres de archivo), termograma |
| **Causa probable** | Interpretación, separada de la observación |
| **Información del modelo** | D/C del elemento, deriva del piso |
| **Severidad** | 0 a 4 (sección 3) |
| **Confianza** | A, B o C (sección 3) |
| **Recomendación** | Acción, responsable sugerido y plazo |
| **Comparación** | Estado en la inspección anterior, si existe |

### Ejemplo resuelto: H01

| Campo | Contenido |
|---|---|
| **Id** | H01 |
| **Elemento** | C1-02, columna 50 × 50 cm, planta baja |
| **Ubicación** | Esquina de los ejes C y 1 (x = 12 m, y = 0 m), cara exterior hacia el eje 1, tercio inferior |
| **Coordenadas** | UTM 18N E 604827.109, N 514160.048, H 2601.825 m · Modelo (12.00, −0.25, 1.83) m |
| **Tipo de daño** | Fisura |
| **Descripción** | Fisura única, inclinada unos 45°, de unos 0.9 m de largo, sin desplazamiento visible entre bordes, sin óxido ni eflorescencia |
| **Medida** | Ancho ≈ 1.5 mm ± 0.4 mm en la foto frontal Z_0143 (zoom, GSD 0.4 mm/px) |
| **Evidencia** | Contexto: foto de cobertura de la fachada del eje 1; detalle: Z_0143.JPG |
| **Causa probable** | Patrón compatible con cortante en la columna (posible efecto sísmico o de columna corta si hay antepecho); descartar en sitio que sea una fisura del pañete |
| **Información del modelo** | D/C = 0.86 en SISMO_X (planta baja, donde están las columnas más exigidas del edificio); piso 1, deriva 0.00357 |
| **Severidad** | 3 (severo): fisura de cortante en columna de planta baja muy exigida |
| **Confianza** | B: el patrón es claro, pero hay que confirmar en sitio que afecta al concreto y no solo al acabado |
| **Recomendación** | Verificación de cerca (retirar pañete localmente, medir con fisurómetro, buscar fisuras en las otras caras) y evaluación estructural de la columna en semanas; instalar testigos para seguimiento |
| **Comparación** | Sin inspección anterior |

## 3. Escala de severidad y de confianza

### Severidad

| Nivel | Nombre | Criterio | Respuesta orientativa |
|---|---|---|---|
| 0 | Sin daño | Elemento observado sin daño visible | Registro |
| 1 | Leve | Daño estético o de durabilidad incipiente, sin efecto en la capacidad | Seguimiento en la próxima inspección rutinaria |
| 2 | Moderado | Afecta la durabilidad o el funcionamiento (corrosión activa, filtraciones, desprendimientos locales sin riesgo de caída a zonas de paso) | Reparación programada en meses |
| 3 | Severo | Compromete o puede comprometer la capacidad del elemento, o puede caer algo a una zona de paso | Verificación y evaluación de ingeniería en semanas; medidas preventivas |
| 4 | Crítico | Riesgo inmediato para personas o para la estabilidad | **Acción inmediata:** restringir el acceso o el uso, apuntalar, retirar elementos sueltos, avisar a la autoridad |

Los umbrales numéricos (anchos de fisura, pérdidas de sección, deformaciones)
son datos del proyecto o de la norma aplicable, no de esta escala.

### Confianza de la observación

| Nivel | Significado | Consecuencia |
|---|---|---|
| **A** | El daño se ve con detalle suficiente y sin ambigüedad | La severidad se puede usar para decidir |
| **B** | El daño es probable, pero la imagen no basta para confirmarlo o medirlo | Verificar de cerca antes de intervenir |
| **C** | Indicio (por ejemplo, solo termografía o una sombra sospechosa) | Requiere inspección de cerca o ensayo |

La combinación **severidad alta + confianza B o C** genera una verificación
prioritaria, no una conclusión.

## 4. Bitácora de vuelo

Formato en CSV (`bitacora_vuelos.csv`), una fila por vuelo:

```
fecha;vuelo;piloto;observador;aeronave;bateria;despegue;aterrizaje;objetivo;viento_m_s;incidentes;observaciones
2026-11-05;20261105_EdA_F1_V01;J. Pérez;A. Gómez;UA-01;B03;09:12;09:31;Cobertura fachada eje 1;3;Ninguno;Deriva de 0.5 m en el ensayo a 6 m
```

Toda emergencia o incidente, aunque no haya consecuencias, se anota en
`incidentes` y se analiza en la revisión del día.
