#pip install tensorflow -> Ejecuta el VS Code en modo administrador!
import tensorflow as tf
import numpy as np
import os # No lo estamos usando, pero lo usaríamos si quisieramos importar archivos
import sys
import random # No lo estamos usando, pero lo usaríamos para generar datos aleatorios

# Definir el corpus de entrenamiento
corpus = """
Son Goku, nacido como Kakarotto, es uno de los guerreros más poderosos y nobles del universo. Proveniente del planeta Vegeta, Goku es un Saiyajin, una raza guerrera conocida por su increíble fuerza y habilidades de combate. Siendo enviado a la Tierra como un bebé, su misión original era conquistar el planeta para su raza. Sin embargo, tras un accidente que lo hizo perder la memoria, fue criado por el bondadoso Son Gohan, quien le enseñó valores humanos como la compasión, el respeto y la amistad.

Desde su infancia, Goku mostró un increíble talento para las artes marciales, destacándose por su capacidad de adaptación en combate y su afán por superar los límites. A lo largo de los años, fue entrenado por maestros legendarios como Maestro Roshi, quien le enseñó la técnica del Kamehameha, una poderosa ola de energía que se convertiría en su movimiento icónico. Con su deseo innato de mejorar, Goku siempre buscaba nuevos rivales y desafíos, enfrentándose a poderosos enemigos como Pilaf, Red Ribbon, y el temible demonio Piccolo Daimaō.

La vida de Goku cambió drásticamente cuando descubrió su origen extraterrestre. Su hermano mayor, Raditz, llegó a la Tierra con la intención de reclutarlo para los Saiyajin y así conquistar más planetas. Este fue el inicio de una serie de batallas épicas que pondrían a prueba los límites de su poder. A lo largo de sus aventuras, Goku no solo se enfrentó a villanos de otro mundo, sino que también desarrolló fuertes lazos de amistad con personajes como Bulma, Krilin, Yamcha, y el príncipe Saiyajin, Vegeta.

A través de los años, Goku alcanzó nuevas transformaciones que aumentaron exponencialmente su fuerza. Su primera gran transformación fue convertirse en Super Saiyajin, un estado de poder legendario que le permitió derrotar a poderosos enemigos como Freezer, quien había destruido el planeta Vegeta. La batalla contra Freezer fue una de las más épicas de su vida, librada en el planeta Namek. Después de esa victoria, Goku continuó su entrenamiento, logrando nuevas formas como el Super Saiyajin 2 y el Super Saiyajin 3.

Sin embargo, sus desafíos no terminaron allí. Cuando el universo se vio amenazado por Majin Buu, un ser antiguo con la capacidad de destruir planetas, Goku mostró su verdadero poder al combinar la energía de todos los seres vivos de la Tierra en la Genkidama, una técnica de pura energía espiritual. Su capacidad para inspirar a otros a pelear a su lado demostró que Goku no solo era un guerrero excepcional, sino también un líder carismático.

Con el paso del tiempo, Goku siguió evolucionando, logrando nuevas formas como el Super Saiyajin God y el Super Saiyajin Blue, combinando su poder Saiyajin con el Ki divino. Estas transformaciones fueron clave en la lucha contra enemigos cada vez más poderosos, como Beerus, el Dios de la Destrucción, y el despiadado Zamasu.

A pesar de sus increíbles poderes, Goku siempre mantuvo su humildad y su deseo de enfrentar a oponentes más fuertes. Esto lo llevó a participar en el Torneo de Poder, donde el destino de varios universos estaba en juego. Allí, Goku alcanzó su forma más impresionante: el Ultra Instinto, un estado en el que su cuerpo se mueve y lucha de forma completamente autónoma, sin que su mente interfiera. Con esta forma, Goku fue capaz de enfrentarse a Jiren, el guerrero más fuerte del Universo 11.

Aunque Goku ha salvado la Tierra y el universo en incontables ocasiones, su espíritu aventurero y su afán de superación lo mantienen siempre en movimiento. Para él, cada batalla es una oportunidad para aprender algo nuevo, perfeccionarse y acercarse más al límite de sus habilidades. Goku no pelea por venganza ni por el poder, pelea porque ama el desafío y el crecimiento personal que viene con cada nuevo enfrentamiento.

En definitiva, Son Goku es un héroe que ha trascendido las barreras del tiempo y el espacio, un guerrero con un corazón puro que siempre se esfuerza por proteger a sus amigos y seres queridos. Pero más allá de su inigualable fuerza, lo que realmente lo define es su deseo de superarse continuamente, y su inagotable amor por la aventura y el combate justo. Son Goku no solo es un guerrero, sino una leyenda viviente que inspira a todos aquellos que sueñan con superar sus propios límites.
"""

# Preprocesar el texto
tokenizer = tf.keras.preprocessing.text.Tokenizer(char_level=True)
tokenizer.fit_on_texts([corpus])
total_chars = len(tokenizer.word_index)

# Convertir el corpus a secuencias de caracteres
input_seq = []
target_seq = []
seq_length = 40

text_as_int = tokenizer.texts_to_sequences([corpus])[0]

for i in range(0, len(text_as_int) - seq_length):
    input_seq.append(text_as_int[i:i+seq_length])
    target_seq.append(text_as_int[i+1:i+seq_length+1])

# Convertir a arrays numpy
input_seq = np.array(input_seq)
target_seq = np.array(target_seq)

# Construir el modelo LSTM
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_chars + 1, 256, input_length=seq_length),
    tf.keras.layers.LSTM(256, return_sequences=True),
    tf.keras.layers.LSTM(256, return_sequences=True),
    tf.keras.layers.Dense(total_chars + 1, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), loss='sparse_categorical_crossentropy')

# Reshape de las etiquetas para que sean compatibles con la salida del modelo
target_seq = np.expand_dims(target_seq, -1)

# Entrenar el modelo
model.fit(input_seq, target_seq, epochs=20)

# Función para generar texto
def generar_texto(modelo, tokenizer, secuencia_inicial, longitud_texto=200):
    result = secuencia_inicial
    input_eval = [tokenizer.texts_to_sequences([secuencia_inicial])[0]]
    input_eval = tf.keras.preprocessing.sequence.pad_sequences(input_eval, maxlen=seq_length, truncating='pre')

    for i in range(longitud_texto):
        predictions = modelo.predict(input_eval)
        predicted_id = np.argmax(predictions, axis=-1)[0, -1]  # Seleccionar el último caracter predicho

        next_char = tokenizer.sequences_to_texts([[predicted_id]])[0]
        result += next_char

        input_eval = np.roll(input_eval, -1)
        input_eval[0, -1] = predicted_id

    return result

# Probar el modelo
secuencia_inicial = "¿Cuál es la receta para la mejor pizza?"
print(generar_texto(model, tokenizer, secuencia_inicial))