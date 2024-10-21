import plotly.express as px
import pandas as pd
import xarray as xr
import netCDF4
import numpy as np
import os

#caminho do diretorio
caminho_pasta= "D:/Gabriel/finaltcc/Vento-ccmp-2019-2020"
#lista dos arquivos do diretorio
lista_arquivos = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]
#dataframe vazio
data = {
    'tempo': [0],
    'u': [0],
    'v': [0],
    'ws': [0]
}

# Criando o DataFrame
df1 = pd.DataFrame(data)

for nome_arquivo in lista_arquivos:
    #vai chamar o arquivo como "arquivo"
    print(f'estou trabalhando no {nome_arquivo} =)')
    arquivo = os.path.join(caminho_pasta, nome_arquivo)

    netcdf_file = arquivo

    conteudo = xr.open_dataset(netcdf_file)

#escolher o ponto (lat lon)
    ponto = conteudo.sel(latitude=-27.625, longitude=-48.325, method='nearest') 
    u,v, ws, tempo =ponto['uwnd'][:], ponto['vwnd'][:], ponto['ws'][:], ponto['time'][:]
    #passando os dados do ponto pro dataframe 
    df2 = pd.DataFrame({
    'tempo': tempo,
    'u': u,
    'v': v,
    'ws': ws,
})
    df2['tempo'] = pd.to_datetime(df2['tempo'], unit='h')
    df1 = pd.concat([df1, df2], ignore_index=True)
    #salvando o arquivo
df1.to_csv('D:/Gabriel/finaltcc/vento-processado-2019-2020/serie_vento.csv')

print('terminei tudo =)')
