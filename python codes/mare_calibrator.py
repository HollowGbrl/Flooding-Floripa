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



start_date = '2020-03-18'
end_date = '2020-04-08'

# Create a folder with the name "pasta" in the directory
os.makedirs(f'../imagens/{pasta}', exist_ok=True)

# Carregar os dados do arquivo CSV

if local == 'adcp_ponte':
    nome_arquivo_final = f'calibracao_adcp'
    df_medido = pd.read_csv(f'casananointeiro/adcp.csv')
    df_modelo = pd.read_csv(f'{pasta}/adcp_processado.csv')
else:
    nome_arquivo_final = f'validação_maregrafo{local}'
    df_medido = pd.read_csv(f'casananointeiro/maregrafo{local}_medido.csv')
    df_modelo = pd.read_csv(f'{pasta}/maregrafo{local}_processado.csv')

#ajustando as datas 
df_medido['data'] = pd.to_datetime(df_medido['data'])
df_modelo['data'] = pd.to_datetime(df_modelo['data'])

df_modelo2= df_modelo.copy()
df_modelo2['nivel'] = df_modelo2['nivel'] - df_modelo2['nivel'].mean()

df_modelo2 = df_modelo2[(df_modelo2['data'] >= start_date) & (df_modelo2['data'] <= end_date)]
df_medido = df_medido[(df_medido['data'] >= start_date) & (df_medido['data'] <= end_date)]

common_dates = pd.merge(df_modelo2, df_medido, on='data')
print(len(common_dates))


#função para calcular o rmse, r2 e correlação
def testes(dataframe, arg1):
    soma=0
    mae=0
    n= len(dataframe)
    x = dataframe['nivel_x']
    y = dataframe['nivel_y']
    quad = (x - y) ** 2
    rss= quad.sum()
    quad2= (y - x.mean()) ** 2
    tss= quad2.sum()
    
    if 'rmse' in arg1:
        rmse= (rss/n)**(1/2)
        print('rmse', rmse)
    if 'correlation' in arg1:
        correlation = np.corrcoef(x, y)[0, 1]
        print('correlation', correlation)
    if 'r2' in arg1:
        r2= 1 - (rss/tss)
        print('r2', r2)
    if 'mae' in arg1:
        mae = (abs(x-y)).sum()/n
        print('mae', mae)
    return rmse, correlation, mae
#função para gerar o grafico e calcular a maré meteorologica em comparação, assim como suas componentes
def graph():
    # executar a análise harmonica de marés com utide.solve()
    coef_mod = solve(common_dates['data'], 
            common_dates['nivel_x'], 
            lat=lat)
    coef_med = solve(common_dates['data'], 
            common_dates['nivel_y'], 
            lat=lat)
    b=0
    #salvar os coeficientes em um arquivo txt
    with open(f'{pasta}/{nome_arquivo_final}_harmonic.csv', 'w') as saida:
        saida.write('constituintesmodeladas,amplitude\n')
        for a in coef_mod['A']:
            saida.write(f'{coef_mod["name"][b]},{a}\n')
            b+=1
    #recostruir a maré com base em consituintes encontrado no coef
    tide_tt = utide.reconstruct(common_dates['data'], coef_mod)
    tide_tt2 = utide.reconstruct(common_dates['data'], coef_med)
    
    #Subtração da meré medido pela astronomica para obter a maré meteorologica
    tide_meteo = common_dates['nivel_x'] - tide_tt['h']
    tide_tt['h'] = tide_tt['h'] - tide_tt['h'].mean()
    tide_tt2['h'] = tide_tt2['h'] - tide_tt2['h'].mean()
    x = pd.DataFrame({'nivel_x': tide_tt['h']})
    y = pd.DataFrame({'nivel_y': tide_tt2['h']})
    juntos = pd.concat([x, y], axis=1)

    #chamando a função testes
    rmse, correlation, mae = testes(juntos, ['rmse','correlation', 'mae'])
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6)) # Create a subplot with 2 rows and 1 column

    # Plot the first subplot
    ax1.plot(common_dates['data'], tide_tt2['h'], label='ADCP (Maré Astro)')
    ax1.plot(common_dates['data'], tide_tt['h'], label='Modelo (Maré Astro)')
    ax1.set_ylabel('Nível (m)')
    ax1.legend()
    ax1.grid(True)
    ax1.set_ylim(-1, 1.5)
    ax1.set_title(f'\n Local: Maregrafo Sul \n Comparação Astronomica entre Observado e Modelado \n  (Correlação= {round(correlation,2)}- rmse= {round(rmse,2)} m, mae= {round(mae,2)} m)')
    ax1.set_xticks(pd.date_range(start_date, end_date, freq='3D'))
    rmse, correlation, mae = testes(common_dates, ['rmse','correlation', 'mae'])

    # Plot the second subplot
    ax2.plot(common_dates['data'], common_dates['nivel_y'], label='ADCP (dado bruto)')
    ax2.plot(common_dates['data'], common_dates['nivel_x'], label='Modelo (dado bruto)')
    ax2.legend()
    ax2.set_xlabel('Tempo')
    ax2.set_ylabel('Nivel(m)')
    ax2.set_title(f'Comparação dado bruto entre Modelado e Medido \n (Correlação= {round(correlation,2)}, rmse= {round(rmse,2)} m, mae= {round(mae,2)} m)')
    ax2.grid(True)
    ax2.set_ylim(-1, 1.5)
    ax2.set_xticks(pd.date_range(start_date, end_date, freq='3D'))
    plt.tight_layout() # Adjust the spacing between subplots
    plt.savefig(f'../imagens/{pasta}/{nome_arquivo_final}_subplot.pdf')
    plt.show()

def basegraph():
    coef_mod = solve(df_modelo2['data'], 
            df_modelo2['nivel'], 
            lat=lat)
    b=0
    #salvar os coeficientes em um arquivo txt
    with open(f'{pasta}/{nome_arquivo_final}_harmonic.csv', 'w') as saida:
        saida.write('constituintesmodeladas,amplitude\n')
        for a in coef_mod['A']:
            saida.write(f'{coef_mod["name"][b]},{a}\n')
            b+=1
    #recostruir a maré com base em consituintes encontrado no coef
    tide_tt = utide.reconstruct(df_modelo2['data'], coef_mod)

    #Subtração da meré medido pela astronomica para obter a maré meteorologica
    tide_meteo = df_modelo2['nivel'] - tide_tt['h']
    tide_tt['h'] = tide_tt['h'] - tide_tt['h'].mean()

    #chamando a função testes
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6)) # Create a subplot with 2 rows and 1 column

    # Plot the first subplot')
    ax1.plot(common_dates['data'], tide_tt['h'], label='Modelo (Maré Astro)')
    ax1.set_ylabel('Nível (m)')
    ax1.legend()
    ax1.grid(True)
    ax1.set_ylim(-1, 1.5)
    ax1.set_title(f'\n Local: {local} \n Variação de nível após analise harmonica')
    ax1.set_xticks(pd.date_range(start_date, end_date, freq='3D'))
    # Plot the second subplot
    ax2.plot(common_dates['data'], common_dates['nivel_x'], label='Modelo (dado bruto)')
    ax2.legend()
    ax2.set_xlabel('Tempo')
    ax2.set_ylabel('Nivel(m)')
    ax2.set_title(f'Variação de nível (dado bruto)')
    ax2.grid(True)
    ax2.set_ylim(-1, 1.5)
    ax2.set_xticks(pd.date_range(start_date, end_date, freq='3D'))
    plt.tight_layout() # Adjust the spacing between subplots
    plt.savefig(f'../imagens/{pasta}/{nome_arquivo_final}_subplot.pdf')
    plt.show()


basegraph()
