import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

#Leitura do arquivo Iris
planta = pd.read_csv("iris.csv")

#Exibindo 5 linhas do Dataframe
print(planta.head()) #Se nenhum número for colocado, ele irá exibir as 5 primeiras linhas do Dataframe

#Resumo de informações das colunas
planta.describe() #Permite descrever a média, desvio padrão, etc... (bom para gerar estatísticas)

#Tipo de dados em cada coluna
planta.dtypes

#Quantidade total de linhas e colunas, respectivamente
#print(planta.shape)

#Renomeando as colunas
