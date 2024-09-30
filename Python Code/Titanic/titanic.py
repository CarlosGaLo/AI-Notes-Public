import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os

# Cargar los archivos locales
current_dir = os.path.dirname(os.path.abspath(__file__))
train_data_path = os.path.join(current_dir, 'train.csv')
test_data_path = os.path.join(current_dir, 'test.csv')

# Leer los datasets
train_data = pd.read_csv(train_data_path)
test_data = pd.read_csv(test_data_path)

# Mostrar algunas estadísticas iniciales de los datos
print(train_data.head())
print(test_data.head())

# Calcular el ratio de supervivencia de mujeres
women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women) / len(women)
print("% of women who survived:", rate_women)

# Calcular el ratio de supervivencia de hombres
men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men) / len(men)
print("% of men who survived:", rate_men)

# Calcular el ratio de supervivencia por clase
for pclass in [1, 2, 3]:
    passengers_in_class = train_data.loc[train_data.Pclass == pclass]["Survived"]
    survival_rate = sum(passengers_in_class) / len(passengers_in_class)
    print(f"Supervivencia en clase {pclass}: {survival_rate:.2%}")

# Ratio de supervivencia de mujeres en primera clase
women_first_class = train_data.loc[(train_data.Sex == 'female') & (train_data.Pclass == 1)]["Survived"]
rate_women_first_class = sum(women_first_class) / len(women_first_class)
print(f"Supervivencia de mujeres en primera clase: {rate_women_first_class:.2%}")

# Ratio de supervivencia de hombres en tercera clase
men_third_class = train_data.loc[(train_data.Sex == 'male') & (train_data.Pclass == 3)]["Survived"]
rate_men_third_class = sum(men_third_class) / len(men_third_class)
print(f"Supervivencia de hombres en tercera clase: {rate_men_third_class:.2%}")

# Función para calcular y mostrar el ratio de supervivencia para un grupo específico
def survival_rate_by_gender_and_class(sex, pclass):
    passengers = train_data.loc[(train_data.Sex == sex) & (train_data.Pclass == pclass)]["Survived"]
    return sum(passengers) / len(passengers)

# Supervivencia por clase y género
rate_women_first_class = survival_rate_by_gender_and_class('female', 1)
rate_men_first_class = survival_rate_by_gender_and_class('male', 1)
print(f"Supervivencia de mujeres en primera clase: {rate_women_first_class:.2%}")
print(f"Supervivencia de hombres en primera clase: {rate_men_first_class:.2%}")

rate_women_second_class = survival_rate_by_gender_and_class('female', 2)
rate_men_second_class = survival_rate_by_gender_and_class('male', 2)
print(f"Supervivencia de mujeres en segunda clase: {rate_women_second_class:.2%}")
print(f"Supervivencia de hombres en segunda clase: {rate_men_second_class:.2%}")

rate_women_third_class = survival_rate_by_gender_and_class('female', 3)
rate_men_third_class = survival_rate_by_gender_and_class('male', 3)
print(f"Supervivencia de mujeres en tercera clase: {rate_women_third_class:.2%}")
print(f"Supervivencia de hombres en tercera clase: {rate_men_third_class:.2%}")

# Modelado con RandomForest
from sklearn.ensemble import RandomForestClassifier

y = train_data["Survived"]
features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=1000, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

# Guardar las predicciones en un archivo CSV
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
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
