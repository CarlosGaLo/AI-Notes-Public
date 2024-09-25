import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier

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

# Definir la columna objetivo y las características para el entrenamiento
y_train = train_data["finalizaCompra"]
features = train_data.drop(columns=["finalizaCompra"]).columns
X_train = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data)

# Asegurarse de que X_train y X_test tienen las mismas columnas después de la transformación
X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

# Crear y entrenar el modelo RandomForest con todo el z_train
model = RandomForestClassifier(n_estimators=10, max_depth=2, random_state=1)
model.fit(X_train, y_train)

# Realizar predicciones en el set de test
predictions = model.predict(X_test)

# Guardar las predicciones en un archivo CSV
output = pd.DataFrame({'clienteId': test_data.index, 'finalizaCompra': predictions})  # Asumiendo que clienteId es el índice si no hay tal columna
output.to_csv(os.path.join(current_dir, 'z_submission.csv'), index=False)
print("Your submission was successfully saved!")