'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos'''

cont = men = women = 0

while True:
    age = int(input('Digite a idade: '))
    if age > 18:
        cont += 1
    gender = str(input('Digite o sexo: [M/F]')).upper().strip()[0]
    if gender == 'M':
        men += 1
    print('-'*10)
    ask = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if gender == 'F' and age < 20:
        women += 1
    if ask == 'N':
        print(f'Há {cont} pessoa(s) maior(es) de 18 anos')
        print(f'Há {men} homen(s) cadastrado(s)')
        print(f'Há {women} mulhere(s) com menos de 20 anos')
        break
