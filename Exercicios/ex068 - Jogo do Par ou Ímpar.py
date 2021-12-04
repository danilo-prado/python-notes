'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''

from random import randint

win = 0
lose = 0

while True:
    #choice = input('PAR OU ÍMPAR? [P/I]:')
    player = int(input('Digite o número: '))
    cpu = randint(0, 10)
    soma = player + cpu
    choice = input('PAR OU ÍMPAR? [P/I] ').upper().strip()[0]

    if choice != 'P' and choice != 'I':
        print('Opção inválida... Tente novamente!')


    elif choice == 'P' and soma % 2 == 0:
        print(f'CPU: {cpu}')
        print('VOCÊ GANHOU :)')
        win += 1


    elif choice == 'I' and soma % 2 != 0:
        print(f'CPU: {cpu}')
        print('VOCÊ GANHOU :)')
        win += 1
    else:
        print(f'CPU: {cpu}')
        print('VOCÊ PERDEU :(')
        lose += 1
        print(f'Você jogou {win + lose} vezes e ganhou {win} vezes')
        break
