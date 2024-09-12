import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
import utide
from utide import solve
import os

local = 'adcp_ponte'
#local='ostras'
pasta= 'BASE'
lat= -27.624

if local == 'norte':
    lat = -27.4909
elif local == 'ostras':
    lat = -27.72
elif local == 'ponte':
    lat = -27.5221


start_date = '2020-01-01'
end_date = '2020-12-31'

# Create a folder with the name "pasta" in the directory
os.makedirs(f'../imagens/{pasta}', exist_ok=True)

# Carregar os dados do arquivo CSV

if local == 'adcp_ponte':
    nome_arquivo_final = f'calibracao_adcp'
    #df_base = pd.read_csv(f'casananointeiro/adcp.csv')
    df_modelo = pd.read_csv(f'{pasta}/adcp_processado.csv')
else:
    nome_arquivo_final = f'validação_maregrafo{local}'
    #df_base = pd.read_csv(f'casananointeiro/maregrafo{local}_medido.csv')
    df_modelo = pd.read_csv(f'{pasta}/maregrafo{local}_processado.csv')

#ajustando as datas 
df_modelo['data'] = pd.to_datetime(df_modelo['data'])

df_modelo['nivel'] = df_modelo['nivel'] - df_modelo['nivel'].mean()
#df_modelo['ref'] = 0.9

def basegraph():
    coef_mod = solve(df_modelo['data'], 
            df_modelo['nivel'], 
            lat=lat)
    b=0
    #salvar os coeficientes em um arquivo txt
    with open(f'{pasta}/{nome_arquivo_final}_harmonic.csv', 'w') as saida:
        saida.write('constituintesmodeladas,amplitude\n')
        for a in coef_mod['A']:
            saida.write(f'{coef_mod["name"][b]},{a}\n')
            b+=1
    #recostruir a maré com base em consituintes encontrado no coef
    tide_tt = utide.reconstruct(df_modelo['data'], coef_mod)

    #Subtração da meré medido pela astronomica para obter a maré meteorologica
    tide_meteo = df_modelo['nivel'] - tide_tt['h']
    tide_tt['h'] = tide_tt['h'] - tide_tt['h'].mean()

    #chamando a função testes
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10)) # Create a subplot with 2 rows and 1 column

    # Plot the first subplot')
    ax1.plot(df_modelo['data'], tide_tt['h'], label='Astronomico')
    ax1.plot(df_modelo['data'], tide_meteo, label='Residuo Meteorologico')
    ax1.set_ylabel('Nível (m)')
    ax1.legend()
    ax1.grid(True)
    ax1.set_ylim(-1, 1.5)
    ax1.set_title(f'\n Local: {local} \n Variação de nível após analise harmonica')
    ax1.set_xticks(pd.date_range(start_date, end_date, freq='3000D'))
    # Plot the second subplot

    ax2.plot(df_modelo['data'], df_modelo['nivel'], label='Dado bruto')
    #ax2.plot(df_modelo['data'], df_modelo['ref'], label='Nível de referência')
    ax2.legend()
    ax2.set_xlabel('Tempo')
    ax2.set_ylabel('Nivel(m)')
    ax2.set_title(f'Variação de nível (dado bruto)')
    ax2.grid(True)
    ax2.set_ylim(-1, 1.5)
    ax2.set_xticks(pd.date_range(start_date, end_date, freq='30D'))
    plt.tight_layout() # Adjust the spacing between subplots
    plt.savefig(f'../imagens/{pasta}/{nome_arquivo_final}_subplot.png')
    plt.show()


basegraph()
