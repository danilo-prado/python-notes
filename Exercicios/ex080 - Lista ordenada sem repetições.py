'''CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA,
JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SORT()).
NO FINAL, MOSTRE A LISTA ORDENADA NA TELA'''

lista = []

for c in range(0,5):
    valor = int(input('Digite um número:'))
#LÓGICA PARA ORDENAÇÃO
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos +=1

print(f'Lista ordenada:{lista}')
