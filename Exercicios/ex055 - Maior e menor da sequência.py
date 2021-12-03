'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''

maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input('Digite o peso da pessoa {}:'.format(c)))
    if c == 1:
        maior = c
        menor = c
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))




