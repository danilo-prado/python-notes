'''Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu'''
import random
n = int(input('Digite um número entre 0 e 5:'))
comp = random.randint(0,5)
print('O número sorteado foi: {}'.format(comp))
if comp==n:
    print('Parabéns você acertou!')
else:
    print('Você errou!')