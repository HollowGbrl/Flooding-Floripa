import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
import utide
from utide import solve
import os

file = 'dados_daniel/imbi_718_2001_2022_atualizado.txt'
lat = -28.26

data = pd.read_csv(file, delimiter=',')
data['data'] = pd.to_datetime(data['data'], format='%Y-%m-%d %H:%M:%S')

coef_mod = solve(data['data'], data['nivel'], lat=lat)

tide_tt = utide.reconstruct(data['data'], coef_mod)


#Subtração da meré medido pela astronomica para obter a maré meteorologica
tide_meteo = data['nivel'] - tide_tt['h']

data['tide_meteo'] = tide_meteo

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))


#fixxx
tide_tt['h'] = tide_tt['h'] - tide_tt['h'].mean()
data['nivel'] = data['nivel'] - data['nivel'].mean()



# Plot data1 on the first subplot
#ax1.plot(data['data'], data['nivel'], label='Dado bruto', color='gray')
#ax1.set_ylabel('Nivel(m)')
#ax1.legend()
#ax1.set_ylim(-1, 1.5)
#ax1.grid(True)
#
#
#
## Plot data2 on the second subplot
#ax2.plot(data['data'], tide_tt['h'], label='Astronômico')
#ax2.plot(data['data'], data['tide_meteo'], label='Meteorológico')
#ax2.set_ylim(-1, 1.5)
#ax2.set_xlabel('Tempo')
#ax2.set_ylabel('Nivel(m)')  
#ax2.legend()
#ax2.grid(True)
## Adjust spacing between subplots
#plt.tight_layout()
#
## Save the figure
##plt.savefig('../finaltcc/imagens/multiplot_imbituba.pdf')
#
## Show the figure
#plt.show()
#