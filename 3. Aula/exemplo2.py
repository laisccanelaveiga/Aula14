import pandas as pd
import numpy as np


df_planilha_custos = pd.read_csv("planilha_de_custos.csv")

df_planilha_custos['Custo Total (R$)'] = (
    df_planilha_custos['Preco de Compra (R$)'] +
    (df_planilha_custos['Preco de Compra (R$)'] * df_planilha_custos['Imposto (%)'] /100) +
    df_planilha_custos['Frete (R$)'] +
    df_planilha_custos['Taxa Operacional (R$)']    
)

#Custo Central dos Produtos ====== Medidas de Tendência Central: Média
array_custo_total = np.array(df_planilha_custos['Custo Total (R$)']) #imprimi um conjunto de números

#Média
media = np.mean(array_custo_total)

#Mediana - valor que fica ao centro de uma distribuição - após valores serem ordenados
mediana = np.median(array_custo_total)

#Medidas de Posição
#Calculando Quartil
q1 = np.quantile(array_custo_total, 0.25)
q2 = np.quantile(array_custo_total, 0.50)
q3 = np.quantile(array_custo_total, 0.75)

print("-"*50)
print(f'Colunas: Produto e Custo Total')
print("-"*50)
print(df_planilha_custos[['Produto','Custo Total (R$)']].head(10))

print("-"*50)
print(f'Medias de Tendência Central')
print("-"*50)
print(f'Média: {media:.0f}')
print(f'Mediana: {mediana:.0f}') #50% dos Custos estão abaixo de 3133


print("-"*50)
print(f'Medidas de Posição (Quartil)')
print("-"*50)
print(f'Q1: {q1:.0f}') # 25% dos produto custam até 1667
print(f'Q2: {q2:.0f}') # 50% custam 3133
print(f'Q3: {q3:.0f}') # 75% dos produtos custam até 4479 e 25% acima desse valor


print("-"*50)
print(f'Menores')
print("-"*50)
menores = df_planilha_custos[df_planilha_custos['Custo Total (R$)'] < q1]
print(menores)

print("-"*50)
print(f'Maiores')
print("-"*50)
maiores = df_planilha_custos[df_planilha_custos['Custo Total (R$)'] > q3]
print(maiores)