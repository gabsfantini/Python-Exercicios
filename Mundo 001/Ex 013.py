#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe seu salário atual: '))
aumento = (salario * 15/100) + salario
print('Seu salário é {} e seu novo salário será {}'.format(salario,aumento))
