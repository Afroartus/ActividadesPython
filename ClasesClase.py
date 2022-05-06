"""si se coloca un guion bajo "-" en una propiedad o una funcion no se deberia modifcar """

class Juguete:
    _encendido = False

    def enciende(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False  #self para hacer una referencia dentro de una clase

    def isEncendido(self):
        return self._encendido


class Estatica: #clase estatica
    numero = 1

    def incrementa(self):
        Estatica.numero+=1 #las clases estaticas deben llamarse con el mismo nombre de la clase en cambio una clase dinamica se hace con un self

"""Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)"""


#para herededar de una clase

class Potato(Juguete):
    brazos = 2
    nombre = None

    def __init__(self, nombre, brazos):
        #Constructor
        self.brazos = brazos
        self.nombre = nombre


    def quitarBrazo(self):
        self.brazos -= 1
        return self.brazos

    def AgregarBrazo(self):
        self.brazos += 1
        return self.brazos


p = Potato("Andres", 2)
print(p.nombre)
