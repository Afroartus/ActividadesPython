"""def miFuncion():
    print("Nombre")

miFuncion()"""

"""
def matematicas(a, b):

    def suma(a, b):
        print(a + b)

    def resta(a, b):
        print(a - b)

    suma(a, b)
    resta(a, b)

matematicas(1, 3)

"""
"""
def mifuncion(nombre):
    hoyHace = 6.0
    print("Hola,", nombre, "la temperatura es de", hoyHace)

mifuncion("Andrés")
"""
"""
#Para definir una variables por defecto en una variable
def suma(a=1, b=5, c=3):
    print(a + b +c)

suma(1, 1, 1)
"""

"""
def suma(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    print(resultado)

suma(9,9)
"""


"""
def suma(**kwargs):
    for key, value in kwargs.items(): #para correr (iterar) un dicionario
        print(key, "=", value)

suma(a="piso", b="rojo")
"""
"""
def suma(**kwargs):
    if kwargs['coche'] == 'bonito':
        print("tu coche es bonito")

suma(coche="bonito")
"""

"""
def operaciones(a,b):
    return a+b,a-b,a*b, a/b, a**b

suma, resta, multi, divi, _ = operaciones(2,4) # _ se utiliza para ignorar el resultado segun su pocicion en este caso a**b
print(suma)
print(resta)
print(multi)
print(divi)
"""

"""
def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else inicial

    resultado = 0
    for x in range(inicial, final + 1):
        resultado += x

    return resultado
    
print(sumador(final=5))

"""
"""
funcionAnonima = lambda nombre, nombre2: print("hola", nombre, "adios", nombre2)
funcionAnonima("pepe", "juan")
"""