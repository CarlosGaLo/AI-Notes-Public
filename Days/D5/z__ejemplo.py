import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os

# Cargar los archivos locales
current_dir = os.path.dirname(os.path.abspath(__file__))
train_data_path = os.path.join(current_dir, 'z_train.csv')
test_data_path = os.path.join(current_dir, 'z_test.csv')

# Leer los datasets
train_data = pd.read_csv(train_data_path)
test_data = pd.read_csv(test_data_path)

# Mostrar algunas estadísticas iniciales de los datos
print(train_data.head())
print(test_data.head())

# Modelado con RandomForest
from sklearn.ensemble import RandomForestClassifier

# La columna objetivo es 'finalizaCompra'
y = train_data["finalizaCompra"]

# Definir las características (features) a utilizar en el modelo
# A continuación seleccionamos las columnas que se utilizarán como características
features = ["mensualidad", "edad", "sexo", "tieneHijos", "tienePadres", "empleado", "KPIValue", "Madrid", "cochePropio", "carnet", "moto", "referido", "altura", "peso", "veDragonBall"]
#features = train_data.drop(columns=["finalizaCompra"]).columns

# Convertir variables categóricas en numéricas con pd.get_dummies (si corresponde)
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

# Asegurarse de que X y X_test tienen las mismas columnas después de la transformación
X, X_test = X.align(X_test, join='left', axis=1, fill_value=0)

# Crear y entrenar el modelo RandomForest
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)

# Realizar predicciones en el set de test
predictions = model.predict(X_test)

# Guardar las predicciones en un archivo CSV
output = pd.DataFrame({'clienteId': test_data.clienteId, 'finalizaCompra': predictions})
output.to_csv(os.path.join(current_dir, 'submission.csv'), index=False)
print("Your submission was successfully saved!")

# División de los datos para validación
from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Evaluación del modelo
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_valid)
accuracy = accuracy_score(y_valid, y_pred)
print(f'Accuracy: {accuracy}')

# ¿Ves que tenemos un accuracy enorme? Tiene trampa. ¡Estamos usando el mismo archivo para casi todo! Vamos a continuar viéndolo en ejemplo_continuación.