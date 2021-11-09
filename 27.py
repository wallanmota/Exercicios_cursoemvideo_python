# Primeiro e último nome de uma pessoa
'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''

nome = input('Digite o nome completo: ').strip()
nome_dividido = nome.split()

print('O primeiro nome da pesso é {}'.format(nome_dividido[0]))
print('O ultimo nome da pesso é {}'.format(nome_dividido[len(nome_dividido)-1]))





