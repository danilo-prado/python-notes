'''CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS).
DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS.'''

tupla = ('aprender', 'programar', 'linguagem')

for p in tupla:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
