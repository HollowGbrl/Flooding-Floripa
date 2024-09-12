import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
import os
import utide


# Carregar os dados do arquivo CSV em pandas

harmonicos = 'd:/Gabriel/finaltcc/harmonicos/new_bounds_gabe\Boundary01_0002.txt'
s_harmonicos = 'speedharmonics.txt'

x=0
df = pd.read_csv(harmonicos)
dfs= pd.read_csv(s_harmonicos, sep='\t')

print()

def onda(t):
    x=0
    for harmonico in df['hc_list']:
        speed = dfs.loc[dfs['Name'] == harmonico, 'Speed'].values[0]
        r = ((speed)/360)

        a = df.loc[df['hc_list'] == harmonico, 'amplitudes'].values[0]
        p = df.loc[df['hc_list'] == harmonico, 'phases'].values[0]
        x+=  a*(np.cos)((r*t) + p)
    return x

dfplot = pd.DataFrame(columns=['t', 'onda'])

for t in range(0, 5000, 20):
    dfplot = pd.concat([dfplot, pd.DataFrame({'t': t, 'onda': onda(t)}, index=[0])], ignore_index=True)
    
plt.plot(dfplot['t'], dfplot['onda'])
plt.grid(True)
plt.show()



