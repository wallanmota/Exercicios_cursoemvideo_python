# Dissecando variável

# var = input("Digite algo:")

# tipo = type(var)
# numero = var.isnumeric()
# letra = var.isalpha()
# alnu = var.isalnum()
#
# if numero == True:
#     numero = 'sim'
# else:
#     numero = 'Não'
#
# if letra == True:
#     letra = 'Sim'
# else:
#     letra = 'Não'
#
# if alnu == True:
#     alnu = 'Sim'
# else:
#     alnu = 'Não'
#
# print(f'O tipo primitivo do valor digitado é: {tipo}')
# print(f'O valor é numeros: {numero}')
# print(f'O valor é letras: {letra}')
# print(f'O valor é Alfanumerico: {alnu}')

####### SOLUÇÃO ##########

var = input("Digite algo:")

print('O tipo primitivo desse valor é:', type(var))
print('Só tem espaço:', var.isspace())
print('É um numero:', var.isnumeric())
print('É alfabetico:', var.isalpha())
print('É alfanumerico:', var.isalnum())
print('Esta em maiusculas:', var.isupper())
print('Esta em minuscula:', var.islower())
print('Esta capitalizada:', var.istitle())
