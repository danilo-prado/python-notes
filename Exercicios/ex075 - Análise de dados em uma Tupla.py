'''DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:
A) QUANTAS VEZES APARECEU O VALOR 9
B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
C) QUAIS FORAM OS NÚMEROS PARES'''

tupla =  (int(input('Digite um valor:')),
int(input('Digite um valor:')),
int(input('Digite um valor:')),
int(input('Digite um valor:')))

print(tupla)

print(f'A) O número 9 apareceu {tupla.count(9)} vezes')
if 3 not in tupla:
    print('B) Não há número 3 na tupla!')
else:
    print(f'B) O primeiro valor 3 foi digitado na posição {tupla.index(3)}')

print('C) Os valores pares digitados foram ', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
