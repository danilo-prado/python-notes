'''APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:
A) A SOMA DE TODOS OS VALORES PARES DIGITADOS
B) A SOMA DOS VALORES DA TERCEIRA COLUNA
C) O MAIOR VALOR DA SEGUNDA LINHA'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = cont2 = maior = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número da posição [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[   {matriz[l][c]}   ]', end=' ')
    print()

#LETRA A
for l in range(0,3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            cont += matriz[l][c]
print(f'A) A soma dos números pares é: {cont}')

#LETRA B
for l in range(0,3):
    for c in range(2,3):
        cont2 += matriz[l][c]
print(f'B) A soma da terceira coluna é: {cont2}')

#LETRA C
for l in range(1,2):
    for c in range(0,3):
        if matriz[l][c] > maior:
                maior = matriz[l][c]
print(f'C) O maior valor da segunda linha é: {maior}')
