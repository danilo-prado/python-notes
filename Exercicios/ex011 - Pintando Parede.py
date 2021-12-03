#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
area = l * a
tinta = area / 2
print('A área é {} m² e a quantidade de tinta é {} litros'.format(area, tinta))