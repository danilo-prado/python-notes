'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

a = float(input('Digite uma reta:'))
b = float(input('Digite a outra reta:'))
c = float(input('Digite mais uma reta:'))


if (a + b) > c and (b + c) > a and (c + a) > b:
    print('É um triângulo')
else:
    print('Não é um triângulo')