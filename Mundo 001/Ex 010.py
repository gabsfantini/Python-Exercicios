#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

din = float(input('Digite quanto você tem de dinheiro em carteira: R$ '))
dol = din // 5.02
print('Com R$ {} você consegue comprar $ {:.2f}'.format(din,dol))