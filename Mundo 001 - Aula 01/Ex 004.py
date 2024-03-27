#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é' ,type(a))
print('Só tem espaços?' ,a.isspace())
print('É um número?' ,a.isnumeric())
print('É alfabético?' ,a.isalpha())
print('É alfa-numérico?' ,a.isalnum())
print('Está todo em maiúsculas?' ,a.isupper())
print('Está em todo em minúsculas?' ,a.islower())
print('Está capitalizada?' ,a.istitle())
