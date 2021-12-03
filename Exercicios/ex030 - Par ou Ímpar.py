''' Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPÁR.'''

n = int(input('Digite um número:'))
resto = n % 2

if resto == 0:
    print('Salve amigão, beleza? Esse número é pár!')
else:
    print('É amigão, esse número aí é ímpar.')