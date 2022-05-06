class Vehiculo:
    color = "Blanco"
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = 26.3
    cilindraje = 150


objCohe = Coche()

print(objCohe.color)
print(objCohe.ruedas)
print(objCohe.puertas)

print(objCohe.velocidad)
print(objCohe.cilindraje)