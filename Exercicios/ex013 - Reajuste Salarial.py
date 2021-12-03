#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Digite o seu salário: R$'))
aumento = sal * 1.15
print('Seu novo salário é R${:.2f}'.format(aumento))