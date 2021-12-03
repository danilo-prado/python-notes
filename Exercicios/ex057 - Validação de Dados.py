'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto'''


masc = 'M'
fem = 'F'
sexo = 0
while sexo != masc and sexo != fem:
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
print('FIM')