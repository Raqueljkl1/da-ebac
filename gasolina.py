#Importando o Pandas e o Seaborn
import pandas as pd
import seaborn as sns

#Criando um dataframe com o arquivo csv
venda_df = pd.read_csv('gasolina.csv', sep=',')
#Criando a figura
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=venda_df, x='venda', y='dia', color='purple')
  grafico.set(title='Preço médio de venda da gasolina em São Paulo ', xlabel='Dia', ylabel='Preco');
