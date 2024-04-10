#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto: '))
desconto = preço - (preço * 5 / 100)
print('O valor do produto é \033[0;032mR$ {:.2f}\033[m e com 5% de desconto passa a ser \033[4;034mR$ {:.2f}\033[m'.format(preço, desconto))
