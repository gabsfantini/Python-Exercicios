#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Nota 1º Bimestre: '))
n2 = float(input('Nota 2º Bimestre: '))
media = (n1 + n2) / 2
print('A sua média somando a nota do 1º e do 2º Bimestre é {}'.format(media))
