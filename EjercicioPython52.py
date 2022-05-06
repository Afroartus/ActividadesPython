def numeroPrimos():
    numero = int(input("Cantidad de numeros a valdidar: "))
    contador = 0
    numeroDivisibles=[]
    for n in range(numero + 1):
        for j in range(n+1):
            if j != 0:
                if (n%j) == 0:
                    numeroDivisibles.append(j)
                    contador += 1
        if contador < 3 and n != 1 and n != 0:
            print("el numero {0} es primo".format(n))
        elif contador > 2 and n != 1:
            print("el numero {0} es compuesto".format(n))
            print("Su divisores son: ", *numeroDivisibles, sep=" ")
        contador = 0
        del numeroDivisibles[:]



numeroPrimos()