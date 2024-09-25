import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Parte 1: Entrenamiento del modelo y evaluación de la eficacia
# ---------------------------------------------------------------

# Cargar los archivos locales
current_dir = os.path.dirname(os.path.abspath(__file__))
train_data_path = os.path.join(current_dir, 'z_train.csv')
test_data_path = os.path.join(current_dir, 'z_test.csv')

# Leer los datasets
train_data = pd.read_csv(train_data_path)
test_data = pd.read_csv(test_data_path)

# Mostrar algunas estadísticas iniciales de los datos
print("Datos de entrenamiento:")
print(train_data.head())
print("Datos de prueba:")
print(test_data.head())

# La columna objetivo es 'finalizaCompra'
y = train_data["finalizaCompra"]

# Definir las características (features) a utilizar en el modelo
features = ["mensualidad", "edad", "sexo", "tieneHijos", "tienePadres", "empleado", "KPIValue", 
            "Madrid", "cochePropio", "carnet", "moto", "referido", "altura", "peso", "veDragonBall"]

# Convertir variables categóricas en numéricas con pd.get_dummies (si corresponde)
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

# Asegurarse de que X y X_test tienen las mismas columnas después de la transformación
X, X_test = X.align(X_test, join='left', axis=1, fill_value=0)

# División de los datos para validación
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo RandomForest
# Vamos a declarar aquí el número de árboles y la profundidad, para luego reutilizarlo. Así no nos arriesgamos a equivocarnos.
# Voy a poner una lista grande de comentarios aquí para que sea fácil volver a esta línea :) así cuando veas mucho verde, sabrás que es el lugar del bosque!
#
#
#
#
#
#
#
#
arboles = 1000
profundidad = 10
model = RandomForestClassifier(n_estimators=arboles, max_depth=profundidad, random_state=1)
model.fit(X_train, y_train)

## OJO ABSOLUTO! Si vas a crear muchos árboles con mucha profundidad deberías aumentar la cantidad de núcleos de tu PC para el cálculo. Para eso usamos la propiedad n_jobs
# Si usas dicha propiedad comenta las líneas 56 y 57 y descomenta las líneas 62 y 63
#model = RandomForestClassifier(n_estimators=arboles, max_depth=profundidad, random_state=1, n_jobs=-1)
#model.fit(X_train, y_train)

#### ¿Cuáles son unos valores razonables?
## Depende mucho de tu muestra. Pero, por norma general, 1000 a 5000 árboles y 10 a 20 de profundidad suelen dar buenos resultados.

# Evaluar el modelo en los datos de validación
y_pred = model.predict(X_valid)
accuracy = accuracy_score(y_valid, y_pred)
print(f'Accuracy en el conjunto de validación: {accuracy}')

# Parte 2: Aplicación del modelo sobre el conjunto de test
# ---------------------------------------------------------------

# Entrenamos nuevamente el modelo con todos los datos de entrenamiento
model.fit(X, y)

# Realizar predicciones en el set de test
predictions = model.predict(X_test)

# Guardar las predicciones en un archivo CSV
output = pd.DataFrame({'clienteId': test_data.clienteId, 'finalizaCompra': predictions})
output.to_csv(os.path.join(current_dir, 'z_submission_final.csv'), index=False)
print("Your submission was successfully saved!")

# Parte 3: Entrenamiento y predicción con diferentes parámetros
# ---------------------------------------------------------------

# Definir nuevamente la columna objetivo y las características para el entrenamiento completo
y_train = train_data["finalizaCompra"]
features_full = train_data.drop(columns=["finalizaCompra"]).columns
X_train_full = pd.get_dummies(train_data[features_full])
X_test_full = pd.get_dummies(test_data)

# Asegurarse de que X_train_full y X_test_full tienen las mismas columnas
X_train_full, X_test_full = X_train_full.align(X_test_full, join='left', axis=1, fill_value=0)

# Crear y entrenar el modelo RandomForest con diferentes parámetros
model_full = RandomForestClassifier(n_estimators=arboles, max_depth=profundidad, random_state=1)
model_full.fit(X_train_full, y_train)

# Realizar predicciones en el set de test completo
predictions_full = model_full.predict(X_test_full)

# Guardar las predicciones en un archivo CSV
output_full = pd.DataFrame({'clienteId': test_data.index, 'finalizaCompra': predictions_full})
output_full.to_csv(os.path.join(current_dir, 'z_submission.csv'), index=False)
print("Your full submission was successfully saved!")
