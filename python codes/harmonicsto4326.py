from pyproj import Transformer
import time
arquivo = 'd:/Gabriel/finaltcc/harmonicos/novabordagrande/bordas.txt'

# Define the source and target coordinate systems


input_crs = "EPSG:32722" # WGS84
output_crs = "EPSG:4326"  # UTM Zone 22S

# Create a transformer for the coordinate conversion
transformer = Transformer.from_crs(input_crs, output_crs)

# Create the transformer



with open(arquivo, 'r') as entrada, open(f'{arquivo}_4326.txt', 'w') as saida:
    saida.write('ponto lon lat\n')
    for linha in entrada:
        linha2= linha.split('\t')
        
        lon, lat, nome = linha2[0], linha2[1], linha2[2].split('\n')[0]
        
        latc = lat.split('E+')
        latd= (float(latc[0]))*(10**int(latc[1]))
        lonc= lon.split('E+')
        lond= (float(lonc[0]))*(10**int(lonc[1]))
        

        nlon, nlat= transformer.transform(lond, latd)

        linhasaida = f'{nome} {nlat} {nlon}\n'
        saida.write(linhasaida)