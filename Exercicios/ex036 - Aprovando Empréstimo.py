'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado '''

print('SIMULAÇÃO DE FINANCIAMENTO')
casa = float(input('Digite o valor da casa:'))
salario = float(input('Digite o seu salário:'))
tempo = float(input('Digite quantos anos:'))
pmt = casa / (tempo * 12)

print('O valor da prestação será de R${:.2f} mensais'.format(pmt))
if pmt <= salario * 0.3:
    print('FINANCIAMENTO APROVADO!')

else:
    print('FINANCIAMENTO NEGADO!')
