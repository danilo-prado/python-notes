'''FAÇA UM PROGRAMA QUE LEIA 5 VALORES NÚMERICOS E GUARDE-OS EM UMA LISTA.
NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.'''

#PRIMEIRA FORMA
#lista = [int(input('Digite um valor na posição 0:')),
#         int(input('Digite um valor na posição 1:')),
#         int(input('Digite um valor na posição 2:')),
#         int(input('Digite um valor na posição 3:')),
#         int(input('Digite um valor na posição 4:'))]'''

#SEGUNDA FORMA
lista = []
maior = menor = 0

for c in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {c}:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('='*30)
print(f'Lista:{lista}')
print(f'O maior número digitado foi {maior} na posição: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor número digitado foi {menor} na posição: ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
