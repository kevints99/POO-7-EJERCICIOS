class Empleado:
    contador_empleados = 0
    
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
        Empleado.contador_empleados += 1
    
    @classmethod
    def cantidad_empleados(cls):
        return cls.contador_empleados
    
    def obtener_info(self):
        return f"Nombre: {self.__nombre}, Salario: {self.__salario}"

# Ejemplo de uso
empleado1 = Empleado("Luzdey Carbal", 3000)
empleado2 = Empleado("Kevin Tapia", 3500)
print(empleado1.obtener_info())
print(empleado2.obtener_info())
print(f"Total de empleados: {Empleado.cantidad_empleados()}")
