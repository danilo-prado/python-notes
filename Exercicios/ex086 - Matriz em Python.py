'''CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3 E PREENCHA COM VALORES LIDOS PELO TECLADO,
NO FINAL, MOSTRE A MATRIZ NA TELA COM A FORMATAÇÃO CORRETA'''

lista1 = [[],[],[]]
lista2 = [[],[],[]]
lista3 = [[],[],[]]

for c in range(0,3):
    valor = int(input('Digite um número: '))
    lista1[c].append(valor)

for c in range(0,3):
    valor = int(input('Digite um número: '))
    lista2[c].append(valor)

for c in range(0,3):
    valor = int(input('Digite um número: '))
    lista3[c].append(valor)

print(lista1)
print(lista2)
print(lista3)
