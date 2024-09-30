import os
import pandas as pd
#pip install faker
from faker import Faker
import random

# Inicializar Faker para generar nombres reales
fake = Faker('es_ES')

# Definir características del dataset
provincias = ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Málaga']
nacionalidades = ['Español', 'Argentino', 'Colombiano', 'Mexicano', 'Venezolano']
estudios = ['Primaria', 'Secundaria', 'Bachillerato', 'Universidad', 'Postgrado']

def generate_data(num_rows):
    data = []
    for clienteId in range(num_rows):
        finalizaCompra = random.randint(0, 1)
        mensualidad = round(random.uniform(10, 150), 2)
        nombre = fake.name()
        edad = random.randint(18, 65)
        sexo = random.choice(['male', 'female'])
        tieneHijos = random.randint(0, 1)
        tienePadres = random.randint(0, 1)
        provincia = random.choice(provincias)
        nacionalidad = random.choice(nacionalidades)
        nivel_estudios = random.choice(estudios)
        viajeAnual = random.randint(0, 2)
        empleado = random.choices([0, 1], weights=[85, 15])[0]
        KPIValue = round(random.uniform(0, 100), 2)
        Madrid = 1 if provincia == 'Madrid' else 0
        cochePropio = random.randint(0, 1)
        carnet = 1 if cochePropio else 0
        moto = random.randint(0, 1)
        referido = random.randint(0, 1)
        altura = random.randint(150, 200)  # en cm
        peso = random.randint(50, 100)     # en kg
        veDragonBall = random.randint(0, 1)

        data.append([clienteId, finalizaCompra, mensualidad, nombre, edad, sexo, tieneHijos, tienePadres, provincia, nacionalidad, 
                     nivel_estudios, viajeAnual, empleado, KPIValue, Madrid, cochePropio, carnet, moto, referido, altura, peso, veDragonBall])
    
    # Crear DataFrame
    df = pd.DataFrame(data, columns=['clienteId', 'finalizaCompra', 'mensualidad', 'nombre', 'edad', 'sexo', 
                                     'tieneHijos', 'tienePadres', 'provincia', 'nacionalidad', 'estudios', 
                                     'viajeAnual', 'empleado', 'KPIValue', 'Madrid', 'cochePropio', 
                                     'carnet', 'moto', 'referido', 'altura', 'peso', 'veDragonBall'])
    return df

# Determinar la ubicación actual del archivo para guardar el archivo CSV generado
current_dir = os.path.dirname(os.path.abspath(__file__))

# Generar 10000 filas para z_test
z_test = generate_data(10000)
z_test.to_csv(os.path.join(current_dir, 'generated.csv'), index=False)