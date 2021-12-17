'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR (LARGURA E
COMPRIMENTO)E MOSTRE A ÁREA DO TERRENO'''

print('CONTROLE DE TERRENOS')
print('-' * 30)


def area():
    a = l * c
    print(f'A área de um terreno {l:.2f}m x {c:.2f}m é {a:.2f}m²')


l = (float(input('LARGURA [m]: ')))
c = (float(input('COMPRIMENTO [m]: ')))
area()
