'''CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.
DEPOIS DISSO, MOSTRE:
A) QUANTOS NÚMEROS FORAM DIGITADOS
B) A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE.
C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA.'''

lista = []

while True:
    valor = int(input('Digite um número:'))
    lista.append(valor)

    a = str(input('Número cadastrado! Deseja continuar? [S/N]'))
    if a in 'Nn':
        break

#LETRA A
print(f'A) Foram digitados {len(lista)} números')

#LETRA B
#COMANDO SORT NÃO FUNCIONA
lista.sort(reverse=True)
print(f'B) Lista em ordem decrescente:{lista}')

#LETRA C
if 5 in lista:
    print('C) O número 5 está na lista')
else:
    print('C) O número 5 não está na lista')
