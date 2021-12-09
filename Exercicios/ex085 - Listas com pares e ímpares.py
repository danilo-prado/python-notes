'''CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR SETE VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA ÚNICA QUE MANTENHA
SEPARADOS OS VALORES PARES E ÍMPARES. NO FINAL, MOSTRE OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTE'''

lista = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()
print(lista)
