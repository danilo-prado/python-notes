'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS: INÍCIO. FIM E PASSO E REALIZE A
CONTAGEM.
SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
A) DE 1 ATÉ 10, DE 1 EM 1
B) DE 10 ATÉ 0, DE 2 EM 2
C) UMA CONTAGEM PERSONALIZADA'''

from time import sleep


#LETRA A
'''def contador(i, f, p):
    while i <= f:
        print(i, end=' ')
        i += p
        sleep(1)
    print('FIM!')


print('A) Contagem de 1 até 10 de 1 em 1:')
contador(1, 10, 1)'''

#LETRA B
'''def contador(i, f, p):
    while i >= f:
        print(i, end=' ')
        i -= p
        sleep(1)
    print('FIM!')


print('B) Contagem de 10 até 0 de 2 em 2:')
contador(10, 0, 2)'''


#LETRA C
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p ==0:
        p =1
    if i < f:
        while i <= f:
            print(i, end=' ')
            i += p
            sleep(1)
        print('FIM!')
    else:
        while i >= f:
            print(i, end=' ')
            i -= p
            sleep(1)
        print('FIM!')


contador(i=int(input('INÍCIO:')), f=int(input('FIM: ')), p=int(input('PASSO: ')))
