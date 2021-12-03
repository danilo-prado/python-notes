'''Crie um programa que faça o computador jogar Jokenpô com você'''
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('OPÇÃO INVÁLIDA')

