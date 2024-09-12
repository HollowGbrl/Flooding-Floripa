import plotly.express as px
import pandas as pd
import xarray as xr
import netCDF4
import numpy as np
import os


#caminho do diretorio que vai trabar
caminho_pasta= "D:/Gabriel/finaltcc/Vento-ccmp-2019-2020"
#codigo que vai fazer ele criar uma lista dos arquivos do diretorio
lista_arquivos = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]


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

###escolhi lat= -27.625 lon= -47.375
    ponto = conteudo.sel(latitude=-27.625, longitude=-48.325, method='nearest') 
    u,v, ws, tempo =ponto['uwnd'][:], ponto['vwnd'][:], ponto['ws'][:], ponto['time'][:]
    df2 = pd.DataFrame({
    'tempo': tempo,
    'u': u,
    'v': v,
    'ws': ws,
})
    print(df2['tempo'][:])
    df2['tempo'] = pd.to_datetime(df2['tempo'], unit='h')
    print(df2['tempo'][:])
    print('-'*34)
    df1 = pd.concat([df1, df2], ignore_index=True)
df1.to_csv('D:/Gabriel/finaltcc/vento-processado-2019-2020/serie_vento.csv')

print('terminei tudo =)')
#u_mil= np.arcsin(u/(((u**2)+(v**2))**(1/2)))
#u_mil_graus= 90 - u_mil*(180/3.14156)

#vento_u.to_csv('vento_u.csv', index=True)

#print(conteudo['latitude'])
#
#lat_nova=[]
#lon_nova=[]
#for lat in conteudo['latitude'][:]:
#    for lon in conteudo['longitude'][:]:
#       lat_nova.append(lat)
#       lon_nova.append(lon)
##
### Crie um DataFrame com suas coordenadas (latitude e longitude)
#data = {'Latitude': lat_nova, 'Longitude': lon_nova}
#df = pd.DataFrame(data)
##
###Crie o mapa
#fig = px.scatter_geo(df, lat='Latitude', lon='Longitude')
##
### Exiba o mapa
#fig.show()
##