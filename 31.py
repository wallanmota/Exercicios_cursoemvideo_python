'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.
'''

distancia = float(input('Qual a distancia da sua viagem? '))

# Forma simplificada (tipo operador ternário)
preco = distancia * 0.45 if distancia > 200 else distancia * 0.50

# Forma tradicional
# if distancia > 200:
#     preco = distancia * 0.45
# else:
#     preco = distancia * 0.50

print('Você está prestes a começar uma viagem de {:.1f}km'.format(distancia))
print('O preço da sua passagem será de R${:.2f}'.format(preco))
