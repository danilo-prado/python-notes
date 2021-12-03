#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
import math
b = float(input('Digite o cateto adjacente:'))
c = float(input('Digite o cateto oposto:'))

#a = b ** 2 + c ** 2
#print('A hipotenusa é:{:.2f}'.format(math.sqrt(a)))
print(math.hypot(b , c))