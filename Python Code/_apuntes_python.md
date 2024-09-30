# Introducción a la Lectura de Código en Python

## ¿Qué es Python?
Python es un lenguaje de programación de alto nivel, interpretado y con una sintaxis simple y fácil de aprender. 
Se utiliza en diversos campos, desde el desarrollo web hasta la ciencia de datos y la inteligencia artificial. 

Vamos a ver cómo funciona un poquito :)

---

## 1. Variables y Tipos de Datos

### 1.1 Definición de Variables
Una variable es un espacio en la memoria que guarda un valor. En Python, no es necesario declarar el tipo de la variable, ya que el lenguaje lo infiere automáticamente.

```python
nombre = "Juan"  # Una variable de tipo string
edad = 25        # Una variable de tipo entero
pi = 3.14159     # Una variable de tipo flotante
```

### 1.2 Tipos de Datos Básicos
- **int**: Representa números enteros, como `10` o `-3`.
- **float**: Números con decimales, como `3.14`.
- **str**: Cadenas de texto o caracteres, como `"Hola"`.
- **bool**: Valores booleanos, `True` o `False`.

---

En esencia, si aparece una palabra nueva que no habías visto antes, es porque se está declarando esa palabra como una variable y, de ahora en adelante, contendrá la información que le ha sido asignada. 

Si ponemos variable = cosa, lo que estamos diciendo es "oye, coge esa cosa y almacénala en la variable" o bien "haz que la variable sea igual a esa cosa".

## 2. Operaciones Básicas

### 2.1 Aritmética
Python permite operaciones aritméticas comunes.

```python
suma = 5 + 3        # Suma
resta = 5 - 3       # Resta
multiplicacion = 5 * 3  # Multiplicación
division = 5 / 3    # División, devuelve un float
modulo = 5 % 3      # Módulo, devuelve el resto de la división
```

---

## 3. Estructuras de Control
Las estructuras de control nos sirven para poder gestionar que suceda una cosa u otra en función a algo. 

Por ejemplo, cuando tu vas a salir a la calle cogerás el paragüas o no en función a si llueve. 
```python
if llueve:
    print("salgo con paragüas")
else:
    print("salgo a lo loco, que se vive mejor.")
```


### 3.1 Condicionales
Las estructuras condicionales permiten ejecutar código dependiendo de una condición.

```python
if edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### 3.2 Bucles
Los bucles permiten ejecutar una acción repetidamente.

#### Bucle `for`:

El for es particularmente importante porque es el bucle más común. Básicamente un for es decir "haz X durante Y veces".
Si yo te digo que le repartas un caramelo a cada uno de tus primos, se podría crear un bucle for así: 

```python
primos = ["Ana", "Luis", "Carlos", "Sofía"]

for primo in primos:
    print(f"Repartiendo un caramelo a {primo}")
```

```python
for i in range(5):
    print(i)  # Imprime del 0 al 4
```

#### Bucle `while`:
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

---

## 4. Funciones

Las funciones encapsulan código para reutilizarlo.

```python
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Juan"))
```

### 4.1 Parámetros y Retorno
Las funciones pueden recibir parámetros y devolver un valor.

```python
def suma(a, b):
    return a + b

resultado = suma(3, 4)  # Devuelve 7
```

---

## 5. Programación Orientada a Objetos (POO)

### 5.1 Clases y Objetos
Python es compatible con la POO, lo que permite crear clases para representar entidades con atributos y comportamientos.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre}"

persona1 = Persona("Juan", 25)
print(persona1.saludar())
```

### 5.2 Herencia
La herencia permite crear nuevas clases basadas en clases existentes.

```python
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
```

---

## 6. Manejo de Errores

En Python, puedes manejar errores usando `try`, `except`, y opcionalmente `finally`.

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
finally:
    print("Esta línea se ejecuta siempre")
```

---

## 7. Buenas Prácticas en Python

### 7.1 Nombrado de Variables
- Utiliza nombres descriptivos y claros: `precio_producto`, `numero_clientes`.
- Sigue las convenciones de Python, como `snake_case` para nombres de variables y funciones.

### 7.2 Comentarios
Añade comentarios para explicar código complejo, pero no abuses de ellos.

```python
# Esto es un comentario
# Calculamos el área del círculo
area = pi * radio ** 2
```

### 7.3 Módulos y Paquetes
Un módulo es un archivo de Python que contiene código, y un paquete es una colección de módulos. Esto permite organizar mejor los proyectos grandes.

```python
# En archivo saludo.py
def saludar():
    return "Hola"

# En otro archivo
import saludo
print(saludo.saludar())
```

---

## 8. Lectura de Código Avanzada

### 8.1 Comprensión de Listas
Permite crear listas de manera concisa.

Una **comprensión de listas** es una forma concisa y eficiente de crear listas en Python. Permite generar una nueva lista aplicando una operación a cada elemento de una secuencia o iterable, como una lista o un rango.

```python
cuadrados = [x**2 for x in range(10)]
```
#### ¿Qué hace este código?
- range(10):

    Esta función genera una secuencia de números enteros desde 0 hasta 9.
    Es decir, el bucle recorrerá los valores x = 0, 1, 2, 3, ..., 9.
    x**2:

    Para cada número x en el rango de 0 a 9, el código está elevando ese número al cuadrado.
    Esto significa que cada valor x se multiplicará por sí mismo.

- [x**2 for x in range(10)]:

    Esta es la estructura de la comprensión de listas. La parte x**2 es la operación que se aplica a cada elemento, y for x in range(10) es la manera de iterar sobre la secuencia de números de 0 a 9.
    En cada iteración, el resultado de x**2 se almacena en la nueva lista.


### 8.2 Decoradores
Un decorador es una función que modifica el comportamiento de otra función.

```python
def decorador(funcion):
    def nueva_funcion():
        print("Función decorada")
        funcion()
    return nueva_funcion

@decorador
def mi_funcion():
    print("Hola")

mi_funcion()
```

### 8.3 Context Managers
Permiten gestionar recursos como archivos de manera eficiente.

```python
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
```

---

## 9. Arquitectura Profesional en Python

### 9.1 Patrones de Diseño
Aprender patrones de diseño como el Patrón Singleton, el Patrón Observador, y otros, puede ser fundamental para entender aplicaciones a gran escala.

### 9.2 Principios SOLID
Estos principios ayudan a escribir código más limpio y escalable.

1. **S**: Responsabilidad Única (Single Responsibility Principle)
2. **O**: Abierto/Cerrado (Open/Closed Principle)
3. **L**: Sustitución de Liskov (Liskov Substitution Principle)
4. **I**: Segregación de Interfaces (Interface Segregation Principle)
5. **D**: Inversión de Dependencias (Dependency Inversion Principle)

### 9.3 Testing y Cobertura
El código profesional se acompaña de pruebas automáticas.

```python
import unittest

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

### 9.4 Lectura de Proyectos Reales
Para leer código a nivel profesional, es importante practicar con proyectos reales de código abierto, como los disponibles en GitHub.
