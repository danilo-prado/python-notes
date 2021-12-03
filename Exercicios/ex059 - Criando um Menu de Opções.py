'''Crie um programa que leia dois valores e mostre um menu na tela:
 [1] somar
 [2] multiplicar
 [3] maior
 [4] novos números
 [5] sair do programa
 Seu programa deverá realizar a operação solicitada em cada caso'''

from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segunto número: '))
op = 0
while op != 5:
    op = int(input('Digite sua opção:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))
    if op == 1:
        print('Soma: {}'.format(n1 + n2))
    elif op == 2:
        print(n1 * n2)
    elif op == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif op == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segunto número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('OPÇÃO INVÁLIDA!')
sleep(2)


print('FIM')








'''PARTE INCORRETA

if op == 1:
    op = print(n1 + n2)
if op == 2:
    op = print(n1 * n2)
elif op == 3:
    if n1 > n2:
        print(n1)
    else:
        print(n2)
elif op == 4:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segunto número: '))
    op = int(input('Digite sua opção:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))
elif op == 5:
    print('Encerrado...')'''
