import requests

# Definir la URL a la que se hará la solicitud
url = 'https://pokeapi.co/api/v2/pokemon/ditto'

try:
    # Realizar la solicitud GET a la URL
    respuesta = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        datos = respuesta.json()
        
        # Imprimir los datos obtenidos
        print("Datos obtenidos:")
        print(datos.get("name")) # Tenemos que usar la función "get" para extraer los datos. Esto es porque Python funciona por diccionarios.
    else:
        print(f"Error: No se pudo obtener la información (código de estado {respuesta.status_code})")

except requests.exceptions.RequestException as e:
    print(f"Se produjo un error al hacer la solicitud: {e}")