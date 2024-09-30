
# Detectron2: Introducción y Ejemplo de Uso

[Enlace al detectron](https://colab.research.google.com/drive/16jcaJoc6bCFAQ96jDe2HwtXj7BMD_-m5#scrollTo=hBXeH8UXFcqU)

## ¿Qué es Detectron2?

Detectron2 es una biblioteca de visión por computadora de código abierto desarrollada por Facebook AI Research (FAIR) que proporciona un marco flexible y eficiente para la detección de objetos, la segmentación de instancias, la segmentación semántica, y la estimación de poses. Está construida sobre PyTorch, lo que permite a los usuarios utilizar todas las características de PyTorch, como la facilidad para entrenar y personalizar modelos de aprendizaje profundo. Además, Detectron2 soporta modelos de última generación como Mask R-CNN, Faster R-CNN, RetinaNet, y muchos otros.

Detectron2 es utilizado principalmente para tareas como:

- **Detección de Objetos**: Localizar y clasificar objetos en una imagen.
- **Segmentación de Instancias**: Asignar una máscara a cada objeto individual en una imagen.
- **Segmentación Semántica**: Asignar una clase a cada píxel de la imagen.
- **Detección de Poses**: Detectar la posición y orientación de personas en una imagen.

## El Notebook (como herramienta que hemos estado viendo en el curso)

El [código](https://colab.research.google.com/drive/16jcaJoc6bCFAQ96jDe2HwtXj7BMD_-m5#scrollTo=0d288Z2mF5dC) es un ejemplo práctico de cómo usar Detectron2 en un entorno de Google Colab para realizar detección de objetos y segmentación de instancias.

## Flujo del código

### 1. Instalación de Detectron2

El código comienza instalando Detectron2 desde el repositorio oficial, lo que permite acceder a las funcionalidades de la biblioteca directamente en el entorno de Colab.

```bash
!pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu118/torch2.0/index.html
```

### 2. Importación de Librerías

Se importan las librerías esenciales para trabajar con PyTorch y Detectron2, así como herramientas adicionales como `cv2` para manipulación de imágenes:

(Como recordatorio, eso de "importar" significa "traerse herramientas que usaremos más tarde". Con herramientas ya definidas y configuradas en otros sitios a los que, generalmente, llamaremos "librerías")

```python
import torch, torchvision
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import cv2
```

### 3. Configuración del Modelo Preentrenado

El siguiente paso es configurar un modelo preentrenado de Detectron2 para la detección de objetos. En este caso, se utiliza `COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml`, que es un modelo Mask R-CNN entrenado en el dataset COCO (Common Objects in Context = Objetos comunes en su contexto).

```python
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # Umbral de confianza para la predicción
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
predictor = DefaultPredictor(cfg)
```

#### ¿Qué es COCO (Common Objects in Context)?
Es un dataset de datos ampliamente utilizados en la investigación de visión por computadora. Fue creado por Microsoft y está diseñado para una variedad de tareas de reconocimiento de imágenes, incluyendo detección de objetos, segmentación de instancias, segmentación semántica, y detección de poses. Si quieres saber más, [ve a su página principal](https://cocodataset.org/#home).

### 4. Cargar una Imagen y Realizar Predicciones

Después de configurar el modelo, se carga una imagen utilizando OpenCV (`cv2`), y se usa el predictor de Detectron2 para realizar la predicción:

```python
im = cv2.imread("./input.jpg")
outputs = predictor(im)
```

Este código procesa la imagen y devuelve las predicciones, como las clases de objetos, las máscaras de segmentación, y las cajas delimitadoras.

### 5. Visualización de Resultados

Finalmente, se visualizan los resultados de la predicción utilizando el módulo `Visualizer`, que dibuja las máscaras, cajas, y etiquetas sobre la imagen original.

```python
v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])
```

Este bloque muestra la imagen con las predicciones visualizadas de manera interactiva en el entorno Colab.
