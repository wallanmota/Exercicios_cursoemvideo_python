# Primeira e última ocorrência de uma string
'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = input('Digite uma frase: ').strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.lower().find('a')+1))
print('A ultima letra "A" apareceu na posição {}'.format(frase.lower().rfind('a')+1))
