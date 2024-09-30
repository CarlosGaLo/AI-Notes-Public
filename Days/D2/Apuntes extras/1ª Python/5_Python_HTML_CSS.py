# ¡Recuerda instalar flask! 
# Recuerda también que Python se ejecuta en servidor mientras que JavaScript se puede ejecutar en navegador, por eso no podemos trabajar con ambos de la misma manera.
# Aquí lo que hacemos es montar un servidor para recibir los datos del formulario del otro archivo.

from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

#en 127.0.0.1 (o localhost) designamos un comportamiento por defecto.
# A esto del @app... se le llama "decorador" y los vamos a ver muy amenudo.
@app.route('/')
def index():
    peliculas = ["El señor de los anillos", "Kung-fu panda", "Deadpool 3"]
    data = {
        "dato":"ejemplo",
        "otroDato": "otroEjemplo",
        "pelis":peliculas,
        "numDePelis": len(peliculas)
    }
    return render_template('5_Python_HTML_CSS.html', data=data) # No hace falta indicar el nombre de la carpeta, porque flask ya sabe que tiene que mirar dentro de "templates".
    # También le estamos pasando el diccionario (un objeto) llamado data mediante el parámetro con su mismo nombre. Que se llamen igual no es obligatorio.

@app.route('/enviar', methods=['POST'])
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


