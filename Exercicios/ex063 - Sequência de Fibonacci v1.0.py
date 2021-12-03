'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
Sequência de Fibonacci
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''


print('SEQUÊNCIA DE FIBONACCI')

n = int(input('Digite quantos termos você deseja:'))

cont = 3
a1 = 0
a2 = 1

print(a1, end=' -> ')
print(a2, end=' -> ')
while cont <= n:
    print(a1 + a2, end=' -> ')
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    cont += 1
print('FIM')