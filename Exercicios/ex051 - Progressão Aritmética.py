'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão'''

a1 = int(input('Digite o primeiro termo de uma PA:'))
r = int(input('Digite a razão da PA:'))

for c in range(1,11):
    print(a1 + ((c - 1) * r), end=' -> ')
print('FIM')