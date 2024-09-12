import netCDF4 as nc

# Open the NetCDF file



def read_netcdf(file):
    
    dataset = nc.Dataset(file)
    print(dataset)
    return #print(arquivo)


read_netcdf('dados_glorys/batimetria/cmems_mod_glo_phy_my_0.083deg_static_1718030082527.nc')

