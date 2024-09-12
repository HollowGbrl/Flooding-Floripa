import pandas as pd
import matplotlib.pyplot as plt
import utide as ut

df = pd.read_csv('dados_daniel/imbi_718_2001_2021.txt_edit.csv', delimiter=',')
lat = -28.26
df2 = pd.read_csv('dados_daniel/imbi_2020_doubleedit.csv', delimiter=',')
df2['data'] = pd.to_datetime(df2['data'], format='%Y-%m-%d %H:%M:%S')

start_date = '2019-12-31'
end_date= '2021-01-01'

df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d %H:%M')
coef_mod = ut.solve(df['data'], df['nivel'], lat=lat)
tide_tt = ut.reconstruct(df['data'], coef_mod)

#Subtração da meré medido pela astronomica para obter a maré meteorologica
tide_meteo = df['nivel'] - tide_tt['h']
df['tide_meteo'] = tide_meteo





dataplot = df[(df['data'] >= start_date) & (df['data'] <= end_date)]

dataplot.to_csv('dados_daniel/imbituba_meteo_2020inteiro.csv', index=False)

#
#plt.plot(df2['data'], df2['nivel'], label='Dado bruto', color='gray')
#plt.plot(dataplot['data'], dataplot['tide_meteo'], label='Astronômico')
#plt.legend()
#
#plt.show()
#