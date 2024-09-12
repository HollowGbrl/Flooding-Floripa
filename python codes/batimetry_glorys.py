import xarray as xr

arquivo = "dados_glorys/batimetria/cmems_mod_glo_phy_my_0.083deg_static_1720040775194.nc"


data = xr.open_dataset(arquivo)
with open('dados_glorys/batimetria/atlanticosul.xyz', 'w') as saida:
    
    for lat in data['latitude'].values[:]:
        for lon in data['longitude'].values[:]:
            ponto = data.sel(latitude=lat, longitude=lon, method='nearest') 
            z= float(ponto['deptho'].values)
            texto= f'{round(float(lat),4)} {round(float(lon),4)} {round(z,2)}\n'
            saida.write(texto)
    print('terminei tudo =)')
    