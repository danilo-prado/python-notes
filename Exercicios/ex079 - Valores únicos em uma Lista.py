'''CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NÚMERICOS E CADASTRE-OS EM UMA LISTA.
CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO.
NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE'''

lista = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)

    a = input('Valor cadastrado! Deseja continuar? [S/N]').strip()
    if a in 'Nn':
        break

#LISTA.SORT() deve ser colocado antes
lista.sort()
print(f'Lista em ordem crescente:{lista}')
