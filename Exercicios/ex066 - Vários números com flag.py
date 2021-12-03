'''Crie um programa que leia vários número inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)'''

soma = cont = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou \033[0:37:40m{cont}\033[m números e a soma deles foi \033[0:37:40m{soma}\033[m')
