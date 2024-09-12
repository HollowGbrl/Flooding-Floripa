import wget
import pandas as pd
import xarray as xr
import time
import netCDF4 as nc
import os

start_range, end_range = '06-01-2020', '31-12-2020'
pasta_dados = 'D:/Gabriel/AUXILIO_AO_DELFT/dados_hycom/'


latmin, latmax, lonmin, lonmax = -29, -27, -49, -46

# Função para checar se a variável é menor que 10 e adicionar um zero a esquerda (necessario ao site do hycom)
def check_var(var):
    if var < 10:
        return '0' + str(var)
    else:
        return str(var)

df = pd.date_range(start=start_range, end=end_range)
latlons=[]
c=0 

with open ('dados_hycom/2020.txt', 'w') as saida:
    saida.write('yyyy-m-d hh:mm\nlat, lon, ssh, ubaro, vbaro\n')
    for data in df:
        d2= check_var(data.day)
        m2= check_var(data.month)
        y2= check_var(data.year)
        for h in range(0, 24, 3):
            h2 = check_var(h)
            #file= f'hycom_glby_930_{y2}{m2}{d2}12_t0{h2}_ssh.nc'
            #file2= f'hycom_glby_930_{y2}{m2}{d2}12_t0{h2}_uv3z.nc'
            file = f'hycom_GLBy0.08_930_{y2}{m2}{d2}12_t0{h2}_sur.nc'
            url = f'https://data.hycom.org/datasets/GLBy0.08/expt_93.0/data/hindcasts/2020/{file}'
            
            cont=1
            while file not in os.listdir(pasta_dados) or cont < 25:
                print('tentativa:', cont)
                try:
                    wget.download(url, out=f'{pasta_dados}{file}')
                except:
                    print(f'Arquivo {file} não encontrado')
                continue
                cont+=1
            
            #xarray = xr.open_dataset(f'{pasta_dados}{file}')
            arquivo = nc.Dataset(f'{pasta_dados}{file}')
            if c == 0:
                for lat in arquivo['lat']:
                    if lat <= latmax and lat >= latmin:
                        for lon in arquivo['lon']:
                            if lon >= 180+ lonmin and lon <= 180+ lonmax:
                                latlons.append((lat, lon))
                c=1
            
            saida.write(f'{y2}-{m2}-{d2} {h2}:00\n')

            for lat, lon in latlons:
                SSH= arquivo['ssh'][:, lat, lon]
                UBARO= arquivo['u_barotropic_velocity'][:, lat, lon]
                VBARO= arquivo['v_barotropic_velocity'][:, lat, lon]
    
                result= f'{round(float(lat), 4)}, {round(float(lon), 4)}, {round(SSH[0], 3)}, {round(UBARO[0], 3)}, {round(VBARO[0], 3)}'

                saida.write(f'{result}\n')

            arquivo.close()
            os.remove(f'{pasta_dados}{file}')
