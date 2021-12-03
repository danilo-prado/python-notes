#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere: US$1.00=R$5.51
n = float(input('Digite quanto você tem na carteira: R$'))
conv = n / 5.51
print('Você pode comprar US${:.2f} dólares'.format(conv))