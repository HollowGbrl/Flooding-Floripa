import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

pasta = 'BASE'
caminho = f"../finaltcc/resultados/{pasta}/"

for arquivo in os.listdir(caminho):
    if 'harmonic' in arquivo:
        data= f'{caminho+arquivo}'
        break

modelastroborda = {
    'M2': 0.2420286608549507,
    'S2': 0.22609215529419968,
    'O1': 0.10780469736022151,
    'M4': 0.09369806785547892,
    'K1': 0.052112361052675235,
    'MS4': 0.039410283697408885,
    'S4': 0.01168876993484956,
    '2MK5': 0.004738443942393602,
    '2MS6': 0.004293138082357504,
    '2SM6': 0.004242321429797424,
    'MSF': 0.00418254964233984,
    'SK3': 0.0037674594504293257,
    'M8': 0.001444662497459658,
    'M3': 0.0012870977670122624,
    'M6': 0.0011555929278537554
}

data_adcp = {
    'M2': 0.2843227395425406,
    'S2': 0.24416045407244713,
    'MSF': 0.14833290500866936,
    'O1': 0.11703874228643911,
    'M4': 0.0524037039269533,
    'MS4': 0.045873068177398106,
    'K1': 0.03729202216553385,
    'M3': 0.034666052768847246,
    'S4': 0.02722863731544743,
    'SK3': 0.026197018887142095,
    '2MS6': 0.009902528327803747,
    '2SK5': 0.005474065385880956,
    '2SM6': 0.004705490288485512,
    '3MK7': 0.0015719488681065392,
    'M6': 0.0012999168478437925,
}

data_modelo = {}
with open(data, 'r') as data:
    for line in data:
        line2= line.split(',')
        if 'amplitude' in line:
            continue
        else:
            data_modelo.update({line2[0]: float(line2[1])})

df = pd.DataFrame({'Modelo': data_modelo})
df = df[:17]

# Create a figure to plot the harmonics

plt.figure(figsize=(10, 6))



# Plot the harmonics
ax = df.plot(kind='bar', ax=plt.gca(), color=['cornflowerblue', 'darkorange'])

# Rotate x-axis labels
# Rotate x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.title('Amplitude dos principais harmônicos')
plt.ylabel('Amplitude (m)')
plt.xlabel('Harmônicos')
plt.ylim(0, 0.25)
y_ticks = np.arange(0, 0.26, 0.025)

# Set the y-axis ticks
plt.yticks(y_ticks)

# Save the figure
plt.savefig(f'../finaltcc/imagens/{pasta}/multiplot_harmonicos_{pasta}.pdf')

# Show the figure
plt.show()

