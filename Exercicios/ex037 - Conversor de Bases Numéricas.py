'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal'''

n = int(input('Digite um número inteiro:'))
print('''Escolha uma base para conversão:
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
base = int(input('Digite sua opção:'))

if base == 1:
    print(bin(n)[2:])
elif base == 2:
    print(oct(n)[2:])
elif base == 3:
    print(hex(n)[2:])
else:
    print('Opção inválida')