''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
Ex: Ana Maria de Souza
primeiro=Ana
último=Souza'''

nome = str(input('Digite seu nome completo:').strip())
print('Primeiro nome:{}'.format(nome[0:nome.find(' ')]))
print('último nome:{}'.format(nome[nome.rfind(' '):]))