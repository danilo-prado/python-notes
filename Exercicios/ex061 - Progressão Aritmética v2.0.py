'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while'''

a1 = int(input('Digite o primeiro termo de uma PA:'))
r = int(input('Digite a razão da PA:'))

c = 1
while c < 11:
    print(a1 + ((c - 1) * r), end=' -> ')
    c += 1
print('FIM')
