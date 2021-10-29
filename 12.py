# Ler preço de um produto e aplicar 5% de desconto

valor = float(input('Digite o atual valor do produto: '))
novoValor = valor - (valor * 5 / 100)

print('O valor do produto com 5% de desconto é: {:.2f}'.format(novoValor))