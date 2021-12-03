'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima: MASTER'''

ano = int(input('Digite o seu ano de nascimento:'))
idade = 2021 - ano
print('Sua idade é {} ano(s)'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL')
elif 14 < idade <= 19:
    print('Sua categoria é JUNIOR')
elif 19 < idade <= 20:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria é MASTER')

