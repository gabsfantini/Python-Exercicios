#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Digite a temperatura em ºC: '))
f = (temp * 1.8) + 32
print('A temperatura {}ºC equivale a {} ºF'.format(temp,f))