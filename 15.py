# Aluguel de carros
# input => dias e kms
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias vc ficou com o carro? '))
km = float(input('Quantos KMs vc rodou com o carro? '))

total = (dias * 60) + (km * 0.15)
print(f'O valor total a pagar é: R${total}')
k