'''APRIMORE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES
 DO APROVEITAMENTO DE CADA JOGADOR'''

time = []
dicio = {}
lista = []

while True:
    dicio.clear()
    dicio['nome'] = input('NOME DO JOGADOR: ')
    app = int(input('NÚMERO DE PARTIDAS: '))
    lista.clear()
    for c in range(0, app):
        lista.append(int(input(f'   QUANTOS GOLS NA PARTIDA {c + 1}:')))
    dicio['gols'] = lista[:]
    dicio['total'] = sum(lista)
    time.append(dicio.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

# MOSTRANDO OS RESULTADOS
print('='* 40)
print('cod ', end='')
for i in dicio.keys():
    print(f'{i:<15}', end='')
print()
print('='* 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='* 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('='* 40)
print('VOLTE SEMPRE!')
