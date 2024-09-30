
# Ventajas y Desventajas de Trabajar a Nivel de Carácter vs Palabra en Modelos NLP

## Ventajas de trabajar a nivel de carácter:

1. **Manejo de palabras desconocidas (OOV - Out Of Vocabulary)**:
   - Al trabajar a nivel de palabra, el modelo no podrá procesar palabras fuera del vocabulario. 
   - A nivel de carácter, el modelo puede descomponer las palabras desconocidas en caracteres y procesarlas sin problema, lo cual es útil para nombres propios o palabras nuevas.

2. **Modelo más compacto**:
   - El vocabulario es mucho más pequeño a nivel de carácter. Por ejemplo, con solo las letras, números y algunos símbolos, puedes cubrir gran parte de los textos, reduciendo el tamaño del modelo y su complejidad.

3. **Mejor generalización para diferentes idiomas**:
   - A nivel de carácter, se pueden procesar diferentes idiomas sin la necesidad de cambiar el vocabulario del modelo, especialmente en idiomas con alfabetos similares.

4. **Procesamiento de subpalabras y morfología**:
   - A nivel de carácter, el modelo puede aprender patrones morfológicos, como prefijos, sufijos o conjugaciones, que pueden ser importantes para comprender la estructura gramatical de un idioma.

5. **Tolerancia a errores tipográficos**:
   - El modelo puede manejar pequeños errores tipográficos porque sigue siendo capaz de procesar cada carácter, incluso si algunas palabras tienen fallas de escritura.

6. **Creación de nuevo vocabulario**:
   - Los modelos basados en caracteres pueden generar palabras nuevas a partir de combinaciones de caracteres, lo que es útil en tareas creativas como la generación de texto.

## Desventajas de trabajar a nivel de carácter:

1. **Secuencias más largas**:
   - Trabajar a nivel de carácter genera secuencias más largas que a nivel de palabra, lo que puede aumentar el tiempo de procesamiento y entrenamiento.

2. **Mayor dificultad para aprender patrones a largo plazo**:
   - Los modelos basados en caracteres necesitan procesar más tokens para entender el contexto, lo que hace que sea más difícil capturar patrones de larga distancia en las secuencias.

3. **Falta de información semántica inmediata**:
   - Las palabras contienen información semántica que se pierde al trabajar a nivel de carácter. El modelo necesita aprender primero a construir palabras y luego extraer su significado, lo que puede ser más ineficiente.

4. **Menor eficiencia en tareas de comprensión de texto**:
   - En tareas como análisis de sentimientos o clasificación de texto, trabajar a nivel de palabra es generalmente más eficiente, ya que las palabras ya llevan consigo información semántica que facilita el proceso de inferencia.

## ¿Cuándo es útil trabajar a nivel de carácter?

- **Generación de texto**: Ideal cuando se necesita generar texto a partir de secuencias de caracteres, como en escritura automática o generación creativa de texto.
- **Lenguajes con alfabetos pequeños**: Para lenguajes con un alfabeto limitado, como el español o el inglés, donde las combinaciones de caracteres cubren gran parte del vocabulario.
- **Procesamiento de errores tipográficos o palabras nuevas**: Aplicaciones donde se espera encontrar errores ortográficos o invención de nuevas palabras.
- **Corpus con palabras raras**: Cuando el corpus contiene muchas palabras únicas, nombres propios o términos técnicos.

## ¿Cuándo es mejor trabajar a nivel de palabra?

- **Tareas de comprensión del lenguaje**: Para tareas como traducción automática o análisis de sentimientos, donde el significado semántico de las palabras es importante.
- **Modelos preentrenados**: Muchos modelos como Word2Vec o BERT están entrenados a nivel de palabra o subpalabra, por lo que trabajar a este nivel permite aprovechar los beneficios de estos modelos.
