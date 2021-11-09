'''
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep
computador = randint(0, 5)

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2) #Pausa execução do código na quantidade de segundos informado

if jogador == computador:
    print('Acertou, eu pensei no número {}'.format(computador))
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))

