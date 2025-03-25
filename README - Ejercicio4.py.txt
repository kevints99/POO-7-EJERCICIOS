Descripción
Este programa define una clase `Libro` que representa un libro con atributos privados para el título, el autor, el número total de páginas y la página actual en la que se encuentra el lector. La clase incluye métodos para avanzar y retroceder páginas, obtener la página actual y obtener la información completa del libro.

Estructura del Código
El código contiene lo siguiente:
  - Clase `Libro`**:
  - `__init__(self, titulo, autor, num_paginas)`: Constructor que inicializa los atributos del libro.
  - `avanzar_paginas(self, cantidad)`: Método que avanza un número de páginas, asegurando que no supere el total de páginas.
  - `retroceder_paginas(self, cantidad)`: Método que retrocede un número de páginas, asegurando que no baje de la página 1.
  - `obtener_pagina_actual(self)`: Método que devuelve la página actual en la que se encuentra el lector.
  - `obtener_info(self)`: Método que devuelve la información completa del libro.

Ejemplo de uso:
  - Se crea un libro "1984" de George Orwell con 328 páginas.
  - Se muestra la información del libro.
  - Se avanza 50 páginas.
  - Se retrocede 10 páginas.
  - Se muestra la página actual en cada paso.
