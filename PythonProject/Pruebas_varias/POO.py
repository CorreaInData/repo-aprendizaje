# Definimos la clase Libro
class Libro:
    def __init__(self, titulo, autor, cantidad):
        self.titulo = titulo  # Título del libro
        self.autor = autor    # Autor del libro
        self.cantidad = cantidad  # Cantidad disponible en la biblioteca

    def __str__(self):
        return f"Libro: {self.titulo} por {self.autor} ({self.cantidad} disponibles)"

    def prestar(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            print(f"Libro '{self.titulo}' prestado. Quedan {self.cantidad} disponibles.")
        else:
            print(f"No hay copias disponibles de '{self.titulo}'.")

    def devolver(self):
        self.cantidad += 1
        print(f"Libro '{self.titulo}' devuelto. Ahora hay {self.cantidad} disponibles.")

# Definimos la clase Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (Libros prestados: {len(self.libros_prestados)})"

    def prestar_libro(self, libro):
        if libro.cantidad > 0:
            libro.prestar()
            self.libros_prestados.append(libro.titulo)
            print(f"{self.nombre} ha prestado '{libro.titulo}'.")
        else:
            print(f"No se puede prestar '{libro.titulo}' a {self.nombre}.")

    def devolver_libro(self, libro):
        if libro.titulo in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro.titulo)
            print(f"{self.nombre} ha devuelto '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene prestado '{libro.titulo}'.")

# Creamos algunos libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 3)
libro2 = Libro("1984", "George Orwell", 2)

# Creamos algunos usuarios
usuario1 = Usuario("Juan")
usuario2 = Usuario("María")

# Mostramos la información inicial
print(libro1)
print(libro2)
print(usuario1)
print(usuario2)

# Juan presta un libro
usuario1.prestar_libro(libro1)

# María presta un libro
usuario2.prestar_libro(libro2)

# Mostramos la información después de los préstamos
print(libro1)
print(libro2)
print(usuario1)
print(usuario2)

# Juan devuelve un libro
usuario1.devolver_libro(libro1)

# Mostramos la información después de la devolución
print(libro1)
print(libro2)
print(usuario1)
print(usuario2)