Descripción
Este programa define una clase `Producto` que representa un producto con atributos privados para su nombre y precio. La clase incluye métodos para modificar el precio, obtener el nombre y el precio, y aplicar descuentos al precio del producto.

Estructura del Código
El código contiene lo siguiente:
Clase `Producto`:
  - `__init__(self, nombre, precio)`: Constructor que inicializa los atributos del producto. Verifica que el precio sea mayor que cero.
  - `cambiar_precio(self, nuevo_precio)`: Método que cambia el precio del producto, validando que sea mayor que cero.
  - `obtener_precio(self)`: Método que devuelve el precio actual del producto.
  - `obtener_nombre(self)`: Método que devuelve el nombre del producto.
  - `aplicar_descuento(self, porcentaje)`: Método que aplica un descuento al precio del producto, asegurando que el porcentaje esté entre 0 y 100.

Ejemplo de uso:
  - Se crea un producto "Celular" con un precio de 500.
  - Se muestra el nombre y el precio del producto.
  - Se cambia el precio a 450.
  - Se aplica un descuento del 10%.
  - Se muestran los valores actualizados.


