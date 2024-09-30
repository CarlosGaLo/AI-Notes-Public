#pip install tensorflow
#pip install numpy
#pip install pillow  # para cargar imágenes

import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
from PIL import Image

# Cargar el modelo InceptionV3 preentrenado
model = InceptionV3(weights='imagenet')

# Función para cargar y preprocesar la imagen
def load_image(img_path):
    img = Image.open(img_path)
    img = img.resize((299, 299))  # Tamaño requerido por InceptionV3
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

# Cargar imagen y predecir
img_path = 'prueba.png'  # Coloca aquí la ruta a tu imagen
img = load_image(img_path)
predictions = model.predict(img)

print("-------------------")
print(predictions)
print("-------------------")

# Cargar imagen y predecir
koji = 'koji.jpg'  # Coloca aquí la ruta a tu imagen
img2 = load_image(koji)
predictions2 = model.predict(img2)

# Cargar imagen y predecir
tao = 'tao.jpg'  # Coloca aquí la ruta a tu imagen
img3 = load_image(tao)
predictions3 = model.predict(img3)

# Descripción de la imagen: Prueba
print("Prueba:")
decoded_predictions = decode_predictions(predictions, top=10)[0]  # Mostrar las 10 clases más probables
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i+1}: {label} ({score*100:.2f}%)")

print("--------------------------------------------------------------------------")
print("Koji:")

# Descripción de la imagen: Koji
decoded_predictions = decode_predictions(predictions2, top=15)[0]  # Mostrar las 15 clases más probables
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i+1}: {label} ({score*100:.2f}%)")

print("--------------------------------------------------------------------------")
print("Tao:")

# Descripción de la imagen: Tao
decoded_predictions = decode_predictions(predictions3, top=10)[0]
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i+1}: {label} ({score*100:.2f}%)")