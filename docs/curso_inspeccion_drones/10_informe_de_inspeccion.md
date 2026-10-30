# Módulo 10. Informe de inspección y gestión de datos

**Duración:** 2 h (1 h de teoría y 1 h de taller) · **Competencia:** C10

Un buen informe responde la pregunta del encargo, separa lo observado de lo interpretado y pone sus limitaciones al principio.

**Objetivos de aprendizaje.**

1. Estructura un informe de inspección con dron que responda la pregunta del encargo.
2. Declara el alcance y las limitaciones de lo observado.
3. Organiza, respalda y entrega los datos de manera trazable y conforme a la protección de datos personales.

## 10.1 Estructura del informe

| N.º | Sección | Contenido |
| --- | --- | --- |
| 1 | Resumen ejecutivo | Una página: pregunta, conclusión, hallazgos de severidad 3 y 4, acciones inmediatas |
| 2 | Datos generales | Estructura, dirección, coordenadas, propietario, encargo, fechas, equipo de inspección |
| 3 | Alcance y limitaciones | Qué se inspeccionó y qué no; zonas sin línea de vista; condiciones que limitaron la observación; qué requiere verificación de cerca o ensayos |
| 4 | Descripción de la estructura | Sistema estructural, materiales, edad, intervenciones conocidas, información del modelo estructural usada |
| 5 | Metodología | Aeronave y sensores, autorización de vuelo, fechas y horas, meteorología, plan de vuelo, GSD logrado, georreferenciación y exactitud en puntos de chequeo, software |
| 6 | Hallazgos | Tabla resumen (id, elemento, tipo, severidad, confianza), plano u ortomosaico con la ubicación, fichas individuales |
| 7 | Evaluación | Lectura de conjunto: patrones, causas probables, relación con el análisis estructural (D/C, derivas) |
| 8 | Recomendaciones | Acciones inmediatas, verificaciones de cerca, ensayos, intervenciones, frecuencia de la próxima inspección |
| 9 | Anexos | Bitácora de vuelos, permisos, informe de procesamiento fotogramétrico, listado de archivos entregados |

**Reglas de redacción:**

- **Separe lo observado de lo interpretado.** "Se observa una fisura inclinada de unos 0.9 m en la cara exterior del pilar C1-02" es observación; "el patrón es compatible con corte" es interpretación.
- **Diga con qué se midió y con qué incertidumbre:** "ancho estimado 1.5 mm ± 0.4 mm (foto Z\_0143, GSD 0.4 mm/px)".
- **Declare la confianza** de cada hallazgo (A, B, C).
- **Nada de adjetivos sin criterio:** "grave", "leve" o "preocupante" solo con la escala de severidad del anexo B.
- **Toda recomendación tiene responsable y plazo** coherentes con la severidad.
- **Las limitaciones van al principio**, no en letra pequeña al final. Si no se pudo ver el pilar interior más exigido, se dice.

**Tabla resumen de hallazgos (ejemplo del laboratorio).** La severidad y la confianza son una propuesta para discutir en el taller; dependen de lo que muestren las fotos y de la verificación.

| Id | Elemento | Tipo | Severidad | Confianza | Acción |
| --- | --- | --- | --: | --- | --- |
| H01 | C1-02 | Fisura diagonal (corte) | 3 | B | Verificación de cerca y evaluación estructural a corto plazo |
| H06 | C1-20 | Fisura horizontal en arranque, eflorescencias | 3 | B | Verificación de cerca; revisar humedad y corrosión en la base |
| H03 | VY3-02 | Desprendimiento con armadura expuesta | 2 | A | Reparación programada; medir la pérdida de sección |
| H02 | VX2-00 | Fisura vertical (flexión) | 1 | B | Medir con fisurómetro; seguimiento |
| H05 | Muro, eje 3, piso 2 | Anomalía térmica | 1 | C | Verificar humedad o daño del muro en sitio |
| H04 | L3-01 | Mapa de fisuras en techumbre | 1 | A | Impermeabilizar |

## 10.2 Gestión de los datos

**Organización de carpetas:**

```
AAAA_estructura/
  00_admin/        encargo, permisos, autorización, plan de misión
  01_bruto/        fotos originales por vuelo, sin modificar
    20261105_EdA_F1_V01/
  02_proceso/      proyectos de fotogrametría, térmica procesada
  03_productos/    ortomosaicos, nubes, modelos 3D, GeoJSON/KML de hallazgos
  04_hallazgos/    hallazgos.json, fichas, fotos seleccionadas (con difuminado)
  05_informe/      informe y anexos
  bitacora_vuelos.csv
```

- Los datos brutos no se modifican nunca; las fotos que se entregan son copias.
- Los metadatos (EXIF/XMP: fecha, posición, orientación de la cámara) se conservan.
- Cada hallazgo se identifica una sola vez (H01, H02…), y ese identificador aparece en la ficha, en el plano, en el GeoJSON y en el informe.

**Respaldo: regla 3-2-1.** Tres copias, en dos medios distintos, una fuera del sitio. Las tarjetas de memoria se formatean solo cuando existen las dos primeras copias (módulo 5).

**Protección de datos y entrega:**

- Difumine rostros, placas e interiores visibles antes de entregar.
- Entregue por un canal con control de acceso, no por enlaces públicos.
- Acuerde en el contrato el tiempo de conservación y la eliminación posterior (Ley 19.628 y, desde su entrada en vigor, Ley 21.719; módulo 2).

**Para la siguiente inspección:** guarde los GCP, la red de puntos, el plan de misión y los modelos. La siguiente inspección repite la captura en el mismo marco y compara (módulo 8): así se sabe si los daños avanzan.

## 10.3 Responsabilidad

El informe lo firma el ingeniero civil responsable, con la competencia que exija la normativa chilena para la evaluación de estructuras. El operador RPAS firma la bitácora y responde por la operación aérea. El informe no certifica la seguridad de la estructura más allá de lo que se pudo observar y de lo que permitieron verificar los ensayos.

## Taller (1 h)

Con los hallazgos del laboratorio del módulo 9, cada grupo redacta el resumen ejecutivo, la sección de alcance y limitaciones y la tabla resumen. Los textos se intercambian entre grupos y se corrigen con las reglas de redacción.

## Errores frecuentes

- Un informe que es un álbum de fotos sin conclusión.
- Mezclar observación e interpretación.
- Limitaciones escondidas al final.
- No reportar el GSD logrado ni la exactitud en puntos de chequeo.
- Entregar fotos con personas identificables.

## Autoevaluación

1. Reescriba separando observación e interpretación: "El pilar tiene una fisura grave por sismo".
2. ¿Qué dos indicadores de calidad de los datos deben estar en la metodología?
3. ¿Qué es la regla 3-2-1?
4. ¿Por qué las limitaciones van al principio del informe?
