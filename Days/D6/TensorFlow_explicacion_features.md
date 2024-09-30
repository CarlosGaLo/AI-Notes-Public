
# ¿Qué son las Features?

En el contexto del aprendizaje automático y las redes neuronales, las **features** (características) son las variables de entrada que se utilizan para entrenar un modelo. Estas representan los atributos o propiedades de los datos que queremos analizar y son fundamentales para que el modelo pueda aprender y hacer predicciones.

## Tipos de Features

En TensorFlow Playground, verás varias **features** representadas por X1, X2, y transformaciones de estas como X1^2, X1X2, sin(X1), y sin(X2). Pero...¿Qué significan?

### 1. **X1 y X2 (Features básicas)**

- **X1** y **X2** son simplemente las variables de entrada originales. En el Playground, X1 y X2 son las coordenadas de cada punto en el espacio de entrada.
  - Por ejemplo, si tienes un conjunto de datos de dos dimensiones (X1 y X2), estos podrían representar características como el peso y la altura de una persona, o cualquier par de variables numéricas.

### 2. **X1^2 (Cuadrado de X1)**

- Esta es una transformación no lineal de la feature X1. Tomar el cuadrado de una feature permite que el modelo capture patrones más complejos.
  - **Ejemplo**: Si X1 representa la distancia de un objeto, entonces X1^2 podría representar el área afectada por la distancia. El uso de X1^2 permite al modelo detectar relaciones cuadráticas en los datos.

### 3. **X1X2 (Multiplicación entre X1 y X2)**

- Esta es la multiplicación entre las dos variables de entrada X1 y X2. Esta interacción captura relaciones conjuntas entre dos features.
  - **Ejemplo**: Si X1 es el precio de un producto y X2 es la cantidad vendida, la multiplicación X1X2 representaría los ingresos totales. Este tipo de combinación permite que el modelo detecte interacciones entre dos features.

### 4. **sin(X1) y sin(X2) (Funciones seno)**

- Estas son transformaciones periódicas de las variables de entrada. Aplicar funciones trigonométricas como el seno permite que el modelo capture patrones cíclicos o periódicos en los datos.
  - **Ejemplo**: Si X1 representa el tiempo (en días o meses), entonces sin(X1) podría capturar patrones estacionales o repetitivos en los datos.

## ¿Por qué usar transformaciones de Features?

Las transformaciones de las features permiten que el modelo tenga mayor flexibilidad para aprender relaciones más complejas en los datos. Por ejemplo:

- Si los datos tienen patrones no lineales, como curvas o ciclos, agregar features como X1^2 o sin(X1) permite al modelo ajustar mejor estos patrones.
- Las combinaciones como X1X2 permiten detectar interacciones entre las características, lo cual puede ser muy importante en problemas con dependencias complejas entre las variables.

## Conclusión

Las **features** son los inputs básicos con los que trabaja un modelo de machine learning. Usar transformaciones no lineales o combinaciones entre features permite que el modelo sea capaz de capturar patrones más complejos en los datos. Dependiendo del tipo de problema, elegir las features adecuadas y las transformaciones correctas puede hacer una gran diferencia en el rendimiento del modelo.

# Ampliación de la explicación

Normalmente la parte que más confunde es la de las Features, porque ¿qué estamos haciendo realmente? Así que vamos a explayarnos un poquito.

## 1. ¿Qué son las features realmente?
Las **features** son **variables de entrada** que usas para "enseñar" a la red neuronal. En el caso del TensorFlow Playground, las features como **X1**, **X2**, **X1^2**, etc., son simplemente ejemplos de cómo puedes transformar o modificar los datos de entrada para entrenar mejor al modelo.

- **X1 y X2**: Son variables directas, como atributos básicos de los datos (por ejemplo, peso y altura).
- **Transformaciones (X1^2, X1X2, sin(X1))**: Son formas de agregar complejidad. Estas transformaciones ayudan al modelo a captar patrones más complicados en los datos.

Piensa en las features como **inputs** para la red neuronal. Es decir, son los datos crudos que la red utiliza para aprender patrones.

## 2. ¿Qué está pasando en el Playground?
Cuando usas TensorFlow Playground, estás **entrenando una red neuronal** para aprender de los datos. El proceso sigue estos pasos clave:

1. **Alimentar la red con datos de entrada (features)**:
   - Las features como X1, X2 o las transformaciones son **parámetros de entrada**. En el Playground, los puntos en la gráfica representan ejemplos de entrenamiento. Las coordenadas (X1, X2) de esos puntos son los datos que la red intenta aprender a clasificar.

2. **Ajuste de los pesos**:
   - La red neuronal tiene neuronas y conexiones (pesos) entre ellas. Cuando entrenas el modelo, lo que realmente estás haciendo es ajustar esos pesos. El algoritmo de aprendizaje, como el **gradiente descendente**, va ajustando esos pesos para minimizar el error entre la predicción de la red y la realidad.

3. **Predicción**:
   - Después de entrenar, la red usa lo que ha aprendido (los pesos ajustados) para hacer predicciones. En el caso del Playground, ves estas predicciones como **áreas de color** que indican cómo la red clasifica diferentes puntos basándose en las features.

## 3. ¿Estoy entrenando una IA o solo visualizando resultados?
**Estás entrenando una IA en el Playground**. Aunque el proceso parece sencillo, realmente estás pasando por las mismas fases que una red neuronal en un entorno de producción:

- **Entrenamiento**: Al hacer clic en "Run", la red ajusta sus pesos basándose en las features que eliges y los datos de entrada.
- **Visualización de resultados**: Lo que ves en el Playground es cómo la red está clasificado los datos después de varias iteraciones de entrenamiento.

## 4. Diferencia entre "representar resultados" y "entrenar"
- **Entrenar**: Significa que estás ajustando los pesos de la red neuronal para que pueda "aprender" a predecir correctamente basándose en las features de entrada.
- **Representar resultados**: Esto es lo que ves después del entrenamiento. Los resultados visuales que ves son una representación de cómo la red neuronal clasifica los datos basándose en lo que ha aprendido.

## Resumen
- **Features**: Son las variables de entrada con las que entrenas la red.
- **Entrenamiento**: Estás ajustando los pesos de la red neuronal con los datos de entrada.
- **Resultados visuales**: Te muestran cómo la red ha aprendido a clasificar los datos.


