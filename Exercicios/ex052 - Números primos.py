'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''

'''n = int(input('Digite um número:'))

for c in range(1, 10):
    primo = n % c
    if primo == 0:
        print('É um número primo')
    else:
        print('Não é um número primo')'''

n = int(input('Digite um número: '))
total = 0
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divizível {} vez(es)'.format(n, total))
if total == 2:
    print('{} é um número primo'.format(n))
else:
    print('{} não é um número primo'.format(n))
