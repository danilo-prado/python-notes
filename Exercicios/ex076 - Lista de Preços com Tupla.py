''' CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS NA SEQUÊNCIA.
NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR'''

tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90)

print('='*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('='*40)

for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R${tupla[pos]:>7.2f}')

print('='*40)