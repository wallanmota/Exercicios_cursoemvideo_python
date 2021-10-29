import openpyxl as openpyxl
import pandas as pd  # (as pd) é para renomear para pd

# Data Frame
df = pd.read_excel('estudo_io.xlsx')
# print(df.index)
# print(df)

# dropna() => remove as linhas q tem valores nulos
df1 = df.dropna()
# print(df1)

# fillna() => insere valor nos campos nulos
df2 = df.fillna(0)
# print(df2)

# print(df['nome']) # Acessa coluna
# print(df.loc[3]) # Acessa a linha

# df.sort_values(by='nome', inplace=True) # Organiza por ordem alfabetica
# print(df)

# Criar coluna nova
# df['teste'] = 'teste'

# Deletar coluna
# del df['teste']

# df.loc[[0, 3]] # Acessa multiplas linhas
# df.loc[[1, 4], ['nome', 'gastos co estudos']] # Acessa linhas e coluna

# print(df.dtypes) # Mostra o tipo das colunas

# print(df.to_string(index=False)) # Mostra tabela completa

print(df)
