class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__num_paginas = num_paginas
        self.__pagina_actual = 1
    
    def avanzar_paginas(self, cantidad):
        if self.__pagina_actual + cantidad <= self.__num_paginas:
            self.__pagina_actual += cantidad
        else:
            raise ValueError("No se puede avanzar mas alla del numero total de paginas.")
    
    def retroceder_paginas(self, cantidad):
        if self.__pagina_actual - cantidad >= 1:
            self.__pagina_actual -= cantidad
        else:
            raise ValueError("No se puede retroceder mas alla de la pagina 1.")
    
    def obtener_pagina_actual(self):
        return self.__pagina_actual
    
    def obtener_info(self):
        return f"Titulo: {self.__titulo}, Autor: {self.__autor}, Paginas: {self.__num_paginas}, Pagina Actual: {self.__pagina_actual}"

# Ejemplo de uso
libro = Libro("1984", "George Orwell", 328)
print(libro.obtener_info())
libro.avanzar_paginas(50)
print(f"Pagina actual: {libro.obtener_pagina_actual()}")
libro.retroceder_paginas(10)
print(f"Pagina actual despues de retroceder: {libro.obtener_pagina_actual()}")
