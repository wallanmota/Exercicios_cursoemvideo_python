# Sorteando uma ordem na lista

import random

nomes = []
qtd_nome = int(input('Quantos nomes serão adicionados a lista? '))

for nome in range(qtd_nome):
    nome = input('Digite o nome: ')
    nomes.append(nome)

random.shuffle(nomes)

print(f'A ordem de apresentação será:\n{nomes}')