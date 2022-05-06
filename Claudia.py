"""@If(
    @Abs(@Abs(@Abs(SALDO_INICIAL)-@Abs(K_DEBITO_SUM)+@Abs(K_CREDITO_SUM)) -@Abs(SALDO_FINAL))
    <
    @Abs(@Abs(@Abs(SALDO_INICIAL)+@Abs(K_DEBITO_SUM)-@Abs(K_CREDITO_SUM))-@Abs(SALDO_FINAL));
@Abs(SALDO_INICIAL)-@Abs(K_DEBITO_SUM)+@Abs(K_CREDITO_SUM);


@Abs(SALDO_INICIAL)+@Abs(K_DEBITO_SUM)-@Abs(K_CREDITO_SUM))
"""


saldoInicial = float(input("Escriba el saldo inicial: "))
saldoFinal = float(input("Escriba el saldo Fianl: "))
credito = float(input("Escriba el saldo credito: "))
debito = float(input("Escriba el saldo debito: "))


primeraComparacion = abs(abs(abs(saldoInicial)-abs(saldoFinal)-abs(credito))-abs(saldoFinal))
segundaComparacion = abs(abs(abs(saldoInicial)+abs(saldoFinal)-abs(credito))-abs(saldoFinal))

if primeraComparacion < segundaComparacion:
    resultado = abs(saldoInicial)-abs(debito)+abs(credito)

    print("si se cumple:", resultado)
    resultado = abs(saldoFinal) - abs(resultado)
    print("Resultado: ", resultado)

    if resultado != 0.0 and credito > 0.0:

        comparacionSaldoFinal = abs(abs(credito)-abs(debito))+abs(saldoInicial)
        comparacionSaldoTotal = abs(comparacionSaldoFinal)-abs(saldoFinal)

        print("Comparacion:", comparacionSaldoTotal)

    if resultado != 0.0 and credito < 0.0:

        comparacionSaldoFinal = abs(abs(debito)-abs(credito))+abs(saldoInicial)
        comparacionSaldoTotal = abs(comparacionSaldoFinal)-abs(saldoFinal)

        print("Comparacion:", comparacionSaldoTotal)
else:
    resultado = abs(saldoInicial)+abs(debito)-abs(credito)

    print("si no se cumple", resultado)
    resultado = abs(saldoFinal) - abs(resultado)

    print("Resultado: ", resultado)

    if resultado != 0.0 and credito > 0.0:

        comparacionSaldoFinal = abs(abs(credito)-abs(debito))+abs(saldoInicial)
        comparacionSaldoTotal = abs(comparacionSaldoFinal)-abs(saldoFinal)
        print("Comparacion:", comparacionSaldoTotal)

    if resultado != 0.0 and credito < 0.0:

        comparacionSaldoFinal = abs(abs(debito)-abs(credito))+abs(saldoInicial)
        comparacionSaldoTotal = abs(comparacionSaldoFinal)-abs(saldoFinal)
        print("Comparacion:", comparacionSaldoTotal)