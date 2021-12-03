'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite'''

vel = int(input('Digite a velocidade do carro:'))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado em R${:.2f}'.format(multa))
else:
    print('Tudo certo amigão, segue o jogo')