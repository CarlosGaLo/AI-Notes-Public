# Glosario de Términos de Python

## Variables
- **Variable**: Un contenedor para almacenar valores, que puede ser de diferentes tipos de datos.
- **Asignación**: El proceso de darle un valor a una variable.

```python
x = 5  # Asignación de una variable
```

## Tipos de datos
- **int**: Representa números enteros, como `5` o `-10`.
- **float**: Números decimales como `3.14` o `-0.001`.
- **str**: Cadenas de texto o caracteres. Se definen entre comillas simples o dobles.
- **bool**: Valores booleanos que solo pueden ser `True` o `False`.
- **list**: Una estructura de datos mutable que puede contener múltiples valores.
- **tuple**: Una estructura de datos inmutable.
- **dict**: Un conjunto de pares clave-valor, útil para datos etiquetados.
- **set**: Colección desordenada sin elementos duplicados.

En python no hace falta anunciar qué tipo de dato tiene cada variable. Eso nos hace la vida más fácil pero también hay que tener más cuidadín a la hora de programar.

```python
a = 42         # int
b = 3.14       # float
c = "Hola"     # str
d = True       # bool
lista = [1, 2, 3, 4]  # list
tupla = (1, 2, 3)     # tuple
diccionario = {"clave": "valor"}  # dict
conjunto = {1, 2, 3}  # set
```

## Operadores
- **Aritméticos**: `+`, `-`, `*`, `/`, `//`, `%`, `**` (suma, resta, multiplicación, división, división entera, módulo, exponente).
- **Relacionales**: `==`, `!=`, `>`, `<`, `>=`, `<=` (comparación).
- **Lógicos**: `and`, `or`, `not` (operaciones lógicas).
- **Asignación**: `=`, `+=`, `-=`, `*=`, `/=` (operadores compuestos).

```python
x = 5
y = 3
z = x + y  # Aritmético
resultado = (x > y) and (y < 10)  # Lógico
```

## Estructuras de control
- **if/elif/else**: Condicionales para ejecutar código basado en una condición.
- **for**: Bucle que itera sobre secuencias.
- **while**: Bucle que se ejecuta mientras una condición sea verdadera.
- **break**: Sale del bucle.
- **continue**: Salta a la siguiente iteración del bucle.

```python
if x > y:
    print("x es mayor que y")
for i in range(5):
    print(i)
while x < 10:
    x += 1
    if x == 8:
        break
```

## Funciones
- **Función**: Bloque de código reutilizable que realiza una tarea específica.
- **Argumento**: Valor pasado a una función.
- **Parámetro**: Variable en la definición de la función.
- **return**: Devuelve un valor de una función.

```python
def suma(a, b):
    return a + b
resultado = suma(3, 5)
```

## Clases y objetos
- **Clase**: Plantilla para crear objetos.
- **Objeto**: Instancia de una clase.
- **Método**: Función definida dentro de una clase.
- **Atributo**: Variable definida dentro de una clase.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"

persona1 = Persona("Carlos", 30)
print(persona1.saludar())
```

## Excepciones
- **Excepción**: Evento que interrumpe el flujo normal del código.
- **try/except**: Bloque de manejo de errores.

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
```

## Módulos
- **Módulo**: Archivo que contiene definiciones y declaraciones de Python.
- **import**: Permite importar un módulo para usar sus funciones y clases.
- **from**: Permite importar elementos específicos de un módulo.

```python
import math
resultado = math.sqrt(16)

from math import pi
print(pi)
```

## Listas por comprensión
- **List comprehension**: Sintaxis concisa para crear listas.
  
```python
cuadrados = [x**2 for x in range(10)]
```

## Decoradores
- **Decorador**: Función que modifica el comportamiento de otra función.
  
```python
def decorador(funcion):
    def nueva_funcion():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return nueva_funcion

@decorador
def funcion_principal():
    print("Función principal")

funcion_principal()
```

## Generadores
- **Generador**: Función que devuelve un objeto iterable y permite iterar sobre una secuencia de valores.

```python
def generador():
    for i in range(3):
        yield i

for valor in generador():
    print(valor)
```

## Tabla Resumen de Términos

| Término             | Descripción                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Variable**         | Contenedor para almacenar un valor.                                         |
| **int**              | Tipo de dato entero.                                                       |
| **float**            | Tipo de dato decimal.                                                      |
| **str**              | Cadena de texto.                                                           |
| **bool**             | Tipo booleano (`True` o `False`).                                           |
| **list**             | Lista de elementos mutables.                                                |
| **tuple**            | Tupla de elementos inmutables.                                              |
| **dict**             | Diccionario de pares clave-valor.                                           |
| **set**              | Conjunto sin elementos duplicados.                                          |
| **if/elif/else**     | Condicional para ejecutar código según una condición.                       |
| **for**              | Bucle que itera sobre secuencias.                                           |
| **while**            | Bucle que se ejecuta mientras una condición sea verdadera.                  |
| **break**            | Rompe un bucle antes de su finalización.                                    |
| **continue**         | Salta a la siguiente iteración de un bucle.                                 |
| **Función**          | Bloque de código reutilizable que realiza una tarea.                        |
| **Clase**            | Plantilla para crear objetos.                                               |
| **Objeto**           | Instancia de una clase.                                                     |
| **try/except**       | Bloque para el manejo de excepciones o errores.                             |
| **import**           | Permite importar módulos.                                                   |
| **Generador**        | Función que devuelve valores de uno en uno, usando `yield`.                 |
| **Decorador**        | Función que modifica el comportamiento de otra función.                     |
| **List comprehension** | Sintaxis para crear listas de forma concisa.                              |

# Cómo instalar pip
En visual studio code abre el terminal y escribe lo siguiente:

`python -m ensurepip --default-pip`

Si pip está instalado, te mostrará la versión actual. Si no, el comando lo instalará.

# Las librerías pandas y numpy

Para poder instalar las librerías, recuerda usar en terminal las siguientes instrucciones.

`pip install pandas`
`pip install numpy scikit-learn`