'''
 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

import datetime
from calendar import isleap

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
data = datetime.date.today()
ano_atual = data.year

if ano == 0:
    ano = ano_atual
if isleap(ano):
    print('O ano {} é \33[36mBISSEXTO\33[m!'.format(ano))
else:
    print('O ano {} não é \33[31mBISSEXTO\33[m!'.format(ano))

# Expressao para saber se é bissexto
# ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0