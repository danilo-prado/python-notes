'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minusculas
Quantas letras ao todo sem considerar espaços
Quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome:').strip())
print('Letra maiúsculas:{}'.format(nome.upper()))
print('Letra minúscula:{}'.format(nome.lower()))
print('Total de letras:{}'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem:{}'.format(nome.find(' ')))