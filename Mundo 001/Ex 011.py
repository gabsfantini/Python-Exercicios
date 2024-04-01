#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

comprimento = float(input('Digite a comprimento da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = altura * comprimento
tinta = area * 2
print('A sua parede tem {}m² e você vai precisar de {:.2f} litros de tinta para pintar ela toda.'.format(area, tinta))