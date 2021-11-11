'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''

sg1 = float(input('Primeiro segmento: '))
sg2 = float(input('Segundo segmento: '))
sg3 = float(input('Terceiro segmento: '))

if sg1 + sg2 > sg3 and sg1 + sg3 > sg2 and sg2 + sg3 > sg1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')