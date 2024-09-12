import pandas as pd
import utide
import matplotlib.pyplot as plt

#arquivo= 'dados daniel/imbi_718_2001_2021.txt'
#with open(arquivo, 'r') as f, open('imbituba.csv', 'w') as f2:
#    f2.write('data,nivel\n')
#    for linha in f:
#        linha2=linha.split('\t')
#        f2.write(f'{linha2[0]} {linha2[1]},{linha2[2]}')


arquivo= 'imbituba.csv'
mare = pd.read_csv(arquivo, sep=',')

mare['data'] = pd.to_datetime(mare['data'], format='%d/%m/%Y %H:%M')

#analise harmonic
coef = utide.solve(mare['data'], mare['nivel'], lat=-28.225)
ttide = utide.reconstruct(mare['data'], coef)

#Subtração da meré medido pela astronomica para obter a maré meteorologica
mare['nivel_meteo'] = mare['nivel'] - ttide['h']
mare['nivel_meteo'] = mare['nivel_meteo'] - mare['nivel_meteo'].mean()





mare['nivel_meteo'] = mare['nivel_meteo'].round(3)
mare.drop(columns=['nivel'], inplace=True)
#pd.DataFrame(mare).to_csv('imbituba_meteo_round.csv', index=False)

#mare = mare[(mare['data'].dt.year >= 2001) & (mare['data'].dt.year <= 2010)]
#pd.DataFrame(mare).to_csv('imbituba_meteo_round_2001_2010.csv', index=False)

mare = mare[(mare['data'].dt.year >= 2020) & (mare['data'].dt.year <= 2021)]
#pd.DataFrame(mare).to_csv('imbituba_meteo_round_2019_2021.csv', index=False)


plt.plot(mare['data'], mare['nivel_meteo'], label='meteorológica')
#plt.plot(mare['data'], mare['nivel']+1, label='Medido')
#plt.plot(mare['data'], ttide['h']+3, label='Astronômica')
plt.xlabel('Data')
plt.ylabel('Nível da Maré')
plt.legend()
#plt.title(f'Comparação entre Astronômico e Modelo (r_square = {round(r2_astro, 2)} - correlação= {round(correlation_astro,2)}- rmse= {round(rmse_astro,2)})')
plt.show()


