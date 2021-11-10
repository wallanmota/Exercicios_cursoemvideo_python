'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

num = int(input('\33[35mMe diga um número qualquer:\33[m '))

if num % 2 == 0:
    print('O número {} é \33[32mPAR\33[m!'.format(num))
else:
    print('O número {} é \33[36mÍMPAR\33[m!'.format(num))
