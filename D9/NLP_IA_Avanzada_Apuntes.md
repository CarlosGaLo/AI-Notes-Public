
# NLP - IA Avanzada

## Procesamiento del Lenguaje Natural Avanzado (NLP Avanzado)

El Procesamiento del Lenguaje Natural (NLP) es una rama de la inteligencia artificial que se centra en la interacción entre las computadoras y los lenguajes humanos. En su nivel más avanzado, el NLP implica el uso de algoritmos de aprendizaje profundo, como `transformadores` y redes neuronales, para tareas complejas como la generación de texto, la traducción automática, el resumen de documentos y el análisis semántico.

Entre los temas avanzados del NLP, se incluyen:

- **Modelos de lenguaje**: Se entrenan para predecir la próxima palabra en una secuencia, lo que permite generar texto coherente.
- **Análisis de sentimientos**: Detectar emociones o polaridades en textos escritos.
- **Reconocimiento de entidades nombradas (NER)**: Identificar y clasificar entidades en un texto como nombres de personas, organizaciones, etc.
- **Resumen de texto**: Extracción o abstracción de información clave de textos largos.
  
## Qué es un Transformador

Los transformadores son arquitecturas de redes neuronales que han revolucionado el procesamiento de secuencias, especialmente en NLP. Introducidos en el artículo [*Attention is All You Need*](https://arxiv.org/abs/1706.03762) (2017), el transformador utiliza un mecanismo llamado *self-attention*, que permite que cada palabra de una secuencia preste atención a otras palabras en la misma secuencia, independientemente de la distancia en la cadena.

Una `secuencia` es, en el contexto de transformadores, una serie de elementos ordenados que son procesados por el modelo. En el caso del procesamiento del lenguaje natural (NLP), una secuencia suele referirse a una secuencia de palabras o tokens en una oración o texto. La longitud de la secuencia depende de la tokenización que se haya realizado.

### Arquitectura del Transformador

- **Codificador**: Toma una secuencia de entrada y produce una representación interna.
- **Decodificador**: Genera una secuencia de salida basada en esa representación interna.
- **Atención**: La clave del éxito del transformador es el mecanismo de atención, en particular el mecanismo de *multi-head attention*, que permite al modelo enfocarse en diferentes partes del texto simultáneamente.

## Cómo los Transformadores han Cambiado la Industria

La llegada de los transformadores ha traído cambios significativos en la industria tecnológica y en la forma en que interactuamos con los sistemas inteligentes:

- **Automatización del servicio al cliente**: Chatbots avanzados y asistentes virtuales como Alexa o Google Assistant.
- **Mejoras en traducción automática**: Modelos como Google Translate han mejorado drásticamente en precisión.
- **Generación de texto**: Los modelos de lenguaje como GPT son capaces de generar texto humano convincente en aplicaciones que van desde la creación de contenido hasta la codificación automática.
- **Medicina y bioinformática**: Transformadores aplicados a la secuenciación genética y análisis de datos biomédicos.

## Qué son los LLMs (Modelos de Lenguaje de Gran Escala)

Los LLMs son modelos de lenguaje que tienen miles de millones de parámetros y están entrenados en grandes cantidades de datos textuales. Estos modelos pueden realizar tareas como traducción, respuesta a preguntas, generación de texto, entre otras.

- **Capacidades**: Los LLMs pueden realizar tareas de NLP sin necesidad de un ajuste fino en datos específicos.
- **Escalabilidad**: Cuanto más grande es el modelo y más datos utiliza, mejor es su rendimiento en tareas de lenguaje natural.
- **Modelos populares**: GPT-3, BERT, T5, y muchos otros son ejemplos de LLMs.

## Modelos pre-entrenados de LLMs que puedo usar en local

Existen muchos modelos pre-entrenados que puedes descargar y ejecutar en local:

- **GPT-2**: Disponible a través de la librería Hugging Face. Es menos potente que GPT-3, pero manejable localmente en máquinas con GPU.
- **BERT**: Un modelo de codificación de texto extremadamente popular que puedes usar para tareas de clasificación de texto, NER y más.
- **DistilGPT**: Una versión más pequeña y eficiente de GPT-2 que puede correr en máquinas más modestas.
- **LLaMA**: Un LLM reciente de Meta optimizado para ser más eficiente en el uso de hardware local.

## Diferencia entre Modelo Base, Modelo Pre-entrenado y Modelo Fine-Tuning

1. **Modelo Base**: Un modelo no entrenado que no ha sido expuesto a ningún dato, simplemente tiene la arquitectura.
2. **Modelo Pre-entrenado**: Un modelo que ha sido entrenado en una gran cantidad de datos generales, lo que lo convierte en una excelente base para otras tareas.
3. **Fine-Tuning**: El ajuste fino es el proceso de tomar un modelo pre-entrenado y entrenarlo en datos específicos de una tarea particular para mejorar su rendimiento en esa tarea.

## GPT-3 & The Pile V1

**GPT-3** es un modelo LLM extremadamente grande con 175 mil millones de parámetros, entrenado en una variedad de tareas de lenguaje. 

**The Pile V1** es un conjunto de datos masivo utilizado para entrenar modelos de lenguaje. Contiene una amplia gama de datos textuales de distintas fuentes, como artículos académicos, libros, sitios web, etc.

## Base LLM vs Instruction Tuned LLM

- **Base LLM**: Estos modelos están entrenados para predecir la próxima palabra en una secuencia de texto y no están adaptados para tareas específicas o instrucciones detalladas.
- **Instruction Tuned LLM**: Un modelo ajustado a instrucciones está afinado para seguir instrucciones humanas más detalladas y específicas, mejorando su utilidad en interacciones de usuario.

## Consejos de Prompt Engineering

El *Prompt Engineering* es el arte de diseñar los mensajes de entrada (prompts) que se le dan a un modelo de lenguaje para obtener la respuesta más útil posible.

### Consejos:

1. **Sé específico**: Cuanto más detallado sea el prompt, mejor será la respuesta.
2. **Proporciona contexto**: Incluye toda la información relevante que el modelo pueda necesitar para generar una respuesta precisa.
3. **Instrucciones paso a paso**: Para tareas complejas, desglosa las instrucciones en pasos más pequeños.
4. **Ejemplos**: Proporcionar ejemplos de la salida deseada puede ayudar al modelo a comprender mejor el formato o estilo esperado.
5. **Iteración**: Experimenta con diferentes variaciones de prompts para descubrir cuál ofrece la mejor respuesta.