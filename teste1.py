cont = 0
soma = 0
while cont < 12:
    mes = float(input("Investimento -  %i° mês R$: " % (cont + 1)))
    rent = mes * (1 + 0.005) #taxa base na cardenete de poupança
    soma = soma + rent 
    cont += 1
    print("R$%6.2f" % soma)
print("Valor final -  R$%6.2f" % soma)

#Planejando a compra de um carro

carro = int(input("Valor do carro - R$ "))
entrada = soma
financiamento = carro - entrada
print("Valor a financiar R$%7.2f " %financiamento)

#Parcelando o valor restante com juros

parcela = (financiamento * 1.89) / 12
print("Quantidade de mês - 12")
print("Valor das parcelas - R$%7.2f" % parcela)
