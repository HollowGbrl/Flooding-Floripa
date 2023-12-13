#importando os arquivos xyz e criando um arquivo novo de saida, com o proposito de diminuir o arquivo gigantesco de 62gibas
arquivo_entrada = 'altimetria4_filtrados.xyz'
arquivo_saida= 'altimetria4_filt_round.xyz'
import time

print('Comecei')
#abrindo os arquivos de entrada e saida
with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
    #para cada linha do arquivo, se o valor de batimetria for 0 (ou outro valor de interesse), ele vai excluir esse valor no novo arquivo
    for linha in entrada:
        linha2=linha.split(' ')
        #aqui é ajustado o valor de não interesse no arquivo
        #if float(linha2[2]) <25 and float(linha2[2]) != 0:
            #saida.write(linha)
        
        #criando variaveis para arredondar os numeros
        x, y, z =float(linha2[0]), float(linha2[1]), float(linha2[2])
        #variaveis arredondadas
        rx, ry, rz = round(x, 1), round(y, 1), round(z, 2)
        
        #escrevendo as variaveis arredondadas no novo arquivo usando um fstring
        linhasaida= f'{rx} {ry} {rz}\n'
        saida.write(linhasaida)

print('Terminei')
