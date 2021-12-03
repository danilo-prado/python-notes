'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome'''
nome = str(input('Digite um nome:').strip())
existe = 'SILVA' in nome.upper()
print(existe)