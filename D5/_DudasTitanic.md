# ¿Por qué...

## El número de árboles y el depth apenas afectan al accuracy

### 1. Modelo ya suficientemente entrenado. 

- **n_estimators** controla el número de árboles en el bosque. A partir de un cierto número, añadir más árboles no siempre mejora el rendimiento, ya que el modelo puede haber alcanzado una precisión estable.
- **max_depth** limita la profundidad de cada árbol. Si los árboles ya están lo suficientemente profundos para capturar la mayoría de las relaciones importantes en los datos, aumentar o reducir este valor no tendrá mucho efecto.

### 2. Datos no suficientemente complejos.

- En muchos casos, los datos pueden no ser lo suficientemente complejos como para beneficiarse de un ajuste fino de estos parámetros. Si los patrones en los datos son claros y simples, incluso un modelo con configuraciones moderadas de `n_estimators` y `max_depth` puede lograr un buen rendimiento.

### 3. Datos de baja calidad (limitados o desequilibrados)

- Si el conjunto de datos es relativamente pequeño o si está desequilibrado (por ejemplo, muchas más personas murieron que sobrevivieron en el Titanic), el impacto de ajustar los hiperparámetros puede ser mínimo. El modelo podría estar alcanzando una precisión cercana a la máxima posible con los datos disponibles.

### 4. Generalización u overfitting

- Aumentar el número de árboles o la profundidad de los árboles puede llevar a un modelo que se ajusta demasiado a los datos de entrenamiento (overfitting). Sin embargo, si el conjunto de validación no presenta mucha variabilidad, es posible que no se vea una mejora significativa en la precisión de validación. Además, en muchos casos, un número moderado de árboles y una profundidad limitada pueden ser suficientes para generalizar bien.

### 5. Interacción con otros hiperparámetros

- A veces, otros hiperparámetros como **min_samples_split**,** min_samples_leaf**, o el criterio de división (**criterion**) tienen un impacto más significativo que los ajustes en n_estimators y max_depth. Si esos otros parámetros están restringiendo el rendimiento del modelo, los cambios en estos dos no afectarán mucho.