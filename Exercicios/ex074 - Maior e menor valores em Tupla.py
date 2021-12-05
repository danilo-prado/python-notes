'''CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA.
DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA'''

from random import randint


tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(tupla)

print(f'O maior valor foi {max(tupla)} e o menor valor foi {min(tupla)}')
