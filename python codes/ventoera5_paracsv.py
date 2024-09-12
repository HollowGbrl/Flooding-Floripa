import pandas as pd
import xarray as xr
import netCDF4
import numpy as np
import os



netcdf_file = 'd:/Gabriel/finaltcc/ventos_era5_horahora/adaptor.mars.internal-1711560871.222956-23483-16-a05b0dff-19b1-4260-85f6-724cf9269604.nc'

conteudo = xr.open_dataset(netcdf_file)
print(conteudo['latitude'])
###escolhi lat= -27.625 lon= -47.375
ponto = conteudo.sel(latitude=-27.625, longitude=-48.325, method='nearest') 
#print(ponto)
#u,v, tempo =ponto['u10'][:], ponto['v10'][:], ponto['time'][:]
#df2 = pd.DataFrame({
    #'tempo': tempo,
    #'u': u,
    #'v': v,
#})
#df2.to_csv(f'{netcdf_file}_processado.csv')
#print(df2)
#print('terminei tudo =)')