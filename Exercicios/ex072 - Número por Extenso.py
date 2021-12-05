'''CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSÃO, DE ZERO ATÉ VINTE.
SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO.'''

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
print(f'Você escolheu o número {tupla[n]}!')