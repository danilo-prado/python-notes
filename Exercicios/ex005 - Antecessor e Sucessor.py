#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número:'))
a = n - 1
s = n + 1
print('Número:{}\nSucessor:{}\nAntecessor:{}'.format(n, s, a))