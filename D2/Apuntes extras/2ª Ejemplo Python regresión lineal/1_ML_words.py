# Importar las bibliotecas necesarias
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Cargar el dataset de noticias
newsgroups = fetch_20newsgroups(subset='all')
X, y = newsgroups.data, newsgroups.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Crear un pipeline que incluye el vectorizador y el clasificador
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Imprimir algunas predicciones de ejemplo
for i in range(5):
    print(f"Actual: {newsgroups.target_names[y_test[i]]}")
    print(f"Predicted: {newsgroups.target_names[y_pred[i]]}")
    print(f"Text: {X_test[i][:200]}...\n")