'''Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes'''

a = float(input('Digite uma reta:'))
b = float(input('Digite a outra reta:'))
c = float(input('Digite mais uma reta:'))


if (a + b) > c and (b + c) > a and (c + a) > b:
    print('É um triângulo', end=' ')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Não é um triângulo')