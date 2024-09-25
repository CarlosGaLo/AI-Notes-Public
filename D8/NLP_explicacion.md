
# Explicación del Código

## Paso a paso del código:

1. **Importación de bibliotecas**:
   ```python
   import tensorflow as tf
   import numpy as np
   ```
   Se importan `TensorFlow` y NumPy, las bibliotecas principales que se utilizan para construir y entrenar el modelo de generación de texto.

2. **Definir el corpus de entrenamiento**:
   ```python
   corpus = """..."""
   ```
   Se define un pequeño corpus de texto sobre Son Goku, que servirá como base de datos para el entrenamiento del modelo. Utilizamos las comillas dobles tres veces no sólo porque Goku es muy fuerte, también porque es la forma en la que python nos permite meter textos con saltos de línea. Para poder introducir así un texto grande.
   

3. **Preprocesamiento del texto**:
   ```python
   tokenizer = tf.keras.preprocessing.text.Tokenizer(char_level=True)
   tokenizer.fit_on_texts([corpus])
   total_chars = len(tokenizer.word_index)
   ```
   Aquí se tokeniza el corpus a nivel de carácter, es decir, cada letra o símbolo se convierte en un número que el modelo puede entender. `total_chars` representa el número total de caracteres únicos en el corpus.

   - ¿Qué es `char_level=true`?
      El argumento char_level=True en el tokenizer de Keras indica que la tokenización se hará a nivel de carácter en lugar de a nivel de palabra.

      Tokenización a nivel de palabra: Si char_level=False (el valor predeterminado), el tokenizer dividiría el texto en palabras, asignando un número único a cada palabra diferente.

      Tokenización a nivel de carácter: Al usar char_level=True, el tokenizer tratará cada carácter (letras, signos de puntuación, espacios, etc.) como una unidad separada. Cada carácter se convierte en un token único. Esto es útil en tareas donde quieres trabajar con secuencias de caracteres en lugar de palabras, como en la generación de texto carácter por carácter. Te explico las ventajas y desventajas en el archivo [Carácter vs palabra](./ventajas_caracter_vs_palabra.md)

   - ¿Qué es eso de `fit_on_texts`?

      La función fit_on_texts() toma como entrada uno o más textos y construye el vocabulario en función de las unidades que se van a tokenizar (caracteres o palabras, dependiendo de char_level).

      En este caso, dado que char_level=True, la función analiza el texto carácter por carácter y crea un diccionario que asigna un número único a cada carácter en el corpus. Este diccionario es accesible a través de tokenizer.word_index.

4. **Conversión del corpus en secuencias**:
   ```python
   input_seq = []
   target_seq = []
   seq_length = 40
   ```
   Se define la longitud de las secuencias que se usarán como entrada para el modelo (40 caracteres). Cada secuencia de entrada está asociada a una secuencia de salida.

   [Ventajas y desventajas del tamaño de la secuencia](ventajas_secuencias_largas_vs_cortas.md)

5. **Preparar los datos para el entrenamiento**:
   ```python
   text_as_int = tokenizer.texts_to_sequences([corpus])[0]
   for i in range(0, len(text_as_int) - seq_length):
       input_seq.append(text_as_int[i:i+seq_length])
       target_seq.append(text_as_int[i+1:i+seq_length+1])
   input_seq = np.array(input_seq)
   target_seq = np.array(target_seq)
   ```
   Convierte el corpus en secuencias numéricas (usando la tokenización) y crea las secuencias de entrada y salida.

6. **Construir el modelo LSTM**:
   ```python
   model = tf.keras.Sequential([
       tf.keras.layers.Embedding(total_chars + 1, 256, input_length=seq_length),
       tf.keras.layers.LSTM(256, return_sequences=True),
       tf.keras.layers.LSTM(256, return_sequences=True),
       tf.keras.layers.Dense(total_chars + 1, activation='softmax')
   ])
   ```
   Aquí se define el modelo. Consiste en una capa `Embedding` (que convierte los números en vectores densos), dos capas `LSTM` (Long Short-Term Memory) que aprenden las dependencias temporales, y una capa `Dense` para generar una distribución de probabilidad sobre los caracteres posibles.

   - Puedes mejorar el modelo incrementando la complejidad del mismo:
      ```python
      model = tf.keras.Sequential([
         tf.keras.layers.Embedding(total_chars + 1, 1024, input_length=seq_length),
         tf.keras.layers.LSTM(1024, return_sequences=True),
         tf.keras.layers.LSTM(1024, return_sequences=True),
         tf.keras.layers.Dense(total_chars + 1, activation='softmax')
      ])
      ```

   - Podemos añadir `dropout` que evita el sobreajuste y hace que el modelo generalice mejor.
      ```python
      model = tf.keras.Sequential([
      tf.keras.layers.Embedding(total_chars + 1, 1024, input_length=seq_length),
      tf.keras.layers.LSTM(1024, return_sequences=True),
      tf.keras.layers.Dropout(0.3),  # Añadir Dropout
      tf.keras.layers.LSTM(1024, return_sequences=True),
      tf.keras.layers.Dropout(0.3),  # Añadir Dropout
      tf.keras.layers.Dense(total_chars + 1, activation='softmax')
      ])
      ```

   - Podemos usar un modelo bidireccional:
      ```python
      model = tf.keras.Sequential([
      tf.keras.layers.Embedding(total_chars + 1, 256, input_length=seq_length),
      tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(256, return_sequences=True)),
      tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(256, return_sequences=True)),
      tf.keras.layers.Dense(total_chars + 1, activation='softmax')
      ])
      ```
      Captura relaciones en ambas direcciones (adelante y atrás), lo que puede mejorar la generación de texto.

   - Podemos ajustar `softmax` con `temperature`:
      ```python
      def generar_texto(modelo, tokenizer, secuencia_inicial, longitud_texto=200, temperature=1.0):
         result = secuencia_inicial
         input_eval = [tokenizer.texts_to_sequences([secuencia_inicial])[0]]
         input_eval = tf.keras.preprocessing.sequence.pad_sequences(input_eval, maxlen=seq_length, truncating='pre')

         for i in range(longitud_texto):
            predictions = modelo.predict(input_eval)
            predictions = predictions / temperature  # Ajustar la temperatura
            predicted_id = np.argmax(predictions, axis=-1)[0, -1]

            next_char = tokenizer.sequences_to_texts([[predicted_id]])[0]
            result += next_char

            input_eval = np.roll(input_eval, -1)
            input_eval[0, -1] = predicted_id

         return result
      ```
      Controla la diversidad en la generación de texto, evitando repeticiones con temperaturas más altas y generando respuestas más coherentes con temperaturas más bajas.

      - Reducir el `Learning Rate`:
      ```python
      from tensorflow.keras import regularizers

         model = tf.keras.Sequential([
            tf.keras.layers.Embedding(total_chars + 1, 256, input_length=seq_length),
            tf.keras.layers.LSTM(256, return_sequences=True, kernel_regularizer=regularizers.l2(0.01)),
            tf.keras.layers.LSTM(256, return_sequences=True, kernel_regularizer=regularizers.l2(0.01)),
            tf.keras.layers.Dense(total_chars + 1, activation='softmax')
         ])
      ```
      El modelo aprende de forma más gradual y es menos propenso a quedar "estancado" o "en un bucle". 

      ¡Y más cosas! Podrías usar regularización L2 en capas densas, modificar el corpus y un largo etc. Esto ya es ir investigando poco a poco.

      Si planteo que compares el resultado final que tenías antes con el resultado final que te daría este código con todas estas mejoras: 
      ```python
      model = tf.keras.Sequential([
      tf.keras.layers.Embedding(total_chars + 1, 512, input_length=seq_length),  # Aumentar el tamaño del embedding
      tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(512, return_sequences=True)),  # Usar LSTM bidireccional
      tf.keras.layers.Dropout(0.3),  # Añadir Dropout para regularización
      tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(512, return_sequences=True)),
      tf.keras.layers.Dropout(0.3),
      tf.keras.layers.Dense(total_chars + 1, activation='softmax')  # Salida con softmax
      ])

      # Compilación con learning rate más bajo
      model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy')
      ```

7. **Compilación del modelo**:
   ```python
   model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
   ```
   El modelo se compila utilizando el optimizador `Adam` y la función de pérdida `sparse_categorical_crossentropy`. Este tipo de pérdida se usa cuando las etiquetas están en formato entero en lugar de one-hot encoded.

8. **Entrenamiento del modelo**:
   ```python
   model.fit(input_seq, target_seq, epochs=50)
   ```
   El modelo se entrena con las secuencias de entrada y salida generadas previamente. Se especifica 50 épocas de entrenamiento.

9. **Generación de texto**:
   ```python
   def generar_texto(modelo, tokenizer, secuencia_inicial, max_caracteres=600):
       result = secuencia_inicial
       input_eval = [tokenizer.texts_to_sequences([secuencia_inicial])[0]]
       input_eval = tf.keras.preprocessing.sequence.pad_sequences(input_eval, maxlen=seq_length, truncating='pre')

       while len(result) < max_caracteres:
           predictions = modelo.predict(input_eval)
           predicted_id = np.argmax(predictions, axis=-1)[0, -1]
           next_char = tokenizer.sequences_to_texts([[predicted_id]])[0]
           result += next_char
           input_eval = np.roll(input_eval, -1)
           input_eval[0, -1] = predicted_id

       return result[:max_caracteres]
   ```
   Esta función genera texto a partir de una secuencia inicial, prediciendo el siguiente carácter en la secuencia hasta alcanzar un límite de 600 caracteres.

## ¿Qué son los Epochs y por qué hay 50?
Un **epoch** es una iteración completa sobre todo el conjunto de datos de entrenamiento. En cada epoch, el modelo ajusta sus pesos basándose en el error calculado por la función de pérdida. Tener 50 épocas permite que el modelo tenga múltiples oportunidades para mejorar y aprender las dependencias en los datos.

## ¿Qué es `loss` y qué implica un valor de 0.18?
El **loss** es una medida de qué tan mal está funcionando el modelo en predecir los datos de entrenamiento. Un valor de `0.18` sugiere que el modelo está funcionando bastante bien, pero aún hay espacio para mejorar. Valores cercanos a `0` implicarían que el modelo está prediciendo casi perfectamente las secuencias correctas.

## Características del modelo pre-entrenado
El modelo que has creado es un **modelo secuencial de LSTM**, que está diseñado para aprender dependencias temporales en los datos, en este caso, el texto. Utiliza embeddings entrenados desde cero basados en el corpus que proporcionaste y es capaz de generar texto carácter por carácter.

## ¿Podría crear mi propio Chat GPT lite con esto?
Este modelo es un buen punto de partida para crear un generador de texto, pero es mucho más sencillo que **GPT**. Los modelos GPT utilizan una arquitectura de **Transformers**, que es más poderosa y eficiente para tareas complejas de procesamiento de lenguaje natural. Sin embargo, este modelo podría considerarse una versión simplificada o "lite" de un generador de texto.

## ¿Podría crear un asistente personalizado especializado en alguna materia en concreto?
Sí, podrías entrenar este modelo con un corpus específico para crear un asistente especializado en un tema concreto. Por ejemplo, si entrenas el modelo con textos sobre medicina, historia o cualquier otro campo, el modelo aprenderá a generar texto que tenga sentido en ese contexto. Sin embargo, para tareas más avanzadas o específicas, un modelo basado en **Transformers** (como GPT) sería más adecuado.

## ¿Y si quiero que aprenda de un archivo de texto?
```python
# Cargar el documento de texto
with open('ruta/al/archivo.txt', 'r', encoding='utf-8') as file:
    corpus = file.read()

# Mostrar el contenido del archivo cargado (opcional)
print(corpus)
```
