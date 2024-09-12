import xarray as xr
import os
import time


caminho_pasta= 'd:/CCMP'

lista_arquivos = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]
print('comecei')
for nome_arquivo in lista_arquivos:
    arquivo = os.path.join(caminho_pasta, nome_arquivo)

# Open the netCDF file
    dados = xr.open_dataset(f'{arquivo}')

# Definindo os limites de latitude e longitude para recorte
    lat_bnds = [-49, -46]
    lon_bnds = [-25, -29]
# Fazendo o recorte usando os limites de latitude e longitude
    dados_recortados = dados.sel(latitude=slice(lat_bnds[0], lat_bnds[1]), 
                             longitude=slice(lon_bnds[0], lon_bnds[1]))
# Salvar o recorte em um novo arquivo NetCDF, se desejar
    dados_recortados.to_netcdf(f'../CCMP2/{nome_arquivo}_v2.nc')
    
    
    print(f'fiz arquivo: {nome_arquivo}')


    



