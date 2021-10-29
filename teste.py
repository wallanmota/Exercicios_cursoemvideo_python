def div(n1, n2):
    try:
        result = n1 /n2
    except ZeroDivisionError:
        print('Não pode dividir por 0')
    except:
        print('Valor informado inválido!')
    else:
        print(f'O reultado da divisão é {result}')
    finally:
        print('Função executada')

div()

'''
git remote add origin https://...
git branch -M master
git push -u origin master
'''