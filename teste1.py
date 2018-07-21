cont = 0
soma = 0
while cont < 12:
    mes = float(input("Investimento -  %i° mês R$: " % (cont + 1)))
    rent = mes * (1 + 0.005) #taxa base na cardenete de poupança
    soma = soma + rent 
    cont += 1
    print("R$%6.2f" % soma)
print("Valor final -  R$%6.2f" % soma)
