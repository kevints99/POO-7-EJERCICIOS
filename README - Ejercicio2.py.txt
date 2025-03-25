Descripción
Este programa define una clase `Rectangulo` que representa un rectángulo con atributos privados para el largo y el ancho. La clase incluye métodos para cambiar las dimensiones, calcular el área y el perímetro, y obtener las dimensiones actuales del rectángulo.

Estructura del Código
El código contiene lo siguiente:
Clase `Rectangulo`:
  - `__init__(self, largo, ancho)`: Constructor que inicializa los atributos del rectángulo, validando que sean mayores que cero.
  - `cambiar_dimensiones(self, nuevo_largo, nuevo_ancho)`: Método que permite modificar el largo y el ancho, asegurando que sean mayores que cero.
  - `calcular_area(self)`: Método que calcula el área del rectángulo.
  - `calcular_perimetro(self)`: Método que calcula el perímetro del rectángulo.
  - `obtener_dimensiones(self)`: Método que devuelve las dimensiones actuales del rectángulo.

Ejemplo de uso:
  - Se crea un rectángulo con largo 10 y ancho 5.
  - Se muestran sus dimensiones.
  - Se calcula y muestra el área y el perímetro.
  - Se cambian las dimensiones a 8 y 4.
  - Se muestran las nuevas dimensiones.
