# Conversor de temperatura Cº para Fº
# °F = °C × 1,8 + 32
# °C = (°F − 32) ÷ 1,8

valor = float(input('Informe a temperatura em ºC: '))
f = valor * 1.8 + 32

print('A temperatura de {}ºC corresponde a {}ºF'.format(valor, f))
