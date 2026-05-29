import pandas as pd 
import openpyxl

df_vendas_roupas = pd.read_excel('vendas_roupas.xlsx')

primeiras_vendas = df_vendas_roupas.head()
maior_valor = df_vendas_roupas['Faturamento Total (R$)'].max()
menor_valor = df_vendas_roupas['Faturamento Total (R$)'].min()
media_faturamento = df_vendas_roupas['Faturamento Total (R$)'].mean()


print(primeiras_vendas)
print(f'\nQuantidade total de produtos vendidos: R$ {df_vendas_roupas['Unidades Vendidas'].sum()}')
print(f'\nMédia de Preços dos Produtos: R$ {df_vendas_roupas['Preço por Unidade (R$)'].mean()}')
print(f'\nProd - Maior Valor de Faturamento: {df_vendas_roupas[df_vendas_roupas["Faturamento Total (R$)"]== maior_valor][['Produto']]}')
print(f'\nProd - Menor Valor de Faturamento: {df_vendas_roupas[df_vendas_roupas["Faturamento Total (R$)"]== menor_valor][['Produto','Faturamento Total (R$)']]}')
print(f'\nProduto com Satisfação - BAIXA: {df_vendas_roupas[df_vendas_roupas["Satisfação"]== "BAIXO"][['Produto','Satisfação']]}')
print(f'\nProduto com Satisfação - MUITO ALTA: {df_vendas_roupas[df_vendas_roupas["Satisfação"]== "MUITO ALTO"][['Produto','Satisfação']]}')
print(f'Produtos - Faturamento Acima da Média: {df_vendas_roupas[df_vendas_roupas["Faturamento Total (R$)"]>media_faturamento][['Produto','Faturamento Total (R$)']]}')


