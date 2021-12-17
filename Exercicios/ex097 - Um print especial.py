'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA
MENSAGEM COM TAMANHO ADAPTÁVEL.
EX: ESCREVA('OLÁ MUNDO!')

SAÍDA

-----------
OLÁ, MUNDO!
-----------'''

def escreva():
    print('~' * len(frase))
    print(frase)
    print('~' * len(frase))


frase = input('Digite: ')
escreva()
