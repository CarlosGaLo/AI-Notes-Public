
# Preguntas Técnicas sobre Procesamiento de Lenguaje Natural (NLP)

## ¿Qué es el Procesamiento de Lenguaje Natural (NLP)?
El Procesamiento del Lenguaje Natural (NLP, por sus siglas en inglés) es una rama de la inteligencia artificial que se encarga de la interacción entre las computadoras y los lenguajes humanos. NLP se enfoca en enseñar a las máquinas a leer, entender y generar texto o habla en lenguaje natural. Este campo abarca varias tareas, como el análisis de texto, la traducción automática y los sistemas de chatbots.

### Ejemplo:
Un asistente virtual como Alexa o Siri utiliza técnicas de NLP para entender comandos de voz y responder preguntas del usuario.

## ¿Cuál es el propósito de la tokenización en NLP?
La tokenización es el proceso de dividir un texto en unidades más pequeñas llamadas "tokens", que pueden ser palabras, frases o incluso caracteres. Este paso es crucial porque muchas técnicas de NLP trabajan con estas unidades de texto, permitiendo que los modelos procesen el texto de manera más manejable.

### Ejemplo:
Dado el texto "El gato se sienta", la tokenización lo dividiría en los siguientes tokens: ["El", "gato", "se", "sienta"].

## ¿Qué es una "stop word" en el contexto de NLP? Proporciona dos ejemplos comunes de stop words.
Las "stop words" son palabras comunes que se eliminan de un texto antes de realizar análisis NLP, ya que no añaden mucho valor al significado del texto y pueden interferir en el análisis. Estas incluyen palabras como "el", "y", "de", que aparecen con mucha frecuencia.

### Ejemplos:
- "el"
- "de"

## ¿Qué es la lematización y cómo se diferencia del "stemming"?
La lematización es el proceso de reducir una palabra a su forma base o "lema", teniendo en cuenta el contexto y la gramática. En cambio, el stemming corta las palabras a sus raíces sin considerar el contexto, lo que puede generar formas incorrectas.

### Ejemplo:
- Lematización de "corriendo": "correr".
- Stemming de "corriendo": "corr".

## ¿Qué es el análisis de sentimientos en NLP?
El análisis de sentimientos es una técnica de NLP que busca determinar si un texto expresa una opinión positiva, negativa o neutral. Se utiliza ampliamente para analizar la opinión de los usuarios en redes sociales, comentarios de productos y reseñas.

### Ejemplo:
Análisis de una reseña de producto: "Este teléfono es excelente" sería clasificado como positivo.

## ¿Cómo se utiliza la "Bolsa de Palabras" (Bag of Words) para representar textos?
El modelo de "Bolsa de Palabras" (Bag of Words, BoW) representa un texto como un conjunto de palabras sin tener en cuenta el orden de estas. Se construye un vector de frecuencia basado en la aparición de cada palabra en un documento.

### Ejemplo:
Para los textos "Me gusta el café" y "El café es bueno", el vector de palabras sería: ["Me", "gusta", "el", "café", "es", "bueno"].

## ¿Qué es una red neuronal en el contexto de NLP?
Una red neuronal en NLP es un modelo de aprendizaje profundo diseñado para procesar secuencias de texto, permitiendo a las máquinas aprender patrones y relaciones dentro de un lenguaje. Se utiliza para tareas complejas como la traducción automática y el análisis de sentimientos.

### Ejemplo:
GPT-3 es un modelo de lenguaje basado en redes neuronales que puede generar texto coherente basado en entradas de texto.

## ¿Qué hace un "modelo de lenguaje" y para qué se puede usar en NLP?
Un modelo de lenguaje predice la probabilidad de la siguiente palabra en una secuencia de texto. Esto permite a las máquinas generar texto, completar oraciones, o realizar traducciones automáticas.

### Ejemplo:
GPT (Generative Pre-trained Transformer) es un modelo de lenguaje usado para generar texto.

## ¿Qué es el "Word Embedding" y por qué es importante en NLP?
El "Word Embedding" es una técnica de representación de palabras en un espacio vectorial, donde palabras con significados similares están cercanas entre sí. Esto es importante porque permite a los modelos capturar relaciones semánticas entre palabras, mejorando el desempeño en tareas de NLP.

### Ejemplo:
En el espacio vectorial de Word2Vec, las palabras "rey" y "reina" estarían cerca entre sí, ya que tienen significados relacionados.

## Menciona dos aplicaciones comunes de NLP en la vida cotidiana.
1. **Asistentes virtuales**: Como Siri, Alexa o Google Assistant, que utilizan NLP para entender y responder preguntas del usuario.
2. **Análisis de sentimientos**: Para analizar comentarios en redes sociales o reseñas de productos.

# Preguntas con referencias

## ¿Qué es el Procesamiento de Lenguaje Natural (NLP) y cuál es su importancia en el campo de la inteligencia artificial?
Mira el punto 1 del cuestionario anterior y añadimos que su importancia está en la mejora e integración de multitud de soluciones para la vida diaria. 

## Explica la diferencia entre análisis de sentimientos y clasificación de texto en el contexto de NLP. Proporciona ejemplos prácticos de cada uno.
El **análisis de sentimientos** clasifica un texto según la emoción (positiva, negativa o neutral). La **clasificación de texto** clasifica un texto en categorías predefinidas. 
- Ejemplo de análisis de sentimientos: "Este producto es increíble" → Positivo.
- Ejemplo de clasificación de texto: "Este es un artículo de tecnología" → Categoría: Tecnología.

## Describe el concepto de "tokenización" en NLP. ¿Por qué es un paso crucial en el procesamiento de texto?
La tokenización divide un texto en partes manejables, como palabras o frases. Es crucial porque los algoritmos de NLP no pueden procesar un texto completo directamente; necesitan unidades pequeñas para trabajar eficientemente.

## ¿Qué es un modelo de lenguaje y cómo se utiliza en aplicaciones de NLP? Menciona al menos un modelo de lenguaje conocido y sus aplicaciones.
Un modelo de lenguaje predice la siguiente palabra o secuencia de palabras. Modelos como **BERT** se usan en tareas como respuesta a preguntas, traducción automática y análisis de sentimientos.

## Explora el concepto de "bolsa de palabras" (Bag of Words) en NLP. ¿Cuáles son sus ventajas y limitaciones en comparación con técnicas más avanzadas como Word Embeddings?
**Ventajas**: Es simple y fácil de implementar. **Limitaciones**: No captura el significado o la relación entre las palabras, mientras que los **Word Embeddings** sí lo hacen.
 
## Explica cómo funcionan los "Word Embeddings" y describe su importancia en la representación semántica de palabras. Menciona un ejemplo de un algoritmo utilizado para crear Word Embeddings.
Los Word Embeddings representan palabras en un espacio continuo, donde la cercanía refleja similitud semántica. Un ejemplo de algoritmo es **Word2Vec**, que utiliza técnicas de aprendizaje no supervisado para generar estos embeddings.

## Describe un caso de uso real en el que se aplique la técnica de análisis de sentimientos. ¿Qué desafíos podrías enfrentar al implementar esta técnica?
Un caso de uso real es el análisis de reseñas de productos para evaluar la satisfacción del cliente. Desafíos incluyen el sarcasmo, ironía, y el análisis de lenguaje informal.

## ¿Qué son las Redes Neuronales Recurrentes (RNN) y cómo se aplican en tareas de procesamiento de lenguaje natural? Menciona una tarea específica en la que las RNN son especialmente útiles.
Las **RNNs** son útiles para procesar secuencias de datos, como texto. Se aplican en la **traducción automática**, donde es crucial entender el contexto anterior para traducir correctamente una oración.

## Explica el concepto de "Named Entity Recognition" (NER). ¿Por qué es importante en NLP y cuáles son algunos desafíos comunes al implementarlo?
NER identifica y clasifica entidades como nombres de personas, organizaciones o lugares en un texto. Es importante para extraer información relevante. Un desafío común es la ambigüedad en nombres que pueden referirse a múltiples entidades.

## En tu opinión, ¿cuáles son las tendencias futuras en el campo del NLP? Discute al menos dos tendencias emergentes y su posible impacto en la industria.
1. **Modelos de lenguaje más grandes y generalistas** como GPT-4, que pueden realizar múltiples tareas sin ajuste fino específico.
2. **NLP explicable**, que busca hacer más transparentas las decisiones de los modelos de IA en aplicaciones críticas como la salud o el derecho.
