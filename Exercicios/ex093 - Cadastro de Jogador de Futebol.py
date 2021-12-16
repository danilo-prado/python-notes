'''CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS
PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM
DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO.'''

dicio = {}
lista = []


dicio['nome'] = input('NOME DO JOGADOR: ')
app = int(input('NÚMERO DE PARTIDAS: '))
for c in range(0, app):
    lista.append(int(input(f'   QUANTOS GOLS NA PARTIDA {c + 1}:')))
dicio['gols'] = lista[:]
dicio['total'] = sum(lista)
print(dicio)
print('='* 30)
for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}')
print('='* 30)

print(f'O jogador {dicio["nome"]} jogou {app} partidas.')
for a, b in enumerate(lista):
    print(f'    => Na partida {a + 1}, fez {b} gols')
print(f'Total de {sum(lista)} gols')




