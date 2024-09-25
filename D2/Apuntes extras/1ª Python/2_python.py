# Programación Orientada a Objetos (POO), así vamos comparando con las BBDD.

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.anio})"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def añadir_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)
        else:
            print("Error: Solo se pueden añadir objetos de tipo Libro.")

    def buscar_libro(self, titulo):
        resultados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        return resultados

    def listar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        for libro in self.libros:
            print(libro)

# Programación Funcional

def filtrar_libros_por_autor(libros, autor):
    """Devuelve una lista de libros cuyo autor coincide con el autor dado."""
    return [libro for libro in libros if autor.lower() in libro.autor.lower()]

def ordenar_libros_por_anio(libros):
    """Devuelve una lista de libros ordenada por año de publicación."""
    return sorted(libros, key=lambda libro: libro.anio)

# Programación Imperativa

def main():
    # Crear una instancia de la biblioteca
    mi_biblioteca = Biblioteca()

    # Añadir libros
    mi_biblioteca.añadir_libro(Libro("El Quijote", "Miguel de Cervantes", 1605))
    mi_biblioteca.añadir_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 1967))
    mi_biblioteca.añadir_libro(Libro("1984", "George Orwell", 1949))

    # Listar libros en la biblioteca
    print("Libros en la biblioteca:")
    mi_biblioteca.listar_libros()

    # Buscar un libro por título
    print("\nBuscando libros con '1984' en el título:")
    libros_encontrados = mi_biblioteca.buscar_libro("1984")
    for libro in libros_encontrados:
        print(libro)

    # Filtrar libros por autor
    print("\nFiltrando libros por autor 'Gabriel García Márquez':")
    libros_de_gabriel = filtrar_libros_por_autor(mi_biblioteca.libros, "Gabriel García Márquez")
    for libro in libros_de_gabriel:
        print(libro)

    # Ordenar libros por año
    print("\nLibros ordenados por año de publicación:")
    libros_ordenados = ordenar_libros_por_anio(mi_biblioteca.libros)
    for libro in libros_ordenados:
        print(libro)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
