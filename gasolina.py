# código de geração do gráfico 
#Importando
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Criando um dataframe com o arquivo csv
venda_df = pd.read_csv('gasolina.csv', sep=',')
#Criando a figura
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=venda_df, x='dia', y='venda', color='green')
  grafico.set(title='Preço médio de venda da gasolina', xlabel='Dia', ylabel='Preco');

plt.savefig('gasolina.png')