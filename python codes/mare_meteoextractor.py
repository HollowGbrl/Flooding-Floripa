#Código para extrair de uma timeseries de dado de nível (marégrafo) as constantes harmonicas e a maré meteorológica
import pandas as pd
import utide
import matplotlib.pyplot as plt

#timeseries de dado de nível e ajustar os dados dela
arquivo= 'imbituba.csv'
mare = pd.read_csv(arquivo, sep=',')
mare['data'] = pd.to_datetime(mare['data'], format='%d/%m/%Y %H:%M')

#analise harmonica com Utide
coef = utide.solve(mare['data'], mare['nivel'], lat=-28.225)
ttide = utide.reconstruct(mare['data'], coef)

#Subtração da meré medido pela astronomica para obter a maré meteorologica
mare['nivel_meteo'] = mare['nivel'] - ttide['h']
#processamento do dado para deixar ele limpo (opcional)
mare['nivel_meteo'] = mare['nivel_meteo'] - mare['nivel_meteo'].mean()
mare['nivel_meteo'] = mare['nivel_meteo'].round(3)
mare.drop(columns=['nivel'], inplace=True)
mare = mare[(mare['data'].dt.year >= 2020) & (mare['data'].dt.year <= 2021)]
#plotando o dado
plt.plot(mare['data'], mare['nivel_meteo'], label='meteorológica')
plt.xlabel('Data')
plt.ylabel('Nível da Maré')
plt.legend()
plt.show()


