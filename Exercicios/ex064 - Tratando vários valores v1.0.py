'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)'''

qnt = 0
soma = 0

n = int(input('Digite um número [999 para parar]: '))

while n != 999:
    qnt += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('FIM')

print('Números digitados: {}\nA soma dos números digitados: {}'.format(qnt, soma))