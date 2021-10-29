# Separando dígitos de um número
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = input('Informe um número: ')
'''
if len(numero) == 4:
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]
elif len(numero) == 3:
    unidade = numero[2]
    dezena = numero[1]
    centena = numero[0]
    milhar = 0
elif len(numero) == 2:
    unidade = numero[1]
    dezena = numero[0]
    centena = 0
    milhar = 0
else:
    unidade = numero[0]
    dezena = 0
    centena = 0
    milhar = 0
print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')
'''

# Fatiando matematicamente

u = int(numero) // 1 % 10
d = int(numero) // 10 % 10
c = int(numero) // 100 % 10
m = int(numero) // 1000 % 10
print(f'Unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')
