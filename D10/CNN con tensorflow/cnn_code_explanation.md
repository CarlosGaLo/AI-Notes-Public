# Código completo:

Entrenar para leer dígitos del 0 al 9.

```python
from tensorflow.keras import layers, models

# Definir el modelo
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Ver el resumen del modelo
model.summary()
```

---

## Explicación paso a paso:

### Paso 1: Importación de módulos de TensorFlow y Keras

```python
from tensorflow.keras import layers, models
```

- **`from tensorflow.keras`**: Este comando importa el módulo `keras` que está integrado en **TensorFlow**. Keras es una API de alto nivel que se utiliza para crear y entrenar redes neuronales de manera sencilla.
- **`layers`**: Contiene los tipos de capas (densas, convolucionales, etc.) que puedes usar en tu modelo.
- **`models`**: Contiene las herramientas para definir y trabajar con modelos completos (secuenciales o funcionales).

---

### Paso 2: Definir un modelo secuencial

```python
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```

En este paso, estás creando un **modelo secuencial** usando `models.Sequential()`, lo que significa que las capas del modelo se apilan una tras otra de manera lineal.

#### Capas:

1. **Primera capa `Dense` (128 neuronas, activación ReLU)**:
   ```python
   layers.Dense(128, activation='relu', input_shape=(784,))
   ```

   - **`Dense(128)`**: Define una capa densamente conectada (fully connected) con **128 neuronas**.
   - **`input_shape=(784,)`**: Indica que cada entrada a esta capa es un vector unidimensional de 784 características (por ejemplo, una imagen de 28x28 píxeles linealizada en un vector plano de 784 valores). Esta es la capa de entrada de la red.
   - **`activation='relu'`**: Utiliza la función de activación **ReLU** (Rectified Linear Unit), que introduce no linealidad al modelo y permite que la red aprenda relaciones complejas. ReLU transforma cualquier valor negativo a 0, y mantiene los valores positivos sin cambios.

2. **Segunda capa `Dense` (64 neuronas, activación ReLU)**:
   ```python
   layers.Dense(64, activation='relu')
   ```

   - **`Dense(64)`**: Define una segunda capa densamente conectada con **64 neuronas**.
   - **`activation='relu'`**: Usa la activación ReLU, similar a la capa anterior.

3. **Tercera capa `Dense` (10 neuronas, activación softmax)**:
   ```python
   layers.Dense(10, activation='softmax')
   ```

   - **`Dense(10)`**: Define la capa de salida con **10 neuronas**, una para cada clase (por ejemplo, si estás clasificando 10 dígitos, del 0 al 9).
   - **`activation='softmax'`**: Usa la función de activación **softmax**, que convierte los valores de salida en probabilidades. Cada neurona tendrá un valor entre 0 y 1, y la suma de todas las probabilidades será 1. Esto es ideal para problemas de clasificación multiclase, donde el modelo elige la clase con la mayor probabilidad.

---

### Paso 3: Compilar el modelo

```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

Aquí estás configurando cómo el modelo será entrenado. Este paso "prepara" el modelo para el proceso de entrenamiento.

- **`optimizer='adam'`**: Aquí estás seleccionando el optimizador **Adam**, que es un método de descenso de gradiente estocástico optimizado. Adam ajusta los pesos del modelo durante el entrenamiento para minimizar el error de predicción (pérdida).
- **`loss='sparse_categorical_crossentropy'`**: La función de pérdida que se utilizará es la **entropía cruzada categórica** para etiquetas enteras (es decir, para clasificación multiclase, donde cada etiqueta es representada como un número entero en lugar de un vector one-hot). Esta función mide la distancia entre las predicciones del modelo y las etiquetas reales.
- **`metrics=['accuracy']`**: Estás indicando que durante el entrenamiento se mostrará la **precisión** como métrica, lo que permite ver qué tan preciso es el modelo en términos del porcentaje de predicciones correctas.

---

### Paso 4: Mostrar el resumen del modelo

```python
model.summary()
```

Este comando imprime una descripción estructurada del modelo que acabas de definir, incluyendo:
- La forma y el número de parámetros de cada capa.
- El número total de parámetros entrenables.

Un ejemplo del **output** del resumen del modelo podría verse así:
```
Layer (type)                 Output Shape              Param #
=================================================================
dense_1 (Dense)              (None, 128)               100480
_________________________________________________________________
dense_2 (Dense)              (None, 64)                8256
_________________________________________________________________
dense_3 (Dense)              (None, 10)                650
=================================================================
Total params: 109,386
Trainable params: 109,386
Non-trainable params: 0
```

Este resumen te muestra:
- **Output Shape**: La forma de salida de cada capa.
- **Param #**: El número de parámetros entrenables en cada capa (se puede calcular como: número de entradas x número de neuronas + un parámetro de sesgo por neurona).

---

### Conclusión

Este código crea y compila un **modelo de red neuronal densa (fully connected)** para un problema de clasificación multiclase, donde el modelo toma una entrada de 784 características (posiblemente una imagen 28x28 aplanada) y produce probabilidades para 10 clases (posiblemente dígitos del 0 al 9). Usa la activación **ReLU** en las capas ocultas para agregar no linealidad, y **softmax** en la capa de salida para devolver probabilidades de clasificación.

Este es un flujo básico de creación de redes neuronales en Keras/TensorFlow, que puedes ajustar y extender para problemas más complejos.

