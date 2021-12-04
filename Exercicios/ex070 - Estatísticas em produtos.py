'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar.
 No final, mostre:
 A) Qual é o total gasto na compra
 B) Quantos produtos custam mais de R$1000.
 C) Qual é o nome do produto mais barato'''

total = qnt = menor = cont = 0
barato = ' '
while True:
    name = str(input('Nome do produto: ')).upper().strip()
    price = float(input('Preço do produto: '))
    cont += 1
    total += price
    if price > 1000:
        qnt += 1

    if cont == 1:
        menor = price
        barato = name
    else:
        if price < menor:
            menor = price
            barato = name





    esc = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if esc == 'N':
        break
print('FIM')
print(f'Total da compra é R${total:.2f}')
print(f'{qnt} produtos custaram mais de R$1000,00 reais')
print(f'{barato} foi o produto mais barato, custando R${menor:.2f}')

