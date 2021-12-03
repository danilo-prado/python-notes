'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra A
Em que posição ela aparece a primeira vez
Em que posição ela aparece a ultima vez'''

frase = str(input('Digite uma frase:').strip().upper())

print('A frase tem {} letras A'.format(frase.count('A')))
print('Na posição {} pela primeira vez'.format(frase.find('A')+1))
print('Na posição {} pela última vez'.format(frase.rfind('A')+1))