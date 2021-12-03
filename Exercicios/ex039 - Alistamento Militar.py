'''Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar
Se é a hora de se alistar
Se já passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo '''

ano = int(input('Digite o seu ano de nascimento:'))
idade = 2021 - ano
print('Sua idade atual é {} anos'.format(idade))

if idade == 18:
    print('Hora de se alistar amigão!')
elif idade < 18:
    print('Falta {} ano(s) para alistar'.format(18 - idade))
elif idade > 18:
    print('Você passou do prazo {} ano(s)'.format(idade - 18))