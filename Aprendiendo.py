"""
contador = 1
while contador <= 10:
    if contador % 2 == 0:
        print(contador, "Es numero par")
        continue
    else:
        print(contador, "es numero impar")

    contador += 1
"""
"""
lista = {1,2,3,'a',5,6}

for valorActual in lista:
    print(valorActual)
lista = ["Hola", "mensaje", "adios"]
"""

"""for palabra in lista:
    print("palabra actual: ", palabra)
    if palabra == "mensaje":
        print("He encontrado la palabra mensaje")
        break
"""
"""
para ordernar listas

lista = [5,9,8,2,6,4,1,3,7]
listaOrdenada = sorted(lista, reverse=False)
print(listaOrdenada)

"""

"""valor = 9

match valor:
    case 1:
        print("valor:", valor)
    case 2:
        print("valor:", valor)
    case 3:
        print("valor:", valor)
    case 4:
        print("valor:", valor)
    case 5:
        print("valor:", valor)
"""

lista = ["Hola", "Mensaje", "adios"]

for palabra in lista:
    if palabra == "Mensaje":
        print("Encontre Mensaje")
        break
else:
    print("no encuentro nada")