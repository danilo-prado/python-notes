#Escreva um programa que pergunte a quantidade de km
#percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

km = float(input('Digite a kilometragem:'))
dias = float(input('Digite quantos dias:'))

print('O preço a pagar é R${:.2f}'.format((km*0.15)+(dias*60)))