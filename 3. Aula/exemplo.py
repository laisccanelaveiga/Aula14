import pandas as pd
import numpy as np

df_vendas_moveis = pd.read_csv("planilha_moveis.csv")
primeiras_vendas = df_vendas_moveis.head(10)
print(primeiras_vendas)

df_vendas_moveis['Total Vendido'] = (df_vendas_moveis['Vendidos'] * df_vendas_moveis['Preco'])
print(df_vendas_moveis)

array_preco = np.array(df_vendas_moveis['Total Vendido'])
q1 = np.quantile(array_preco,0.25)
q2 = np.quantile(array_preco,0.50)
q3 = np.quantile(array_preco,0.70)


media = np.mean(array_preco)
mediana = np.median(array_preco)
menores = df_vendas_moveis[df_vendas_moveis['Total Vendido'] < q1]
maiores = df_vendas_moveis[df_vendas_moveis["Total Vendido"] > q3]


print("==Padrão Central de Vendas==")
print(f'Média: R$ {media:.2f}\nMediana: R$ {mediana:.2f}')
print("-"*50)

print('\nAnálise dos Dados')
print(f"Os produtos com venda abaixo de R$ {q1:.2f} são os que possuem menor valor agregado e representam 25% do total.")
print(f"Enquanto as vendas acima de R$ {q3:.2f} são as de maior representatividade financeira.")
print(f"Portanto 50% estão na faixa entre R$ {q1 + 1:.2f} - R$ {q3 - 1:.2f} com média de R$ {q2:.2f}\n")
print(f'Deve-se observar que entre os produtos de maior valor agregado 35% tem satisfação de Nível Baixo e precisam de atenção ')

print("-"*50)
print('Produtos de Menor Valor')
print(menores[['Produto','Satisfacao']])

print("-"*50)
print('\nProdutos de Maior Valor')
print(maiores[['Produto','Satisfacao']])

print('\n% Satisfação dos Produtos de Maior Valor')
percentual = maiores['Satisfacao'].value_counts(normalize=True)*100
print(percentual.map('{:.2f}'.format))


