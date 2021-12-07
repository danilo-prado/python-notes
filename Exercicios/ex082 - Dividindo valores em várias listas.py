'''CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.
DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS OS VALORES PARES E OS VALORES ÍMPARES DIGITADOS,
RESPECTIVAMENTE.
AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS.'''

lista1 = []

while True:
    valor = int(input('Digite um número:'))
    lista1.append(valor)
    a = input('Valor cadastrado! Deseja continuar? [S/N]')
    if a in 'Nn':
        break

lista2 = []
lista3 = []
#ESTRUTURA ENUMERATE PARA MOSTRAR CADA VALOR NOS ÍNDICES
for i, valor in enumerate(lista1):
    if valor % 2 == 0:
        lista2.append(valor)
    elif valor % 2 == 1:
        lista3.append(valor)

print('='*30)
print(f'Lista:{lista1}')
print(f'Pares:{lista2}')
print(f'Ímpares:{lista3}')
