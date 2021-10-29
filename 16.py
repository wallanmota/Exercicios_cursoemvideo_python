# QUEBRANDO UM NUMERO

from math import trunc

num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {:.0f}'.format(num, num))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
