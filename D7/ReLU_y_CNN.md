
# ReLU (Rectified Linear Unit)

## ¿Qué es ReLU?

ReLU (Rectified Linear Unit) es una función de activación ampliamente utilizada en redes neuronales, especialmente en redes profundas. Su principal ventaja es que introduce no linealidad al modelo sin afectar la computación de manera significativa, lo que la convierte en una opción ideal para las capas ocultas de las redes neuronales.

La función ReLU se define de la siguiente manera:

`f(x) = \max(0, x)`

En palabras simples, la salida de ReLU es 0 si la entrada es negativa, y la misma entrada si es positiva. Esto se traduce en lo siguiente:

- Si **x < 0**, entonces **f(x) = 0**.
- Si **x ≥ 0**, entonces **f(x) = x**.

### Ejemplo

```python
import numpy as np

def relu(x):
    return np.maximum(0, x)

# Ejemplo con valores
input_values = np.array([-2, -1, 0, 1, 2, 3])
output_values = relu(input_values)
print(output_values)
```

Salida:
```
[0 0 0 1 2 3]
```

### Ventajas de ReLU
- **Simplicidad y eficiencia**: Es computacionalmente eficiente y permite un entrenamiento rápido.
- **Evitación del gradiente desaparecido**: A diferencia de la función sigmoide o tangente hiperbólica, ReLU mitiga el problema del gradiente que tiende a desaparecer en redes profundas.

### Desventajas
- **Muerte de neuronas**: Algunas neuronas pueden quedar inactivas permanentemente durante el entrenamiento si sus entradas siempre son negativas. En estos casos, variantes como **Leaky ReLU** pueden ser útiles.

## Red Neuronal Convolucional (CNN)

Las Redes Neuronales Convolucionales (CNN) están diseñadas para procesar datos con estructura de cuadrícula, como imágenes. Son especialmente útiles en el reconocimiento de patrones visuales.

### Componentes Clave

1. **Capas Convolucionales**:
   - Aplican filtros o "kernels" a la imagen de entrada para detectar características como bordes, texturas, y formas.
   - Estas capas extraen **características locales** de las imágenes al detectar patrones repetitivos.

2. **Capas de Pooling**:
   - Reducen las dimensiones de las imágenes mediante un proceso conocido como *downsampling*.
   - **Max Pooling** es una técnica común que selecciona el valor máximo en una ventana definida.

3. **Capas Completamente Conectadas (Fully Connected)**:
   - Después de varias capas convolucionales y de pooling, la CNN se conecta a capas densas, donde se realiza la clasificación final.

### Ejemplo: Detección de la Raza de un Perro

Supongamos que queremos entrenar una red para detectar la raza de un perro a partir de su imagen.

1. **Primera Capa Convolucional**: Detecta características básicas como bordes o esquinas en la imagen del perro.
2. **Capas Convolucionales Posteriores**: A medida que avanzamos por las capas, la red aprende patrones más complejos, como el contorno de las orejas, forma del hocico, o la textura del pelaje.
3. **Clasificación**: Finalmente, en las últimas capas totalmente conectadas, el modelo usará la información extraída para clasificar entre diferentes razas de perros (Golden Retriever, Poodle, etc.).

```python
# Ejemplo básico de CNN con Keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential()

# Capa convolucional
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Otra capa convolucional
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Aplanar la entrada
model.add(Flatten())

# Capa completamente conectada
model.add(Dense(128, activation='relu'))

# Capa de salida para clasificación
model.add(Dense(10, activation='softmax'))  # Supongamos 10 razas de perros
```

### Ejemplo: Conducción Autónoma en Carretera

En el caso de la conducción autónoma, una CNN puede utilizarse para analizar las imágenes captadas por las cámaras del vehículo y tomar decisiones en tiempo real. Por ejemplo:

1. **Capas Iniciales**: Las primeras capas convolucionales detectarán características como las líneas de la carretera, señales de tráfico o bordes de la carretera.
2. **Capas Intermedias**: A medida que la red profundiza, puede identificar objetos como otros vehículos, peatones, o semáforos.
3. **Decisiones en Tiempo Real**: La salida de la red será una serie de decisiones, como girar a la izquierda, reducir la velocidad, o frenar.

```python
# Ejemplo básico de una CNN para conducción autónoma con Keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential()

# Capa convolucional
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Capas adicionales convolucionales y de pooling
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Aplanar la entrada
model.add(Flatten())

# Capa completamente conectada
model.add(Dense(256, activation='relu'))

# Capa de salida para tomar decisiones
model.add(Dense(3, activation='softmax'))  # Ejemplo de salida: girar a la izquierda, seguir recto, frenar
```

Las CNNs son herramientas poderosas en el procesamiento de imágenes, lo que permite su uso en una amplia variedad de aplicaciones, desde el reconocimiento de objetos hasta la conducción autónoma.
