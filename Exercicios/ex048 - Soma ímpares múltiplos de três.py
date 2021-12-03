'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
 no intervalo de 1 até 500'''
'''print('NÚMERO ÍMPARES ENTRE 1 E 500')
for c in range(1, 500, 2):
    print(c)'''

print('NÚMERO IMPÁRES MÚLTIPLOS DE TRÊS')
s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma dos {} números é {}'.format(cont, s))

