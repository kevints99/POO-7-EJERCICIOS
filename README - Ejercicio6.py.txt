Descripción
Este programa define una clase `Empleado` que mantiene un registro del número total de empleados creados. Cada empleado tiene un nombre y un salario, y la clase ofrece un método de clase para consultar el número total de empleados.

Estructura del Código
El código contiene lo siguiente:
  - Clase `Empleado`:
  - `contador_empleados`: Atributo de clase que mantiene la cuenta de empleados creados.
  - `__init__(self, nombre, salario)`: Constructor que inicializa los atributos del empleado e incrementa el contador de empleados.
  - `cantidad_empleados(cls)`: Método de clase que devuelve el número total de empleados creados.
  - `obtener_info(self)`: Método que devuelve la información del empleado.

Ejemplo de uso:
  - Se crean dos empleados con nombres y salarios distintos.
  - Se muestra la información de cada empleado.
  - Se muestra el número total de empleados creados.