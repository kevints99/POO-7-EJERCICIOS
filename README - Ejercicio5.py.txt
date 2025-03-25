Descripción
Este programa define una clase `CuentaBancaria` y una subclase `CuentaAhorro` que extiende su funcionalidad añadiendo un atributo de interés anual. La clase `CuentaAhorro` permite aplicar el interés al saldo actual y consultar el porcentaje de interés.

Estructura del Código
El código contiene lo siguiente:
  - Clase `CuentaBancaria`:
  - `__init__(self, titular, saldo)`: Constructor que inicializa el titular y el saldo de la cuenta.
  - `depositar(self, cantidad)`: Método para depositar dinero en la cuenta.
  - `retirar(self, cantidad)`: Método para retirar dinero de la cuenta.
  - `obtener_saldo(self)`: Método que devuelve el saldo actual.

  - Clase `CuentaAhorro` (hereda de `CuentaBancaria`):
  - `__init__(self, titular, saldo, interes_anual)`: Agrega el atributo de interés anual.
  - `aplicar_interes(self)`: Método que aplica el interés anual al saldo de la cuenta.
  - `obtener_interes(self)`: Método que devuelve el porcentaje de interés.

Ejemplo de uso:
  - Se crea una cuenta de ahorro con un saldo de 1000 y un interés del 5%.
  - Se muestra el saldo inicial.
  - Se aplica el interés.
  - Se muestra el saldo actualizado.