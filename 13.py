# Ler salario de um funcionario e aplicar 15% de aumento

salario = float(input(('Digite seu salário: ')))
novoSalario = salario + (salario * 15 / 100)

print('Seu novo salario é: {:.2f}'.format(novoSalario))
