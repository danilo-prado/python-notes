''' Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120'''


n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    f *= c
    c -=1
print(f)






'''FORMA INCORRETA
n = int(input('Digite um número: '))

n = 0
while n == 1:
    for c in range(n, 1, -1)
        n * c'''