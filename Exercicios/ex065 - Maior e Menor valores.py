'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
 e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''

r = 'S'
soma = media = cont = 0
maior = 0
menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    media = soma / cont
    r = str(input('Quer continuar? [S/N] ')).upper()
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('''A soma de todos os valores é {}.
A média é de {}.
O maior número é {}.
O menor número é {}.'''.format(soma, media, maior, menor))