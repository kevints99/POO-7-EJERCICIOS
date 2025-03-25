class CuentaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
        else:
            raise ValueError("El deposito debe ser mayor que cero.")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            raise ValueError("Fondos insuficientes o cantidad invalida.")
    
    def obtener_saldo(self):
        return self._saldo

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes_anual):
        super().__init__(titular, saldo)
        self.__interes_anual = interes_anual
    
    def aplicar_interes(self):
        self._saldo += self._saldo * (self.__interes_anual / 100)
    
    def obtener_interes(self):
        return self.__interes_anual

# Ejemplo de uso
cuenta = CuentaAhorro("Kevin Tapia", 1000, 5)
print(f"Saldo inicial: {cuenta.obtener_saldo()}")
cuenta.aplicar_interes()
print(f"Saldo despues de aplicar interes: {cuenta.obtener_saldo()}")
