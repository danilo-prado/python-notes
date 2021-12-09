'''FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO
GERADOS E VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA'''

from random import randint
from time import sleep

print('='*30)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('='*30)

lista = []
jogos = []
tot = 1
qnt = int(input('Digite quantos jogos você quer? '))
while tot <= qnt:
    cont = 0
    while True:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
             break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('{:^30}'.format('SORTEANDO'))
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
    sleep(1)
print('BOA SORTE!')
