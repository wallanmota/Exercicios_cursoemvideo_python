'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))
# n3 = int(input('Digite o terceiro número: '))
#
# maior = n1
# menor = n3
#
# if n2 > maior:
#     maior = n2
# if n3 > maior:
#     maior = n3
# if n1 < menor:
#     menor = n1
# if n2 < menor:
#     menor = n2
#
# print('Os números digitados foram n1:{}, n2:{}, n3:{}'.format(n1, n2, n3))
# print('O maior número é o: {}'.format(maior))
# print('O menor número é o: {}'.format(menor))

quantidade = int(input('Quantos números vc quer digitar? '))
c = 0
numeros = []
while c < quantidade:
    entrada = int(input('Digite um número: '))
    numeros.append(entrada)
    c += 1

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print('Os números digitados foram: {}'.format(numeros))
print('O maior número digitado foi: {}'.format(maior))
print('O menor número digitado foi: {}'.format(menor))

