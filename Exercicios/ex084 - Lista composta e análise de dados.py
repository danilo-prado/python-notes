'''FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
A) QUANTAS PESSOAS FORAM CADASTRADAS.
B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS
C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES'''

lista = []
dados = []
menor = maior = 0

print('=====','CADASTRO DE PESSOAS','=====')

while True:
    dados.append(str(input('Nome: ')))
    peso = dados.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    a = str(input('Deseja continuar? [S/N]'))
    if a in 'Nn':
        break
print('='*30)

#LETRA A
print(f'A) Foram cadastradas {len(lista)} pessoas.')

#LETRA B
print(f'B) O maior peso foi de {maior} Kg. Peso de ', end='')
for c in lista:
    if c[1] == maior:
        print(f'{c[0].upper().strip()}' , end='')

#LETRA C
print(f'\nC) O menor peso foi de {menor} Kg. Peso de ', end='')
for c in lista:
    if c[1] == menor:
        print(f'{c[0].upper().strip()}' , end='')
