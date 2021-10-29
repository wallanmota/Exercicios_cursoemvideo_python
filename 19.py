# Sorteando um item na lista

import random

alunos = []
qto_alunos = int(input('Quantos alunos irão participar do sorteio? '))
#logica 1
'''
num_sortado = random.randint(0, qto_alunos - 1)
for aluno in range(qto_alunos):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)
print(f'O aluno escolhido foi {alunos[num_sortado]}')
'''

#logica 2
for aluno in range(qto_alunos):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)
escolhido = random.choice(alunos)
print(f'O aluno escolhido foi {escolhido}')

