#A code to transform a netcdf file containing elevation latitude and longitude to a xyz file.
import xarray as  xr

file = 'GEBCO_09_Apr_2024_0815e339f916/gebco_2023_n-27.6828_s-27.8654_w-48.5719_e-48.4071.nc'

ds = xr.open_dataset(file)

with open('newbatimetry_wgs84.xyz', 'w') as saida:
    for latitude in ds['lat'].values:
        for longitude in ds['lon'].values:
            elev = ds['elevation'].sel(lat=latitude, lon=longitude).values
            linhanova= f'{latitude} {longitude} {elev}\n'
            saida.write(linhanova)

