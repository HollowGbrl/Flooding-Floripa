import xarray as xr
import pandas as pd

pasta = 'D:/Gabriel/finaltcc/batimetria'
file = 'bati_flripa_32722_corrigido_imbituba_delft_rio_campeche.xyz'


# Load CSV data into a DataFrame
df = pd.read_csv(f'{pasta}/{file}', sep=' ', header=None, names=['x', 'y', 'z'])

# Convert the DataFrame to an xarray Dataset
ds = xr.Dataset.from_dataframe(df)

print(ds['x'])

# Save to NetCDF
#ds.to_netcdf(f'{pasta}/NC_bathy.nc')