# Introducción a Python

## Cómo declarar variables

### Variables

En Python, las variables se declaran simplemente asignando un valor a un nombre de variable. No se necesita especificar el tipo de dato.

```python
x = 10          # Variable entera. Y de paso, así se ponen comentarios ;)
nombre = "Ana"  # Variable de cadena
pi = 3.14       # Variable flotante
```

### Arrays

En Python, los arrays se manejan usando listas. Una lista puede contener elementos de diferentes tipos de datos.

```python
numeros = [1, 2, 3, 4, 5]                # Lista de enteros
frutas = ["manzana", "banana", "cereza"]  # Lista de cadenas
mezcla = [1, "dos", 3.0, True]           # Lista de diferentes tipos de datos
```

### Objetos

En Python, los objetos son instancias de clases. Se utilizan para representar entidades y sus comportamientos. Aquí la palabra "objeto" cobra otro valor.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

persona1 = Persona("Luis", 30)
print(persona1.saludar())
```

### Diccionarios

En Python un diccionario es bastante similar a un objeto en JavaScript en términos de funcionalidad. Ambos permiten almacenar datos en pares clave-valor y acceder a estos valores mediante sus claves.

#### Ejemplo comparativo

##### Python example

```python
# Crear un diccionario
persona = {
    'nombre': 'Ana',
    'edad': 28,
    'ciudad': 'Barcelona'
}

# Acceder a un valor
print(persona['nombre'])  # Output: Ana

# Añadir un nuevo par clave-valor
persona['profesion'] = 'Diseñadora'

# Eliminar un par clave-valor
del persona['ciudad']
```

##### Javascript example

```javascript
// Crear un objeto
const persona = {
  nombre: "Ana",
  edad: 28,
  ciudad: "Barcelona",
};

// Acceder a un valor
console.log(persona.nombre); // Output: Ana

// Añadir un nuevo par clave-valor
persona.profesion = "Diseñadora";

// Eliminar un par clave-valor
delete persona.ciudad;
```

### ¡Importante! Sobre la nomenclatura

A la hora de poner nombres la cosa se puede poner más complejo de lo que parece. Nosotros, para poder centrarnos en la programación, vamos a mantener un perfil bajo respecto a las definiciones técnicas de las cosas cuando hablemos. Te digo las definiciones simples que vamos a usar en el bootcamp para:

#### Cuando hablemos de JS

    - Objeto: Una colección de pares clave-valor. Puede contener propiedades y métodos.
    - Diccionario: No aplicable directamente en JS. El concepto más cercano es el objeto, aunque los diccionarios en otros lenguajes son más específicos.
    - Instancia: Un objeto creado a partir de una función constructora o clase. (igual en todos)
    - Modelo: Generalmente es una función constructora o clase que define la estructura y el comportamiento de los objetos.
    - Clase: Una función constructora o un esquema para crear objetos, que puede definir propiedades y métodos.

#### Cuando hablemos de Python

    - Objeto: Una instancia de una clase, que puede contener atributos y métodos.
    - Diccionario: Una estructura de datos que almacena pares clave-valor, similar a un objeto en JS pero solo para datos.
    - Instancia: Un objeto creado a partir de una clase. (igual en todos)
    - Modelo: Generalmente se refiere a una clase que define la estructura y el comportamiento de las instancias. Vamos, sinónimo de clase. Es la base para la comunicación con la DB.
    - Clase: Un molde o plantilla para crear objetos, que puede definir atributos y métodos.

#### Cuando hablemos de Java

    - Objeto: Una instancia de una clase, que puede contener atributos y métodos.
    - Diccionario: No aplicable directamente en Java. La estructura más cercana sería HashMap o Hashtable.
    - Instancia: Un objeto creado a partir de una clase. (igual en todos)
    - Modelo: Generalmente se refiere a una clase que define la estructura y el comportamiento de los objetos. Es la base para la comunicación con la DB.
    - Clase: Un molde o plantilla para crear objetos, que define atributos y métodos y puede ser utilizada para instanciar objetos.

## Cómo realizar:

### If

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
```

### If else

```python
edad = 16
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

### switch

```python
def dia_de_la_semana(dia):
    opciones = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return opciones.get(dia, "Día inválido")

print(dia_de_la_semana(3))  # Imprime "Miércoles"
```

### while

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### for

```python
for i in range(5):
    print(i)
```

### fetch

```python
import requests

response = requests.get('https://api.example.com/data')
data = response.json()
print(data)
```

```python
import requests

# Definir la URL a la que se hará la solicitud
url = 'https://pokeapi.co/api/v2/pokemon/ditto'

try:
    # Realizar la solicitud GET a la URL
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        datos = respuesta.json()

        # Imprimir los datos obtenidos
        print("Datos obtenidos:")
        print(datos)
    else:
        print(f"Error: No se pudo obtener la información (código de estado {respuesta.status_code})")

except requests.exceptions.RequestException as e:
    print(f"Se produjo un error al hacer la solicitud: {e}")
```

## Cómo declarar funciones

Las funciones se declaran utilizando la palabra clave def seguida del nombre de la función y paréntesis.

```python
def mi_funcion(parametro1, parametro2):
    # Código de la función
    return resultado
```

### Ejemplo de funciones

```python
import math

def calcular_radio(circulo_area):
    radio = math.sqrt(circulo_area / math.pi)
    return radio

area = 50
print(calcular_radio(area))

def multiplicar(n1, n2):
    return n1 * n2

resultado = multiplicar(5, 3)
print(resultado)

def sustituir_cadena(cadena):
    return cadena.replace(cadena, "ironPython")

cadena_original = "Texto de ejemplo"
print(sustituir_cadena(cadena_original))
```

## Qué tipo de lenguaje es

Python es un lenguaje de programación de alto nivel, interpretado (no compilado, como Java, que lo veremos en el siguiente módulo. Es más cercano a JS), y de propósito general. Es conocido por su sintaxis clara y legible, lo que facilita el desarrollo rápido de aplicaciones. Python soporta múltiples paradigmas de programación, incluyendo la programación orientada a objetos, la programación imperativa y la programación funcional.

### Qué es programación imperativa

La **programación imperativa** es un paradigma de programación que se basa en describir una serie de instrucciones secuenciales que cambian el estado del programa. En este enfoque, el programador especifica los pasos exactos que la computadora debe seguir para alcanzar un objetivo. Es la programación "de toda la vida de Dios", la primera, la más básica, directa e intuitiva.

**Características clave:**

- **Secuencialidad:** El flujo de control es determinista y sigue un orden secuencial.
- **Modificación del estado:** El programa cambia el estado del sistema mediante la asignación de valores a variables y la ejecución de instrucciones.
- **Uso de variables y estructuras de control:** Utiliza variables para almacenar datos y estructuras de control como bucles (`for`, `while`) y condicionales (`if`, `else`) para dirigir la ejecución.

### Qué es programación funcional

La **programación funcional** es un paradigma de programación que trata a las funciones como ciudadanos de primera clase y promueve el uso de funciones puras. En este enfoque, el cálculo se realiza mediante la evaluación de funciones y la composición de estas funciones. En esencia es dividir la programación imperativa en pequeños bloques (las funciones) y usarlas y reusarlas continuamente para generar otros tipos de lógica.

**Características clave:**

- **Funciones como ciudadanos de primera clase:** Las funciones pueden ser pasadas como argumentos, devueltas como valores, y asignadas a variables.
- **Inmutabilidad:** Se fomenta el uso de datos inmutables, evitando cambios en el estado del programa.
- **Funciones puras:** Las funciones puras no tienen efectos secundarios y su salida depende únicamente de sus entradas.
- **Composición de funciones:** Las funciones pueden ser combinadas para construir operaciones más complejas.

### Qué es programación orientada a objetos

La **programación orientada a objetos (POO)** es un paradigma de programación que organiza el software en "objetos", que son instancias de "clases". Cada objeto puede contener datos y métodos que operan sobre esos datos. La POO facilita la organización del código y promueve la reutilización y la modularidad.

**Características clave:**

- **Clases y Objetos:** Las clases son plantillas para crear objetos, que son instancias de esas clases.
- **Encapsulación:** Los datos y métodos que operan sobre esos datos están agrupados en una sola unidad (la clase), y el acceso a esos datos se controla mediante métodos públicos y privados.
- **Herencia:** Permite crear nuevas clases basadas en clases existentes, heredando sus propiedades y comportamientos.
- **Polimorfismo:** Permite que diferentes clases puedan ser tratadas a través de una interfaz común, con diferentes implementaciones para métodos similares.

### Ejemplos de Código

```python
# Programación imperativa
x = 0            # Inicialización de una variable
while x < 5:     # Bucle que se ejecuta mientras x sea menor que 5
    print(x)     # Imprime el valor de x
    x += 1       # Incrementa x en 1

#Programación Funcional
def suma(x, y):
    return x + y

def cuadrado(x):
    return x * x

resultado = cuadrado(suma(3, 4))  # Primero suma 3 y 4, luego calcula el cuadrado del resultado
print(resultado)  # Imprime 49

# POO
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "El animal hace un sonido."

class Perro(Animal): #Esta es la forma en la que hacemos herencias en Python. No te preocupes, aún no hemos visto estos conceptos de POO. Nosotros hemos hecho hasta ahora programación funcional.
    def hacer_sonido(self):
        return "El perro ladra."

mi_perro = Perro("Rex")
print(mi_perro.nombre)         # Imprime "Rex"
print(mi_perro.hacer_sonido())  # Imprime "El perro ladra."
```

## Diferencias (en particular con JavaScript, que es lo que vamos conociendo)

1. **Tipado:**

   - **Python:** Es un lenguaje de tipado dinámico, lo que significa que las variables no tienen un tipo fijo y el tipo se determina en tiempo de ejecución.
   - **JavaScript:** También es de tipado dinámico, pero sus tipos y coerciones pueden ser más impredecibles debido a la conversión implícita de tipos. Python tiende a lanzar errores si intentas realizar operaciones con tipos incompatibles sin una conversión explícita. Por ejemplo:

   ```javascript
   let a = "5";
   let b = 5;
   console.log(a == b); // true
   ```

   ```python
        a = 5
        b = "10"
        # resultado = a + b  # Esto generará un TypeError en Python
   ```

2. **Entorno de Ejecución:**

   - **Python:** Se ejecuta en el servidor o en el entorno local y es utilizado para una amplia gama de aplicaciones desde scripts simples hasta aplicaciones web complejas y análisis de datos.
   - **JavaScript:** Se ejecuta principalmente en el navegador web para crear aplicaciones web interactivas y dinámicas. También se puede ejecutar en el servidor con Node.js.

3. **Sintaxis:**

   - **Python:** Utiliza indentación para definir bloques de código, lo que promueve una sintaxis más limpia y estructurada. Muchísimo cuidado con esto, si no lo haces bien desde el principio tu código será absolutamente ilegible.
   - **JavaScript:** Utiliza llaves `{}` para definir bloques de código, lo que permite una mayor flexibilidad en el estilo de codificación.

4. **Paradigmas de Programación:**

   - **Python:** Soporta una variedad de paradigmas de programación, incluyendo programación orientada a objetos, funcional, y procedimental.
   - **JavaScript:** Aunque originalmente diseñado para la programación imperativa y orientada a objetos, también soporta la programación funcional, especialmente con las características modernas introducidas en ECMAScript 6 (ES6) y posteriores.

5. **Uso en la Web:**
   - **Python:** Usado para el desarrollo de back-end con frameworks como Django y Flask.
   - **JavaScript:** Esencial para el desarrollo front-end, manipulando el DOM y gestionando interacciones en el navegador.

## Particularidades de Python

1. **Legibilidad del Código:**

   - Python enfatiza la legibilidad del código con una sintaxis limpia y un diseño que promueve el código fácil de leer y mantener.

2. **Indentación:**

   - La indentación es crucial en Python ya que define el alcance de los bloques de código. Esto es diferente a muchos otros lenguajes que usan llaves `{}`.

3. **Bibliotecas Extensas:**

   - Python tiene una rica colección de bibliotecas y paquetes para diversas tareas, como `NumPy` para computación numérica, `Pandas` para análisis de datos, y `Requests` para manejar solicitudes HTTP.

4. **Interpretado:**

   - Python es un lenguaje interpretado, lo que significa que el código se ejecuta línea por línea, facilitando la depuración y la ejecución de scripts.

5. **GIL (Global Interpreter Lock):**
   - Python usa un mecanismo llamado Global Interpreter Lock que limita la ejecución simultánea de múltiples hilos en el mismo proceso, lo que puede afectar el rendimiento en aplicaciones multihilo intensivas.

## Dificultades principales de Python

1. **Velocidad de Ejecución:**

   - Python puede ser más lento en comparación con lenguajes compilados como C o C++ debido a su naturaleza interpretada y al GIL.

2. **Gestión de Memoria:**

   - La gestión automática de memoria puede llevar a un mayor uso de memoria, especialmente en aplicaciones con gran cantidad de datos o estructuras complejas.

3. **Dependencias de Versiones:**

   - Las diferencias entre versiones de Python (por ejemplo, Python 2 vs Python 3) pueden llevar a problemas de compatibilidad con bibliotecas y código legado.

4. **Rendimiento en Aplicaciones Multihilo:**
   - El GIL puede limitar el rendimiento en aplicaciones que hacen uso extensivo de múltiples hilos.

## Imprescindible para usar bien Python

1. **Conocimiento de la Sintaxis Básica:**

   - Familiaridad con la sintaxis básica, estructuras de datos y control de flujo.

2. **Uso de Bibliotecas y Módulos:**

   - Comprender cómo instalar, importar y utilizar bibliotecas y módulos externos para extender las funcionalidades de Python.

3. **Prácticas de Programación Limpia:**

   - Aplicar buenas prácticas de programación, como el uso adecuado de indentación, nombres de variables significativos, y escritura de funciones modulares.

4. **Conocimiento de Herramientas de Desarrollo:**

   - Familiaridad con herramientas como entornos virtuales (`venv`), gestores de paquetes (`pip`), y sistemas de control de versiones (como Git).

5. **Manejo de Excepciones:**

   - Saber cómo manejar errores y excepciones de manera efectiva para construir aplicaciones robustas y resilientes.

6. **Documentación y Comunidad:**
   - Utilizar la documentación oficial y los recursos de la comunidad para resolver problemas y mejorar habilidades. Python tiene una gran comunidad y una excelente documentación oficial que puede ser de gran ayuda.

## ¿Por qué se usa Python para Machine Learning, Big Data, IA...

Python se ha convertido en uno de los lenguajes de programación más populares y preferidos en el campo de Machine Learning, Big Data, Inteligencia Artificial (IA) y otras áreas relacionadas.

### 1. **Facilidad de Aprendizaje y Uso**

- **Sintaxis Simple y Legible:** Python tiene una sintaxis clara y concisa que facilita la escritura y lectura del código, lo que es especialmente beneficioso para los desarrolladores y científicos de datos.
- **Productividad:** La simplicidad del lenguaje permite a los programadores ser más productivos y enfocar más tiempo en resolver problemas en lugar de en la complejidad del lenguaje.

### 2. **Amplia Biblioteca y Ecosistema**

- **Bibliotecas Especializadas:** Python cuenta con una gran variedad de bibliotecas y frameworks diseñados para Machine Learning, Big Data e IA, como `TensorFlow`, `Keras`, `PyTorch`, `scikit-learn`, `Pandas`, `NumPy`, y `SciPy`.
- **Herramientas de Big Data:** Herramientas como `Dask` y `PySpark` facilitan el procesamiento y análisis de grandes volúmenes de datos.

### 3. **Comunidad Activa y Soporte**

- **Comunidad Grande:** Python tiene una comunidad de desarrolladores y científicos de datos muy activa que contribuye constantemente con nuevos paquetes, herramientas y soluciones a problemas comunes.
- **Recursos y Soporte:** Hay una abundancia de recursos, tutoriales y documentación disponible para aprender y resolver problemas en Python.

### 4. **Integración y Flexibilidad**

- **Integración con Otros Lenguajes y Tecnologías:** Python puede integrarse fácilmente con otros lenguajes y tecnologías, como C/C++, Java y SQL, permitiendo una mayor flexibilidad en el desarrollo de soluciones.
- **Interoperabilidad:** La capacidad de Python para interoperar con otros sistemas y plataformas lo convierte en una opción atractiva para aplicaciones que requieren interacción con diversas fuentes de datos y sistemas.

### 5. **Desarrollo Rápido de Prototipos**

- **Iteración Rápida:** Python facilita el desarrollo rápido de prototipos gracias a su sintaxis sencilla y a las bibliotecas poderosas. Esto permite a los investigadores y desarrolladores experimentar con diferentes algoritmos y modelos de manera eficiente.

### 6. **Soporte para Ciencia de Datos**

- **Análisis y Visualización de Datos:** Bibliotecas como `Matplotlib`, `Seaborn`, y `Plotly` permiten una visualización de datos efectiva, mientras que `Pandas` y `NumPy` son esenciales para el análisis y manipulación de datos.
- **Entornos Interactivos:** Herramientas como Jupyter Notebooks proporcionan un entorno interactivo para la exploración y experimentación con datos.

### 7. **Escalabilidad y Mantenimiento**

- **Escalabilidad:** Python permite construir sistemas escalables mediante el uso de bibliotecas como `Dask` para el procesamiento distribuido y `PySpark` para la integración con Apache Spark.
- **Mantenimiento:** La claridad y simplicidad de Python contribuyen a un código más mantenible, lo que facilita la evolución y el mantenimiento de proyectos complejos.

## Instalaciones

### Python

[Python](https://www.python.org/)

### Extensión Python

Instala lae extensión Python del VSCode

### Ejecuta como administrador

Imprescindible para algunas de nuestras instalaciones

### Actualizar versión

python -m pip install --upgrade pip

### Requests para el fetch

`pip install requests`

### Flask

`pip install Flask`
