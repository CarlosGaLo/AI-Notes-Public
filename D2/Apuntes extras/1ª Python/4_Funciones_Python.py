# 1. Funciones para Números

# abs(): Devuelve el valor absoluto de un número. 
num = -5
print(abs(num))  # Salida: 5

# round(): Redondea un número al número especificado de decimales.
num = 3.14159
print(round(num, 2))  # Salida: 3.14

# max(): Devuelve el valor máximo en un array o entre dos o más argumentos.
nums = [1, 2, 3, 4, 5]
print(max(nums))  # Salida: 5

# min(): Devuelve el valor mínimo en un array o entre dos o más argumentos.
print(min(nums))  # Salida: 1

# sum(): Devuelve la suma de todos los elementos en un array.
print(sum(nums))  # Salida: 15


# 2. Funciones para Cadenas de Caracteres

# len(): Devuelve la longitud de un objeto.
s = "hello"
print(len(s))  # Salida: 5

# str(): Convierte un objeto a una cadena de caracteres.
num = 123
print(str(num))  # Salida: '123'

# lower(): Convierte todos los caracteres de una cadena a minúsculas.
s = "HELLO"
print(s.lower())  # Salida: 'hello'

# upper(): Convierte todos los caracteres de una cadena a mayúsculas.
s = "hello"
print(s.upper())  # Salida: 'HELLO'

# replace(): Reemplaza una subcadena por otra.
s = "hello world"
print(s.replace("world", "there general Kenobi"))  # Salida: 'hello there'


# 3. Funciones para Listas y Arrays

# append(): Agrega un elemento al final de una lista.
lst = [1, 2, 3]
lst.append(4)
print(lst)  # Salida: [1, 2, 3, 4]

# extend(): Extiende una lista agregando todos los elementos de otro array.
lst.extend([5, 6])
print(lst)  # Salida: [1, 2, 3, 4, 5, 6]

# insert(): Inserta un elemento en una posición específica de la lista.
lst.insert(2, "insertado")
print(lst)  # Salida: [1, 2, 3, insertado, 4, 5, 6]

# pop(): Elimina y devuelve el elemento en una posición específica.
print(lst.pop(2))  # Salida: 3
print(lst)  # Salida: [1, 2, 3, 4, 5, 6]

# remove(): Elimina la primera ocurrencia de un valor en la lista.
lst.remove(3)
print(lst)  # Salida: [1, 2, 4, 5, 6]


# 4. Funciones para Manejo de Objetos y Clases

# type(): Devuelve el tipo del objeto.
s = "hello"
print(type(s))  # Salida: <class 'str'>

# isinstance(): Verifica si un objeto es una instancia de una clase o una tupla de clases.
# ¿Y eso qué es?
# Una instancia de clase es un objeto individual creado a partir de una clase. Las clases son como planos, modelos (de hecho así lo llamaremos más adelante) o moldes para crear objetos, y cada objeto creado a partir de una clase es una instancia de esa clase. Cuando creas una instancia, estás invocando el constructor de la clase, típicamente el método __init__.
# Una tupla de clases es simplemente una tupla (como en BBDD) que contiene una o más clases. Se usa a menudo en el contexto de funciones como isinstance() y issubclass() para verificar si un objeto es una instancia de alguna de las clases en la tupla. Esto es confuso pero no le dedicaremos mucho tiempo porque es una forma concreta de operar en Python. En java veremos las interfaces y la herencia, que nos servirá para un propósito parecido.
print(isinstance(s, str))  # Salida: True

# Creamos una clase sencilla para los siguientes ejemplos
class MyClass:
    def __init__(self):
        self.name = "MyClass"

# getattr(): Devuelve el valor de un atributo de un objeto.
obj = MyClass()
print(getattr(obj, 'name'))  # Salida: 'MyClass'

# setattr(): Establece el valor de un atributo de un objeto.
setattr(obj, 'name', 'NewName')
print(obj.name)  # Salida: 'NewName'

# hasattr(): Verifica si un objeto tiene un atributo específico.
print(hasattr(obj, 'name'))  # Salida: True