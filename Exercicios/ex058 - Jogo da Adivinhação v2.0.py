'''Melhore o jogo DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
 adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
n = -1
cpu = randint(0, 10)
palpites = 0
while n != cpu:
      n = int(input('Tente adivinhar o número:'))
      palpites += 1
print('ACERTOU, você precisou de {} palpite(s) para acertar!'.format(palpites))
