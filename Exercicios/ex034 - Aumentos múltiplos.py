'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$1.250 calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%'''

sal = float(input('Digite seu salário:'))

if sal >= 1250:
    print('Seu aumento é de 10%, ou seja seu novo salário é R${:.2f}'.format(sal * 1.1))
else:
    print('Seu aumento é de 15%, ou seja seu novo salário é R${:.2f}'.format(sal * 1.15))