#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
temp = float(input('Digite a temperatura:'))
conv = (temp*(9/5))+32
print('A temperatura convertida é: {:.1f}ºF'.format(conv))