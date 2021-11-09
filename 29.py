'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = int(input('Digite a velocidade do carro... '))
velocidade_maxima = 80

if velocidade > velocidade_maxima:
    valor_multa = float((velocidade - velocidade_maxima) * 7)
    print('MULTADO! por andar acima da velocidade máxima permitida que é 80km/h! ')
    print('O valor da multa é R${:.2f}'.format(valor_multa))
print('Tenha um bom dia! Dirija com segurança!')