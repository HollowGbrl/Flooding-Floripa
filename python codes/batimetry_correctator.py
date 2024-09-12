arquivo_entrada = 'dados_glorys/batimetria/atlanticosul.xyz'
arquivo_saida= f'{arquivo_entrada}_32722.xyz'
import time
from pyproj import Transformer

print('Comecei')

# Define the input and output coordinate systems
input_crs = "EPSG:4326"  # WGS84
output_crs = "EPSG:32722"  # UTM Zone 22S

# Create a transformer for the coordinate conversion
transformer = Transformer.from_crs(input_crs, output_crs)
#abrindo os arquivos de entrada e saida
with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
    #para cada linha do arquivo, se o valor de batimetria for 0 (ou outro valor de interesse), ele vai excluir esse valor no novo arquivo
    for linha in entrada:
        #separando a linha 
        linha2=linha.split(' ')
        #criando variaveis para arredondar os numeros
        x, y, z =float(linha2[0]), float(linha2[1]), float(linha2[2])
        #variaveis arredondadas
        x, y=  transformer.transform(x, y)
        rx, ry, rz = round(x, 4), round(y, 4), round(-z, 2)
        #escrevendo as variaveis arredondadas no novo arquivo usando um fstring
        linhasaida= f'{rx} {ry} {rz}\n'
        saida.write(linhasaida)
print('terminei')