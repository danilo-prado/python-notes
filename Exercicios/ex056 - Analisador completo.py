'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo
Qual o nome do homem mais velho
Quantas mulheres têm menos de 20 anos'''


somaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheres = 0


for c in range(1, 5):
    print('----{}ª PESSOA----'.format(c))
    nome = str(input('Nome:'.format(c)))
    idade = int(input('Idade:'.format(c)))
    sexo = str(input('Sexo [M/F]:'.format(c)))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        mulheres += 1


mediaidade = somaidade / 4
print('A média de idade é {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('{} mulher(es) tem menos de 20 anos'.format(mulheres))




