# Analisador de Textos

nome = input('Digite seu nome: ').strip()
nome_dividido = nome.split()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculasé {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', '')))) # opcao 1
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # opcao 2
print('Seu primeiro nome é {} e tem {} letras'.format(nome_dividido[0].title(), len(nome_dividido[0])))
