# Verificando as primeiras letras de um texto
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite a cidade onde vc nasceu: ').strip()
print('SANTO' in cidade[:5].upper())
print(cidade[:5].upper() == 'SANTO')