#pip install opencv-python
#pip install --upgrade numpy
import torch

# Cargar el modelo YOLOv5 preentrenado (usando YOLOv5s)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Realizar la inferencia sobre una imagen
## Recuerda comentar con una almohadilla las imágenes que no estés usando para evitar problemas :) 
img = 'https://ultralytics.com/images/zidane.jpg'  # Imagen de ejemplo
#img = 'https://www.shutterstock.com/image-photo/red-cats-on-sea-beach-600nw-1302160747.jpg'  # Imagen de ejemplo2
#img = 'https://p325k7wa.twic.pics/high/dragon-ball/dragonball-project-z/00-page-setup/dbzk_banner_final.jpg?twic=v1/cover-min=2300x779'  # Imagen de ejemplo3
#img = 'https://catalonia.com/documents/176177/179354/catalonia-video-games-header.jpg/acf52eeb-566c-fad7-fe7b-e567ad1c2a6e?t=1676532885908'  # Imagen de ejemplo4
#img = 'https://media.gq-magazine.co.uk/photos/645b5c3c8223a5c3801b8b26/16:9/w_2560%2Cc_limit/100-best-games-hp-b.jpg'  # Imagen de ejemplo5
results = model(img)

# Mostrar los resultados
results.show()

# Opcionalmente, guardar los resultados
results.save()

# Para obtener las coordenadas de los bounding boxes y etiquetas
print(results.xyxy[0])  # Coordenadas de las cajas delimitadoras
print(results.pandas().xyxy[0])  # Resultados en formato pandas