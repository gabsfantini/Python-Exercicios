#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
from math import sqrt
n = int(input('Digite um número: '))
n1 = n * 2
n2 = n * 3
n3 = sqrt(n)
print('Analisando o número {}, o seu dobro é {}, o seu triplo é {} e a sua raiz quadrada é {:.0f}'.format(n,n1,n2,n3))
