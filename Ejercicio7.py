class TarjetaCredito:
    @staticmethod
    def validar_tarjeta(numero):
        numero = str(numero).replace(" ", "")
        if not numero.isdigit():
            return False
        
        suma = 0
        invertir_numeros = numero[::-1]
        for i, digito in enumerate(invertir_numeros):
            n = int(digito)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            suma += n
        
        return suma % 10 == 0

# Ejemplo de uso
numero_tarjeta = "4539578763621486"
if TarjetaCredito.validar_tarjeta(numero_tarjeta):
    print("El numero de tarjeta es valido.")
else:
    print("El numero de tarjeta no es valido.")
