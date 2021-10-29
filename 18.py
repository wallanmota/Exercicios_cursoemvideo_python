# Seno, Cosseno e Tangente

# import math
from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo: '))
angulo = radians(angulo)
'''
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
'''
s = sin(angulo)
c = cos(angulo)
t = tan(angulo)

print('O seno do angulo é: {:.4f}\nO cosseno do angulo é: {:.4f}\nA tangente do angulo é: {:.4f}'.format(s, c, t))
