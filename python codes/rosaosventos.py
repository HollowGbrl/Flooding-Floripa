import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import windrose as wr



pasta= '../finaltcc/Resultados/BASE'
filesaida= f'{pasta}/windspedir.csv'

ventoxfile = f'{pasta}/windx.csv'
ventoyfile = f'{pasta}/windy.csv'


#adjust the delft file into one dataframe
ventox = pd.read_csv(ventoxfile, delimiter=',')
ventoy = pd.read_csv(ventoyfile, delimiter=',')
time0, u0 = ventox.columns[0], ventox.columns[1]
ventox.rename(columns={time0:'time', u0:'u10'}, inplace=True)
ventoy.rename(columns={time0:'time', u0:'v10'}, inplace=True)
ventoxy = ventox.merge(ventoy, on='time')

ventoxy['u10'] = ventoxy['u10'].str.replace('_', '.')
ventoxy['v10'] = ventoxy['v10'].str.replace('_', '.')

def savevento(filesaida, ventoxy):
    with open(filesaida, 'w') as saida:
        saida.write('time,wind10_speed,wind10_direction\n')
        for time, u, v in zip(ventoxy['time'], ventoxy['u10'], ventoxy['v10']):
            u, v = float(u), float(v)
            vetor = (u**2 + v**2)**(1/2)
            direcao = 180 + (180/3.14156)*np.arctan2(v, u)
            saida.write(f'{time},{vetor},{direcao}\n')


savevento(filesaida, ventoxy)

dfdir = pd.read_csv(filesaida)
print(dfdir['wind10_direction'].mean())
# Convert direction to radians
dfdir['wind10_direction_rad'] = np.radians(dfdir['wind10_direction'])

# Create wind rose plot
ax = wr.WindroseAxes.from_ax()
ax.bar(dfdir['wind10_direction'], dfdir['wind10_speed'], normed=True, opening=1, edgecolor='white')
ax.set_legend()
plt.show()




