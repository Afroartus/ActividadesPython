"""
def EncontrarHipotenusa():
    catetoOpuesto = float(input("Cateto opuesto: "))
    catetoAdyacente = float(input("Cateto adyacente: "))
    resultado = round(math.sqrt((catetoOpuesto**2) + (catetoAdyacente**2)), 2)
    return resultado


print("El resultado de la hipotenusa:", EncontrarHipotenusa())

"""

"""
def EncontrarCateto():
    cateto = float(input("Cateto: "))
    hipotenusa = float(input("Hipotenusa: "))
    resultado = round(math.sqrt((hipotenusa**2) - (cateto**2)), 2)

    return resultado

print("El resultado del cateto:", EncontrarCateto())
"""

def AreaTriangulo():
    altura = float(input("Escriba la altura del triangulo: "))
    base = float(input("Escriba le base del triangulo: "))
    area = (altura * base) /2
    return area

print("El area de un triangulo:", AreaTriangulo())


def AreaCirculo():
    radio = float(input("Escriba el radio del circulo: "))
    area = (radio**2) * 3.14
    return area

print(AreaCirculo())




