# Lab Python - Crea tu propio terrario

Aprovechando que Python es un tipo de serpiente (de ahí su logo), vamos a crear un terrario. Para ello debemos seguir los siguientes pasos:

## Paso 1: Definir la Clase `Terrario`

1. Crea una clase llamada `Terrario` que tenga los siguientes atributos:
    - `nombre` (nombre del terrario)
    - `ancho` (ancho del terrario en metros)
    - `largo` (largo del terrario en metros)
    - `habitantes` (una lista de habitantes en el terrario, inicialmente vacía)

2. Define un método llamado `agregar_habitante` que reciba un objeto `Serpiente` y lo agregue a la lista de `habitantes`.

3. Define un método llamado `area` que calcule el área del terrario.

## Paso 2: Definir la Clase `Serpiente`

1. Crea una clase llamada `Serpiente` que tenga los siguientes atributos:
    - `nombre` (nombre de la serpiente)
    - `longitud` (longitud de la serpiente en metros)
    - `especie` (especie de la serpiente)

2. Define un método llamado `deslizarse` que imprima un mensaje indicando que la serpiente se está deslizando.

## Paso 3: Crear Instancias y Probar

1. Crea una instancia de la clase `Terrario`.

2. Crea al menos dos instancias de la clase `Serpiente`.

3. Agrega las serpientes al terrario usando el método `agregar_habitante`.

4. Calcula el área del terrario y muestra el resultado.

5. Haz que cada serpiente se deslice usando el método `deslizarse`.

6. Muestra todas las serpientes del terrario (Tendrás que crear una función nueva que no te he pedido previamente)

## Paso 4: Ejecuta todo el código para un navegador. 

Crea un HTML y un CSS, vincúlalos y haz que cuando el usuario pulse el botón "guardar" se guarde el terrario y todos los animales en un archivo. 