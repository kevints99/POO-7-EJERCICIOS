class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []
    
    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0 y 100.")
    
    def calcular_promedio(self):
        return sum(self.__notas) / len(self.__notas) if self.__notas else 0
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_edad(self):
        return self.__edad

# Ejemplo de uso
estudiante = Estudiante("Kevin Tapia", 20)
estudiante.agregar_nota(85)
estudiante.agregar_nota(90)
estudiante.agregar_nota(78)
print(f"Nombre: {estudiante.obtener_nombre()}, Edad: {estudiante.obtener_edad()}")
print(f"Promedio de notas: {estudiante.calcular_promedio()}")
