import xarray as xr
import time

file = '../finaltcc/delft/52_astro_imbi.dsproj_data/FlowFM/input/grid_compl_casan_juntando_8_topo_alti_net.nc'


conteudo = xr.open_dataset(file)


with open('pontosgrade.csv', 'w') as saida:
    saida.write('lon,lat,z\n')
    for i in range(0, len(conteudo['mesh2d_node_x'])):
        lon, lat, z= conteudo['mesh2d_node_x'][i].values, conteudo['mesh2d_node_y'][i].values, conteudo['mesh2d_node_z'][i].values
        lon, lat, z = round(float(lon), 4), round(float(lat), 4), round(float(z), 2)
        saida.write(f'{lon},{lat},{z}\n')
        
        
