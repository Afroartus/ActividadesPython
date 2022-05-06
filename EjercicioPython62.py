"""
En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos
su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
con el resultado de la nota y si ha aprobado o no.
"""

class Alumno:
    nombre = ""
    nota = 0.0

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota

    def ResultadoNota(self):
        if self.nota >= 3.0 and self.nota <= 5.0:
            resultado = "El estudiante {0} aprobo con una nota {1}".format(self.nombre, self.nota)
        elif self.nota >= 0.0 and self.nota <= 2.9:
            resultado = "El estudiante {0} reprobo con una nota {1}".format(self.nombre, self.nota)
        else:
            resultado = "Escriba una nota validad para el sistema"
        return resultado



objAlumno = Alumno()

objAlumno.setNombre("Andres")
objAlumno.setNota(2.6)

print(objAlumno.ResultadoNota())
