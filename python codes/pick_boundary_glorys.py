#codigo feito para gerar arquivos de timeseries a partir de dados de netcdf (no caso, dados de reanalise do GLORYS) para inserir ao modelo como pontos na borda.
#pode ser usado para extrair os pontos de um arquivo  .pli de borda do Delft3D
#o codigo atualmente suporta apenas um arquivo de boundary, com uma boundary por vez, e apenas um arquivo netcdf de dados
import xarray as xr 
import time
import pandas as pd
from pyproj import Transformer


#arquivo netcdf com todos os pontos, o arquivo deve conter as variaveis zos, uo e vos, e as dimensões latitude, longitude e time
file = 'dados_glorys/seasurfacegeoid_u_v/cmems_mod_glo_phy_my_0.083deg_P1D-m_1718996170742.nc'
#pasta para onde será salvo os arquivos processados
pasta = 'dados_glorys/processamento'
#pasta para onde será salvo os arquivos processados com nivel ajustado
save = 'dados_glorys/process0/'
#arquivo pli (boundary) com os pontos de interesse
arquivopli = '../finaltcc/delft/51_astroonly_1borda.dsproj_data/FlowFM/input/Boundary01.pli'
#projeção geografica dos pontos do arquivo pli
proj = 'EPSG:32722'



#função para ler o arquivo pli e extrair os pontos
def geralocais(arquivopli, projcord):
    transformer = Transformer.from_crs(projcord, 'EPSG:4326')
    with open(arquivopli, 'r') as pli:
        locais = []
        for line in pli:
            if len(line)>12:
                line2 = line.split(' ')
                lon, lat = line2[0], line2[2]
                name= line2[3].split('\n')[0]
                latc, lonc =float(lat.split('E+00')[0]), float(lon.split('E+00')[0])
                vallatc, vallonc = int(lat.split('E+00')[1]), int(lon.split('E+00')[1])
                flat, flon= latc*(10**vallatc), lonc*(10**vallonc)
                nlat, nlon = transformer.transform(lon, lat)
                locais.append((nlat, nlon, name))
    return  locais
#Função para ler o arquivo netcdf e extrair os dados
def netcdfprocess(file, locais, pasta):
    #criando varios arquivos time series para cada ponto da região de interesse
    for regiao in locais:
        lat_t, lon_t, name = regiao
        #selecionando o ponto mais proximo do ponto do arquivo
        print(f'comecei {name}: lat {lat_t} lon {lon_t}')
        arquivo= xr.open_dataset(file)
        arquivo = arquivo.sel(latitude=lat_t, longitude=lon_t, method='nearest')
        
        with open(f'{pasta}/timeseries_nivel_{name}_{round(lat_t, 2)}_{round(lon_t, 2)}.csv', 'w') as saida:
            saida.write('date,nivel,uo,vo\n')
            #criando a time series para o ponto
            for tempo in arquivo['time']:
                nivel = arquivo['zos'].sel(time=tempo).values
                uo= arquivo['uo'].sel(time=tempo, depth= 0.494025).values
                vo= arquivo['vo'].sel(time=tempo, depth= 0.494025).values
                tempo2= tempo.values
                tempo2= str(tempo2).split('T')[0]
                saida.write(f'{tempo2} 00:00,{nivel},{uo},{vo}\n')
    return print('terminei tudo')
#função para tirar a media (ajustar ao nivel 0)
def adjustzero(pasta, save):
    for file in os.listdir(pasta):
        df =pd.read_csv(f'{pasta}/{file}')
        df['nivel']= df['nivel'] - df['nivel'].mean()
        df.to_csv(f'{save}{file}', index=False)
    return print('ajustado o nivel zero')



#chamando as funções
locais = geralocais(arquivopli, proj)
#netcdfprocess(file, locais, pasta)
#adjustzero(pasta, save)
#gerando apenas um txt simples com os pontos usados
with open ('dados_glorys/locais.txt', 'w') as saida:
    saida.write('lat lon name\n')
    for local in locais:
        saida.write(f'{round(local[0], 2)} {round(local[1],2)} {local[2]}\n')

