#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite um ângulo:'))

print('O sen de {:.0f} é {:.1f}, o cos é {:.1f} e a tan é {:.1f}'.format(a, math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))