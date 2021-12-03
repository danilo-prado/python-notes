'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida'''

print('CALCULADORA DE IMC')

print('O cálculo do IMC é utilizado para analisar se seu peso está de acordo com sua altura')
peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))

imc = peso / (altura ** 2)

print('Sua categoria é:')
if imc <= 18.5:
    print('ABAIXO DO PESO')
elif 18.5 < imc <= 25:
    print('PESO IDEAL')
elif 25 < imc <= 30:
    print('SOBREPESO')
elif 30 < imc <= 40:
    print('OBESIDADE')
else:
    print('GIGANTESCO')
