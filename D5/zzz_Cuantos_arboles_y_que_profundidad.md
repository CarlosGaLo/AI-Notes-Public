
# Optimización de Random Forest: Número de Árboles y Profundidad (Con mates)

## 1. **Grid Search**:
El uso de una búsqueda en cuadrícula (Grid Search) te permite probar diferentes combinaciones de hiperparámetros para optimizar el modelo. Los parámetros que puedes ajustar incluyen:

- **`n_estimators`**: Número de árboles en el bosque.
- **`max_depth`**: Profundidad máxima de los árboles.
- **`min_samples_split`**: El número mínimo de muestras necesarias para dividir un nodo.
- **`min_samples_leaf`**: El número mínimo de muestras necesarias en una hoja.

Ejemplo **`GridSearchCV`** de `sklearn`:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Definir el modelo base
rf = RandomForestClassifier()

# Definir el grid de parámetros
param_grid = {
    'n_estimators': [50, 100, 200],  # número de árboles
    'max_depth': [None, 10, 20, 30],  # profundidad máxima
    'min_samples_split': [2, 5, 10],  # número mínimo de muestras para dividir un nodo
    'min_samples_leaf': [1, 2, 4],  # número mínimo de muestras por hoja
}

# Configurar la búsqueda en cuadrícula con validación cruzada
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='accuracy', verbose=2, n_jobs=-1)

# Entrenar la búsqueda
grid_search.fit(X_train, y_train)

# Obtener los mejores parámetros
print("Mejores parámetros:", grid_search.best_params_)
```

## 2. **Randomized Search**:
Parecido a `GridSearchCV`, pero en lugar de probar todas las combinaciones posibles, selecciona aleatoriamente algunas para hacer la búsqueda más rápida:

```python
from sklearn.model_selection import RandomizedSearchCV

# Definir el grid de parámetros
param_dist = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

# Configurar la búsqueda aleatoria
random_search = RandomizedSearchCV(estimator=rf, param_distributions=param_dist, n_iter=10, cv=5, scoring='accuracy', verbose=2, n_jobs=-1)

# Entrenar la búsqueda
random_search.fit(X_train, y_train)

# Obtener los mejores parámetros
print("Mejores parámetros:", random_search.best_params_)
```

## 3. **Curva de Validación**:
Otra opción es generar una curva de validación que muestre cómo varía el rendimiento del modelo al cambiar el número de árboles (`n_estimators`) y la profundidad (`max_depth`)..

```python
from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt
import numpy as np

# Definir los valores a probar para n_estimators
param_range = np.arange(1, 200, 10)

# Generar la curva de validación
train_scores, test_scores = validation_curve(
    RandomForestClassifier(),
    X_train, y_train,
    param_name="n_estimators",
    param_range=param_range,
    cv=5,
    scoring="accuracy"
)

# Calcular la media y desviación estándar para los conjuntos de entrenamiento y validación
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

# Graficar la curva de validación
plt.plot(param_range, train_mean, label="Entrenamiento", color="r")
plt.plot(param_range, test_mean, label="Validación", color="g")

plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, alpha=0.2, color="r")
plt.fill_between(param_range, test_mean - test_std, test_mean + test_std, alpha=0.2, color="g")

plt.title("Curva de Validación")
plt.xlabel("Número de árboles")
plt.ylabel("Exactitud")
plt.legend(loc="best")
plt.show()
```

## 4. **Tener en cuenta el riesgo de sobreajuste**:
- Si **n_estimators** es demasiado bajo, el modelo puede ser poco robusto (bajo rendimiento).
- Si **max_depth** es muy alto, puede sobreajustarse (overfitting) a los datos de entrenamiento y no generalizar bien.

Por eso, un buen valor de `max_depth` suele ser uno que no sea muy profundo y permita una buena generalización.

Estas estrategias te ayudarán a identificar los parámetros óptimos para tu modelo de Random Forest.

A continuación, vamos a verlo sin tanta matemática ni herramientas, simplemente a nivel conceptual :)

# ¿Cuántos árboles y qué profundidad debería tener un Random Forest? (Sin mates)

A nivel general y sin entrar en matemáticas profundas, puedes estimar el número de árboles y la profundidad de un **Random Forest** basándote en algunas consideraciones prácticas y el comportamiento típico del modelo.

## 1. Número de árboles (`n_estimators`)
   - **Más árboles tienden a mejorar la estabilidad del modelo**, pero el beneficio marginal disminuye después de cierto punto. Esto significa que agregar más árboles después de cierto número no mejorará mucho el rendimiento.
   - **Recomendación general**: un rango de **100 a 300 árboles** suele ser suficiente para la mayoría de los casos. Aumentar más allá de este punto puede traer mejoras muy pequeñas, a menos que tengas muchos datos y un problema complejo.
   - **Consideraciones prácticas**:
     - Si tienes **muchos datos** o el problema es complejo, puedes aumentar el número de árboles a 500 o incluso 1000 para mejorar la robustez del modelo.
     - Si **el tiempo de entrenamiento es un factor importante**, empezar con 100 árboles es un buen punto de partida.

## 2. Profundidad máxima de los árboles (`max_depth`)
   - **La profundidad controla cuánto puede crecer cada árbol individualmente**. Si la profundidad es muy baja, el árbol será poco flexible y no capturará patrones complejos; si es muy alta, el árbol puede sobreajustarse.
   - **Recomendación general**: una profundidad moderada, como entre **10 y 30 niveles**, suele ser adecuada.
   - **Consideraciones prácticas**:
     - Para conjuntos de datos más simples o con menos ruido, puedes optar por una profundidad mayor.
     - Para datos más complejos o ruidosos, es mejor limitar la profundidad para evitar el sobreajuste.

## 3. Relación entre número de árboles y profundidad
   - **Más árboles y menor profundidad**: Si ajustas los árboles para que tengan menos profundidad, puedes compensar esto aumentando el número de árboles. Esta combinación tiende a hacer que el modelo sea más generalizable y robusto frente a los datos.
   - **Menos árboles y mayor profundidad**: Si permites que los árboles crezcan más (más profundidad), no necesitas tantos árboles, pero corres el riesgo de que cada árbol aprenda demasiado de los datos de entrenamiento, lo que puede llevar a un sobreajuste.

## 4. Tamaño del conjunto de datos
   - Si tienes un **conjunto de datos pequeño**, no necesitas tantos árboles ni una gran profundidad, ya que los patrones son más fáciles de aprender.
   - Para **conjuntos de datos grandes o más complejos**, se recomienda aumentar ambos (número de árboles y profundidad), pero siempre con precaución de no caer en el sobreajuste.

## 5. Tipo de problema
   - Para **clasificación** (cuando el resultado es una categoría), puedes empezar con un número moderado de árboles (alrededor de 100) y una profundidad limitada (alrededor de 10-20 niveles).
   - Para **regresión** (cuando el resultado es un valor continuo), la profundidad suele ser más crítica, ya que es importante ajustar mejor los datos, pero aún así es mejor no dejar que crezca sin límite.

## 6. Estrategia de ajuste progresivo
   - **Comienza con valores pequeños/moderados**. Por ejemplo, comienza con 100 árboles y una profundidad máxima de 10.
   - **Aumenta gradualmente**. Si notas que el modelo no está rindiendo bien, aumenta el número de árboles a 200 y la profundidad a 20.
   - **Observa si el modelo mejora significativamente**. Si después de aumentar el número de árboles o la profundidad, el rendimiento del modelo mejora poco, es una señal de que has alcanzado un punto de estabilidad.

### Resumen de reglas prácticas:
- **Número de árboles**: Comienza con **100 a 300**. Aumenta si el rendimiento es inestable.
- **Profundidad**: Comienza con una profundidad de **10 a 20 niveles**. Ajusta si necesitas más flexibilidad o si ves señales de sobreajuste.
- **Recuerda el equilibrio**: Un número mayor de árboles mejora la estabilidad del modelo, mientras que una profundidad más moderada ayuda a evitar el sobreajuste.

Este enfoque empírico te ayudará a tener una idea inicial de cómo configurar tu modelo sin entrar en cálculos demasiado detallados. Luego, puedes afinar con herramientas como **Grid Search** o **Randomized Search**, que son las que hemos visto arriba, para encontrar el ajuste más preciso.
