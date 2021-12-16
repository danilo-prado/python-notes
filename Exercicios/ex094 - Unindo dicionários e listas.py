'''CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO E
TODOS OS DICIONÁRIOS EM UMA LISTA. NO FINAL, MOSTRE:
A) QUANTAS PESSOAS FORAM CADASTRADAS
B) A MÉDIA DE IDADE DO GRUPO
C) UMA LISTA COM TODAS AS MULHERES
D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA'''

dict = {}
all = []
soma = media = 0
while True:
    dict.clear()
    dict['nome'] = str(input('NOME: '))
    while True:
        dict['sexo'] = str(input('SEXO: [M/F]')).upper()[0]
        if dict['sexo'] not in 'MF':
            print('ERRO! DIGITE [M/F]')
        else:
            break
    dict['idade'] = int(input('IDADE: '))
    soma += dict['idade']
    all.append(dict.copy())
    while True:
        q = str(input('QUER CONTINUAR? [S/N]')).upper()[0]
        if q in 'SN':
            break
        print('ERRO!')
    if q == 'N':
        break
print('=' * 30)
print(all)
print(f'A) Ao todo temos {len(all)} pessoas cadastradas')
media = soma / len(all)
print(f'B) A média das idades é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in all:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas acima da média: ')
for p in all:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
