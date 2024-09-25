# Solución del Lab del terrario

# Solución a la última parte - guardar en archivo.
from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

#en 127.0.0.1 (o localhost) designamos un comportamiento por defecto.
# A esto del @app... se le llama "decorador" y los vamos a ver muy amenudo.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terrario', methods=['POST'])
def enviar():
    try:
        # Obtiene los datos del formulario
        data = request.get_json()
        nombre = data.get('nombre', '')
        habilidad = data.get('habilidad', '')

        if not nombre:
            return jsonify({'mensaje': 'Nombre no proporcionado'}), 400

        # Define el nombre del archivo y la ruta
        archivo = 'superheroes.json'
        
        # Si el archivo ya existe, lee su contenido
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                superheroes = json.load(f)
        else:
            superheroes = []
        
        # Agrega el nuevo superhéroe
        superheroes.append({'nombre': nombre, 'habilidad': habilidad})
        
        # Guarda los datos actualizados en el archivo
        with open(archivo, 'w') as f:
            json.dump(superheroes, f, indent=4)

        mensaje = f"Hola, {nombre}! Tu habilidad es {habilidad}."
        return jsonify({'mensaje': mensaje})

    except Exception as e:
        return jsonify({'mensaje': f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

# Paso 1: Definir la Clase `Terrario`
class Terrario:
    def __init__(self, nombre, ancho, largo):
        self.nombre = nombre
        self.ancho = ancho
        self.largo = largo
        self.habitantes = []

    def agregar_habitante(self, serpiente):
        self.habitantes.append(serpiente)

    def area(self):
        return self.ancho * self.largo
    
    def mostrar_serpientes(self):
        if not self.habitantes:
            print("El terrario está vacío.")
        else:
            print("Serpientes en el terrario:")
            for serpiente in self.habitantes:
                print(f"Nombre: {serpiente.nombre}, Longitud: {serpiente.longitud} metros, Especie: {serpiente.especie}")

# Paso 2: Definir la Clase `Serpiente`
class Serpiente:
    def __init__(self, nombre, longitud, especie):
        self.nombre = nombre
        self.longitud = longitud
        self.especie = especie

    def deslizarse(self):
        print(f"La serpiente {self.nombre} de la especie {self.especie} se está deslizando.")

# Paso 3: Crear Instancias y Probar

# Crear una instancia de la clase `Terrario`
mi_terrario = Terrario("Terrario Tropical", 5, 10)

# Crear instancias de la clase `Serpiente`
serpiente1 = Serpiente("Kaa", 2, "Python Reticulatus")
serpiente2 = Serpiente("Nagini", 3, "Python Molurus")

# Agregar las serpientes al terrario
mi_terrario.agregar_habitante(serpiente1)
mi_terrario.agregar_habitante(serpiente2)

# Calcular el área del terrario y mostrar el resultado
print(f"El área del terrario es: {mi_terrario.area()} metros cuadrados.")

# La serpiente se desliza
serpiente1.deslizarse()

# Mostrar todas las serpientes en el terrario
mi_terrario.mostrar_serpientes()

