#importando os arquivos xyz e criando um arquivo novo de saida, com o proposito de diminuir o arquivo gigantesco de 62gibas
arquivo_entrada = 'dados das bordas.txt'
arquivo_saida= 'regioes_mare_borda.txt'
import time
import math

#criando uma função usada para converter.
def utm_to_wgs84(x, y):
    # Constants for UTM zone 22S (WGS 84)
    λ0 = math.radians(-51)
    k0 = 0.9996
    E0 = 500000
    N0 = 10000000
    a = 6378137  # Semi-major axis of WGS 84 ellipsoid

    # Convert UTM coordinates to latitude and longitude
    E = x - E0
    N = y - N0
    φ = N / (k0 * a)
    λ = λ0 + E / (k0 * a * math.cos(φ))

    # Convert radians to degrees
    φ_degrees = math.degrees(φ)
    λ_degrees = math.degrees(λ)

    return φ_degrees, λ_degrees






print('Comecei')

#abrindo os arquivos de entrada e saida sendo "r para read" e "w para write"
with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
    #para cada linha é separado entre ',' no arquivo
    for linha in entrada:
        linha2=linha.split(', ')

        #criando variaveis para os valores das linhas, float é para mostrar que podem ser numeros não inteiros
        x, y, z =linha2[0], float(linha2[1]), float(linha2[2])
       
        #transformando o dataset
        rx = x 
        ry, rz = utm_to_wgs84(y, z)

        print(f'y:{y}, ry:{ry} -------- z: {z}, rz={rz}')

        #escrevendo as variaveis novas no novo arquivo usando um fstring
        linhasaida= f'{rx}: {ry}, {rz}\n'
        saida.write(linhasaida)

print(f'Terminei em {time.process_time()}s')
