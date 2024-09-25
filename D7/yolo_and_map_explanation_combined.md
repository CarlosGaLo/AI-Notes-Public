# Modelos YOLO y Evaluación de Precisión con mAP

## Introducción a YOLO

**YOLO** (You Only Look Once) es una familia de modelos diseñados para la **detección de objetos en tiempo real**. ¿Por qué son tan populares? Porque su eficiencia permite detectar y localizar objetos dentro de una imagen o video en una sola pasada por la red neuronal, lo que los hace muy rápidos en comparación con otros métodos.

YOLO utiliza una técnica donde la imagen se divide en una cuadrícula, y cada celda de la cuadrícula predice cajas delimitadoras (bounding boxes) y las probabilidades de clase de los objetos. Así, en lugar de analizar la imagen en múltiples pasos o regiones, YOLO lo hace todo en un solo vistazo.

### Versiones de YOLOv5

Dentro de la versión **YOLOv5**, encontramos diferentes tamaños de modelos que se adaptan a las necesidades específicas de **velocidad** y **precisión**. Estas versiones son:

1. **YOLOv5s (small)**:
   - **Características**: Modelo más pequeño y rápido. Ideal para dispositivos con menos capacidad de procesamiento.
   - **Aplicaciones**: Cámaras de vigilancia, drones donde la rapidez es esencial.
2. **YOLOv5m (medium)**:

   - **Características**: Un equilibrio entre velocidad y precisión.
   - **Aplicaciones**: Sistemas que requieren detección en tiempo real, pero con mayor capacidad de procesamiento.

3. **YOLOv5l (large)**:

   - **Características**: Mayor precisión, aunque es más pesado y más lento.
   - **Aplicaciones**: Detección de objetos en entornos donde la precisión es más crítica, como en fábricas.

4. **YOLOv5x (extra-large)**:
   - **Características**: El modelo más preciso, diseñado para aplicaciones donde se requiere la mayor exactitud posible.
   - **Aplicaciones**: Análisis de imágenes médicas, control de calidad industrial.

## ¿Qué es mAP (mean Average Precision)?

Para evaluar el rendimiento de estos modelos, se utiliza una métrica llamada **mAP (mean Average Precision)**. Pero, ¿qué mide realmente?

**mAP** nos indica qué tan bien el modelo identifica y localiza los objetos en una imagen, considerando tanto la **precisión** (qué porcentaje de las detecciones son correctas) como el **recall** (qué porcentaje de los objetos presentes fueron correctamente detectados).

### ¿Qué significa "mAP coco"?

El valor **mAP coco** se refiere a la precisión media obtenida al evaluar los modelos con el conjunto de datos **COCO (Common Objects in Context)**, un benchmark estándar que contiene imágenes con objetos cotidianos en escenas naturales.

Los valores de **mAP coco** se calculan utilizando una medida llamada **IoU (Intersection over Union)**, que evalúa qué tan bien se superponen las cajas delimitadoras predichas por el modelo con las cajas reales.

### mAP para los modelos YOLOv5

Los valores de **mAP coco** que mencionamos en los modelos de YOLOv5 son los siguientes:

- **YOLOv5s**: 36.8 mAP
- **YOLOv5m**: 44.5 mAP
- **YOLOv5l**: 48.1 mAP
- **YOLOv5x**: 50.1 mAP

### ¿Qué significan estos valores?

Cada uno de estos números nos indica la precisión media de cada modelo al detectar objetos en imágenes del conjunto de datos COCO. A mayor mAP, mejor será el rendimiento del modelo para identificar correctamente objetos.

- **YOLOv5s (36.8 mAP)**: El más rápido, pero menos preciso. Ideal cuando la velocidad es lo más importante.
- **YOLOv5m (44.5 mAP)**: Un buen equilibrio entre velocidad y precisión.
- **YOLOv5l (48.1 mAP)**: Mayor precisión, pero a costa de ser más lento.
- **YOLOv5x (50.1 mAP)**: El más preciso de todos, pero requiere mayor capacidad de procesamiento.

#### 50.1 mAP ¿es como decir que acierta un 50,1% de las veces?

No, 50.1 mAP no significa que el modelo acierte el 50% de las veces. La métrica mAP (mean Average Precision) es una métrica más compleja que solo el porcentaje de aciertos y no debe interpretarse directamente como una "tasa de éxito" simple.

##### ¿Qué significa entonces eso de 50.1 mAP?

mAP (mean Average Precision) es una métrica que combina dos aspectos importantes:

- Precisión: Proporción de verdaderos positivos (detecciones correctas) entre todas las detecciones hechas (verdaderos positivos + falsos positivos).
- Recall: Proporción de verdaderos positivos entre todos los objetos que están presentes en la imagen (verdaderos positivos + falsos negativos).

Un mAP de 50.1 indica que el modelo tiene un buen rendimiento general en términos de precisión y recall sobre todas las clases de objetos evaluadas, y en diferentes niveles de IoU (Intersection over Union). Sin embargo, no significa que el modelo detecta correctamente el 50.1% de los objetos, ya que el cálculo es más detallado y depende del IoU y del recall en cada clase.

Un mAP más alto (como 50.1) sugiere que el modelo tiene un alto grado de precisión y recall en la mayoría de los casos.
Un mAP más bajo indicaría que el modelo está fallando más en detectar y localizar correctamente los objetos, o que sus predicciones no están bien alineadas con los objetos reales.

##### mAP y su interpretación
Ya vemos que un mAP me da más datos que simplemente "acierto" y "no acierto", por lo que es muchísimo más preciso que una media. Pero... ¿Cómo podemos interpretar los mAP?

- mAP > 50: Un mAP superior a 50, como 50.1, indica un rendimiento bastante bueno. El modelo está detectando bien los objetos y las cajas predichas están razonablemente alineadas con los objetos reales.

- mAP entre 30 y 50: Indica un rendimiento moderado. El modelo puede estar fallando en detectar ciertos objetos o tener problemas con la localización precisa de los mismos.

- mAP < 30: Señala que el modelo no está funcionando bien. Tiene dificultades para detectar objetos correctamente y la calidad de las predicciones es baja.

## Ejemplo de uso de YOLOv5 en Python

Ahora que entendemos las diferentes versiones de YOLOv5 y cómo se evalúan, veamos cómo podemos usar YOLOv5 en un código de Python para realizar detección de objetos.

```python
import torch

# Cargar el modelo YOLOv5 preentrenado (usando YOLOv5s)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Realizar la inferencia sobre una imagen
img = 'https://ultralytics.com/images/zidane.jpg'  # Imagen de ejemplo
results = model(img)

# Mostrar los resultados
results.show()

# Opcionalmente, guardar los resultados
results.save()

# Para obtener las coordenadas de los bounding boxes y etiquetas
print(results.xyxy[0])  # Coordenadas de las cajas delimitadoras
print(results.pandas().xyxy[0])  # Resultados en formato pandas
```

## Comparación y Trade-off entre Velocidad y Precisión

El **trade-off** que encontramos en los modelos YOLOv5 (s, m, l, x) se basa en el equilibrio entre **velocidad** y **precisión**:

- **YOLOv5s** es el más rápido, pero sacrifica precisión para ganar velocidad.
- **YOLOv5x**, por otro lado, es el más preciso, pero es mucho más lento.

Este **trade-off** entre velocidad y precisión es importante cuando diseñamos un sistema que dependa de detección de objetos. Si necesitamos procesar imágenes en tiempo real, quizás debamos optar por modelos más rápidos y ligeros, como **YOLOv5s** o **YOLOv5m**. Si la precisión es crítica y el tiempo de procesamiento no es un problema, modelos más grandes como **YOLOv5x** son más adecuados.

## Conclusión

Los modelos YOLO, especialmente en su versión **YOLOv5**, nos ofrecen opciones muy flexibles para adaptarse a las necesidades de distintas aplicaciones. Desde sistemas que requieren una detección rápida en tiempo real, hasta aquellos que priorizan la precisión en tareas críticas, YOLO proporciona una solución eficiente.

La métrica **mAP coco** nos da una idea clara del rendimiento de cada modelo en términos de precisión. A mayor mAP, más efectivo será el modelo en la detección de objetos.

Esperamos que ahora tengan una comprensión más clara sobre cómo funcionan los modelos YOLOv5, su evaluación mediante mAP, y cómo elegir el modelo adecuado para sus necesidades.
