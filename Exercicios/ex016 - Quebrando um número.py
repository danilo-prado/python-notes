#Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira.
#Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

import math
n = float(input('Digite um número:'))
int = math.trunc(n)
print('O número {}tem a parte inteira {}'.format(n, int))