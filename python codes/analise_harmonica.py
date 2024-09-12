# importar as bibliotecas a ser usadas
import pandas as pd
import utide
from utide import solve
import matplotlib as plt
import numpy as np

#carrega
# r os dados do arquivo txt
data = pd.read_csv('d:\Gabriel\finaltcc\Resultados\casananointeiro\maregrafoponte_medido.csv', delimiter=',')
#converter as colunas de data e hora para um projeto datetime
data['data'] = pd.to_datetime(data['data'], format='%Y/%m/%d %H:%M')


#definir os valores observados como a terceira coluna
observed_values = data['nivel']
#latitude onde foram feitas as medições 
latitude = -27.67
    
# executar a análise harmonica de marés com utide.solve()

coef = solve(data['data'], observed_values, lat=latitude)

#exibir os coeficientes calculados
import matplotlib.pyplot as plt

#recostruir a maré com base em consituintes encontrado no coef
tide_tt = utide.reconstruct(data['data'], coef)

# plotar os resultados usando matplotlib
#plt.plot(data['data'], observed_values, label='Observado')
plt.plot(data['data'], tide_tt['h'], label='Astronômico')
plt.plot(data['data'], tide_tt2['h'], label='Modelo')
#plt.plot(data['data'], tide_meteo, label='Meteorológico')
plt.xlabel('Data')
plt.ylabel('Nível da Maré')
plt.legend()
plt.title(f'Comparação entre Astronômico e Modelo (r_square = {round(r2, 2)} - correlação= {round(correlation,2)}- rmse= {round(rmse,2)})')
plt.show()