#importando os arquivos xyz e criando um arquivo novo de saida, com o proposito de diminuir o arquivo gigantesco de 62gibas
#escrevaaqui o local
local= 'ostras'
pasta= 'BASE'

dado_modelo = f'{pasta}/maregrafo{local}.csv'
dado_modelo = f'{pasta}/adcp.csv'
dado_processado = f'{pasta}/maregrafo{local}_processado.csv'
dado_processado = f'{pasta}/adcp_processado.csv'
import time
c=0
print('Comecei')

#abrindo os arquivos de entrada e saida
with open(dado_modelo, 'r') as modelo, open(dado_processado, 'w') as proces :
    proces.write('data,nivel\n')
    #para cada linha do arquivo, vou arrumar valores de data, hora e maré
    for linha in modelo:
        if c>0:
            linha2=linha.split(' ')
        #arrumando hora, excluindo o valor de segundos que não era usado.
            hm_sep = linha2[1].split(',')
            tempo = hm_sep[0].split(':')
            tempopronto= f'{tempo[0]}:{tempo[1]}'
        #arrumando valores de maré
            marepronta= hm_sep[1].replace('_', '.')
        #escrevendo os dados processados em um novo arquivo:
            proces.write(f'{linha2[0]} {tempopronto},{marepronta}')
        c+=1
print('Terminei')

