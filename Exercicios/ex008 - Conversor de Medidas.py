#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Digite a metragem:'))
c = n * 100
m = n * 1000
print('O valor em centímetros é {:.0f} e em milímetros é {:.0f}'.format(c, m))