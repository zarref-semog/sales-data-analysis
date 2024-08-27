import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados da planilha Excel
df = pd.read_excel('./data/vendas.xlsx', sheet_name='Vendas')

# Visualizar as primeiras linhas do DataFrame
print(df.head())

# Calcular o total de vendas
df['total_vendas'] = df['quantidade'] * df['preco']

# Total de vendas
total_vendas = df['total_vendas'].sum()
print(f'Total de vendas: R${total_vendas:.2f}')

# Quantidade vendida por produto
vendas_por_produto = df.groupby('produto')['quantidade'].sum()
print(vendas_por_produto)

# Gráfico de barras
vendas_por_produto.plot(kind='bar')
plt.title('Quantidade Vendida por Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.show()