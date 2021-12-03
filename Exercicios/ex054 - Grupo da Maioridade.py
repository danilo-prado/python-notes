'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores'''

menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da pessoa {}:'.format(c)))
    if 2021 - ano < 18:
        menor += 1
    elif 2021 - ano > 18:
        maior += 1
print('{} pessoas são menores e {} são maiores'.format(menor, maior))







