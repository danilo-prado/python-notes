'''CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDE ESSES RESULTADOS EM UM
DICIONÁRIO. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO.'''

from time import sleep
from random import randint
from operator import itemgetter

lista = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = {}

for k, v in lista.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(lista.items(), key=itemgetter(1), reverse=True)
print('='*30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)



