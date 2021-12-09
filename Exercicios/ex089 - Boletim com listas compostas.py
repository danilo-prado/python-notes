'''CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA. NO FINAL,
MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE'''

from time import sleep

lista = []
print('=' * 30)
print('{:^30}'.format('CADASTRO DE ALUNOS'))
print('=' * 30)

while True:
    nome = str(input('NOME: '))
    p1 = float(input('P1: '))
    p2 = float(input('P2: '))
    media = (p1 + p2) / 2
    lista.append([nome, [p1, p2], media])
    q = str(input('DESEJA CONTINUAR? [S/N]'))
    print('=' * 30)
    if q in 'Nn':
        break

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0].upper():<10}{a[2]:>8.1f}')

while True:
    print('=' * 30)
    q2 = int(input('DIGITE O NÚMERO DO ALUNO OU 999 PARA SAIR: '))
    if q2 == 999:
        print('FINALIZANDO...')
        sleep(1)
        print('VOLTE SEMPRE!')
        break
    if q2 <= len(lista) - 1:
        print(f'As notas de {lista[q2][0].upper()} são {lista[q2][1]}')
