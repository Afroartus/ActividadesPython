def anioBisiesto():
    anio = int(input("Escriba el año el cual quiere saber si es bisiesto: "))
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                print("El año: {0} es un año bisisesto".format(anio))
            else:
                print("El año: {0} no es un año bisisesto".format(anio))
        else:
            print("El año: {0} es un año bisisesto".format(anio))
    else:
        print("El año: {0} no es un año bisisesto".format(anio))


anioBisiesto()