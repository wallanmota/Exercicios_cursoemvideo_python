# Catetos e Hipotenusa

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimeto do cateto adjacenter: '))
# Solução 1 => Resolvendo mátematicamente
h = (co ** 2 + ca ** 2) ** (1/2)

#Suloção 2 => com metodo hypot da modolo math
import math
hi = math.hypot(co, ca)

print('Matemáticamente => A hipotenusa vai medir {:.2f}'.format(h))
print('Método Hypot => A hipotenusa vai medir {:.2f}'.format(hi))
