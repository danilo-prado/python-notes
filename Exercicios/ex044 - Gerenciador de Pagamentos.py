'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
À vista dinheiro/cheque: 10% de desconto
À vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou mais no cartão: 20%de juros'''

valor = float(input('Digite o valor do produto:'))
forma = int(input('Qual a forma de pagamento?\n[1] À vista dinheiro/cheque\n[2] À vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\nDigite a forma de pagamento:'))

if forma == 1:
    print('10% de desconto. O valor passa a ser R${:.2f}'.format(valor * 0.90))
elif forma == 2:
    print('5% de desconto. O valor passa a ser R${:.2f}'.format(valor * 0.95))
elif forma == 3:
    print('Preço normal, R${:.2f} sem desconto'.format(valor))
else:
    print('Juros de 20%. O valor passa a ser R${:.2f}'.format(valor * 1.2))

