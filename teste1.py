cont = 0
soma = 0
while cont < 12:
    mes = float(input("Investimento -  %i° mês R$: " % (cont + 1)))
    rent = mes * (1 + 0.00857)
    soma = soma + rent 
    cont += 1
    print("R$%6.2f" % soma)
print("Valor final -  R$%6.2f" % soma)
