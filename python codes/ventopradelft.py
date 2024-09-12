import time
import numpy as np

arquivo= "d:/Gabriel/finaltcc/ventos_era5_horahora/adaptor.mars.internal-1711560871.222956-23483-16-a05b0dff-19b1-4260-85f6-724cf9269604.nc_processado.csv" 

print('comecei')
with open(arquivo, 'r') as entrada, open(f'../finaltcc/ventos_era5_horahora/windxdirydir.wnd', 'w') as saida:
    cont=0
    for linha in entrada: 
        linha2=linha.split(',')
        #ajustando o vetor
        x, y= float(linha2[2]), float(linha2[3])
        content= f'{float(cont)} {x} {y}\n'
        #content= f'{float(cont)} {y} {x}\n'
        saida.write(content)
        cont+=60
print('terminei')
