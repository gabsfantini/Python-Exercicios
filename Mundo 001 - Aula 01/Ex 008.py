#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite um valor em metros:' ))
n1 = n * 100
n2 = n * 1000
print('{} metros em centimetros equivale a {:.0f} cm e em milimetros equivale a {:.0f} mm.'.format(n,n1,n2))