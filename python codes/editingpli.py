import os
import time
import pandas as pd
from pyproj import Transformer

saida1, saida2= 'edit2_Boundary02.pli', 'edit2_Waterlevel.bc'
entrada1, entrada2 = 'edit_Boundary02.pli', 'edit_Waterlevel.bc'

input_crs = "EPSG:4326" 
output_crs = "EPSG:32722"  
transformer = Transformer.from_crs(input_crs, output_crs)

with open(saida1, 'w') as spli, open(entrada1, 'r') as epli, open(entrada2, 'r') as ebc, open(saida2, 'w') as sbc:
        
    files = os.listdir('D:/Gabriel/AUXILIO_AO_DELFT/dados_glorys/processamento')
    text1=''
    cont1=0 
    for file in files:
        splits = file.split('_')
        lat= splits[2]
        exclude = splits[3].replace('.txt', '')
        lon = exclude
        nlon, nlat= transformer.transform(lat, lon)

        lenlat, lenlon = len(str(nlat).split('.')[0]), len(str(nlon).split('.')[0])

        nlat2, nlon2 = nlat/(10**(lenlat-1)), nlon/(10**(lenlon-1))

        cont2=cont1+1
        if cont2<10:
            cont2 = f'0{cont2}'
        
        text1 += f'{nlon2}E+00{lenlon-1}  {nlat2}E+00{lenlat-1} Boundary02_00{cont2}\n'
        cont1+=1
    spli.write(f'Boundary02\n    2    {cont1}\n{text1}')

        
    
        


    

