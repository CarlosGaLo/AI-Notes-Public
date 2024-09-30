# Tecnologías Clave en Visión por Computadora: Descripción Detallada

## 1. [LeNet-5 (1998)](https://medium.com/@siddheshb008/lenet-5-architecture-explained-3b559cb2d52b)

Desarrollada por Yann LeCun en 1998, **LeNet-5** fue una de las primeras redes neuronales convolucionales (CNNs) diseñadas para la tarea de clasificación de dígitos manuscritos, utilizando el conjunto de datos MNIST como referencia. Este fue uno de los primeros éxitos en el uso de CNNs, y aunque hoy en día su uso ha disminuido, LeNet-5 estableció los principios básicos que se utilizan en arquitecturas modernas de redes convolucionales.

### Arquitectura
LeNet-5 tiene una arquitectura simple en comparación con redes neuronales más modernas y profundas. Consta de 7 capas, excluyendo las capas de entrada y salida, e incluye tanto capas convolucionales como capas de agrupamiento (pooling), seguidas de capas totalmente conectadas. Las capas clave son:
- **Capas convolucionales**: Estas capas utilizan filtros pequeños que se deslizan sobre la imagen de entrada para detectar características locales, como bordes y esquinas.
- **Capas de agrupamiento (pooling)**: Se utilizan para reducir la dimensionalidad de las características detectadas y hacer la red más eficiente, al mismo tiempo que ayudan a controlar el sobreajuste.
- **Capas completamente conectadas**: Después de las capas convolucionales y de agrupamiento, las capas completamente conectadas toman las características aprendidas y las utilizan para tomar decisiones de clasificación.

### Impacto
Aunque la arquitectura es básica, LeNet-5 fue un gran avance en la época, demostrando que las CNNs podían superar a las técnicas tradicionales en el reconocimiento de patrones en imágenes.

---

## 2. AlexNet (2012)

En 2012, Alex Krizhevsky y su equipo introdujeron **AlexNet**, una red neuronal convolucional más profunda y poderosa que fue responsable de ganar el **desafío ImageNet**, marcando un hito en el campo de la visión por computadora. Su éxito consolidó el uso de las CNNs en este campo y popularizó el uso de GPUs para acelerar el entrenamiento de modelos.

### Características
- **Uso intensivo de GPU**: AlexNet fue una de las primeras redes en aprovechar el paralelismo masivo de las GPUs para reducir los tiempos de entrenamiento.
- **Arquitectura profunda**: AlexNet cuenta con 8 capas aprendibles, con 5 capas convolucionales y 3 capas completamente conectadas, permitiendo que la red capture características mucho más complejas de las imágenes.
- **Activación ReLU**: La función de activación **ReLU (Rectified Linear Unit)** fue un gran avance, ya que aceleró significativamente el entrenamiento al reducir los problemas de desvanecimiento del gradiente.
- **Técnicas de regularización**: Para prevenir el sobreajuste, AlexNet incorporó **data augmentation** (aumentando artificialmente el tamaño del dataset mediante rotaciones y cambios de iluminación) y **dropout** (para reducir la co-adaptación de las neuronas).

### Contribuciones Clave
AlexNet mostró que las redes neuronales profundas eran capaces de superar significativamente las técnicas tradicionales de visión por computadora, y abrió el camino para arquitecturas más grandes y complejas.

---

## 3. VGGNet (2014)

Desarrollada por el **Visual Geometry Group** de la Universidad de Oxford, **VGGNet** es conocida por su simplicidad y profundidad. A diferencia de otras arquitecturas, que varían en el tamaño de sus filtros convolucionales, VGGNet utiliza consistentemente filtros pequeños (3x3), lo que permite una estructura uniforme y fácil de implementar.

### Arquitectura
- **Capas convolucionales pequeñas (3x3)**: VGGNet apila varias capas convolucionales con filtros 3x3 en lugar de utilizar filtros más grandes, lo que le permite capturar características más complejas a medida que la red se profundiza.
- **Profundidad de la red**: VGGNet puede tener entre 16 y 19 capas, lo que la convierte en una de las arquitecturas más profundas de su tiempo. Las versiones más populares incluyen **VGG-16** y **VGG-19**.
- **Capas completamente conectadas**: Las capas convolucionales son seguidas por dos o tres capas completamente conectadas y, finalmente, una capa de softmax para la clasificación.

### Limitaciones
Aunque VGGNet tuvo éxito en la clasificación de imágenes y fue muy influyente, tiene un alto costo computacional, ya que el número de parámetros es muy grande, lo que demanda más memoria y tiempo de procesamiento.

---

## 4. ResNet (2015)

**ResNet (Residual Networks)** fue presentada por Kaiming He y su equipo en 2015, y es famosa por resolver el problema de la **degradación del gradiente** en redes profundas. ResNet introdujo el concepto de **bloques residuales**, lo que permite entrenar redes mucho más profundas sin que el rendimiento se degrade.

### Conceptos Clave
- **Bloques residuales**: Un bloque residual permite que la entrada de una capa se salte una o más capas y se sume a la salida de una capa más adelante. Esto permite a la red aprender funciones de identidad (básicamente, que la salida es igual a la entrada) cuando sea necesario, lo que ayuda a mitigar el problema de la degradación.
- **Extrema profundidad**: ResNet ha sido entrenada con hasta 152 capas (ResNet-152), lo que habría sido imposible sin los bloques residuales. Esto permitió que redes más profundas puedan entrenarse sin problemas de degradación o desaparición de gradiente.

### Impacto
ResNet no solo ganó competiciones como ImageNet, sino que se convirtió en una arquitectura de referencia para muchas otras tareas, incluidas la segmentación de imágenes y la detección de objetos. También se ha adaptado a diferentes variantes, como **ResNeXt** y **Wide ResNet**, que mejoran aún más el rendimiento.

---

## 5. Inception (GoogLeNet, 2014)

**Inception (GoogLeNet)** fue desarrollado por Google y marcó un enfoque radicalmente diferente al de las redes anteriores al usar módulos de Inception, que permiten capturar información en múltiples escalas simultáneamente.

### Módulos de Inception
- **Captura multi-escala**: Un módulo de Inception realiza múltiples convoluciones (1x1, 3x3, 5x5) y una operación de agrupamiento en paralelo. Esto permite que la red extraiga características a diferentes escalas y las combine de manera eficiente.
- **Reducción de parámetros**: Inception reduce el número de parámetros mediante el uso de convoluciones 1x1 antes de las convoluciones más grandes, lo que disminuye el costo computacional mientras mantiene una capacidad de representación robusta.
- **Profundidad optimizada**: A pesar de ser profunda, Inception es más eficiente que redes como VGGNet porque optimiza el uso de los parámetros, haciendo que la red sea más rápida de entrenar.

### Evolución
Inception ha evolucionado a lo largo del tiempo con variantes como **Inception v3** y **Inception v4**, mejorando la precisión y la eficiencia computacional, y sigue siendo una arquitectura clave en la clasificación de imágenes.

[Ampliación github](https://github.com/google/inception)

---

## 6. Transformers para Imágenes (Vision Transformers, ViTs)

Los **Transformers**, introducidos originalmente para tareas de procesamiento de lenguaje natural (NLP), han sido adaptados para la visión por computadora con la creación de los **Vision Transformers (ViTs)**. Los ViTs representan un cambio fundamental en la forma en que se procesan las imágenes.

### Principios Clave
- **División en parches**: En lugar de aplicar convoluciones, ViTs dividen la imagen en pequeños parches (por ejemplo, 16x16 píxeles), que luego se tratan como una secuencia de tokens (de manera similar a las palabras en NLP). Cada parche es linealizado y proyectado a un espacio de características.
- **Autoatención (Self-Attention)**: Utilizan el mecanismo de autoatención para capturar relaciones entre los diferentes parches de la imagen. Esto permite que la red construya una representación global de la imagen y se centre en las áreas más importantes.
- **Escalabilidad**: Los ViTs pueden superar a las CNNs cuando se entrenan en grandes cantidades de datos. Una ventaja de los transformers es que tienen menos **sesgo inductivo** que las CNNs, es decir, no imponen restricciones de diseño sobre la forma en que aprenden las relaciones espaciales, lo que los hace más flexibles.

### Impacto
Los Vision Transformers han demostrado un rendimiento competitivo en tareas de clasificación de imágenes y están comenzando a aplicarse en otras tareas de visión por computadora, como la detección de objetos y la segmentación semántica. Son una alternativa poderosa a las CNNs tradicionales cuando hay grandes cantidades de datos disponibles para el entrenamiento.



# Modelos de CV pre-entrenados

[Enlace a github](https://github.com/balavenkatesh3322/CV-pretrained-model)
