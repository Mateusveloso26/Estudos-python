import pandas as pd

tabela_clientes = pd.read_csv("clientes.csv")
print (tabela_clientes) #DataFrame é uma estrutura de dados que organiza os dados em uma tabela bidimensional de linhas e colunas, como uma planilha.
print(tabela_clientes["idade"])  # Series é uma das colunas do DataFrame.

# Transforma um dicionario em um DataFrame.
dicionario_produtos = {"nome":["iphone", "ipad", "airpod"], "preco": [5000,9000,2400], "estoque": [100,70,30]}
tabela_produtos = pd.DataFrame(dicionario_produtos)
print(tabela_produtos)
