import time
import numpy as np

arquivo= "d:/Gabriel/finaltcc/vento-processado-2019-2020/serie_vento.csv" 

print('comecei')
with open(arquivo, 'r') as entrada, open(f'{arquivo}_processado.csv', 'w') as saida:
    saida.write('tempo,u,v,direcao,ws\n')
    for linha in entrada:
        linha2=linha.split(',')
        
        #ajustando data
        tempohora= linha2[1].split(' ')
        tempo= tempohora[0].split('-')
        tempo_certo= f'{int(tempo[0])+17}-{tempo[1]}-{tempo[2]} {tempohora[1]}'

        #ajustando o vetor
        u, v= float(linha2[2]), float(linha2[3])

        vetor= u/(((u**2)+(v**2))**(1/2))
        rad= np.arcsin(vetor)
        vetor_graus= rad*(180/3.14156)
        vetor_graus2= - vetor_graus
        if u>0 or v>0:
            vetor_graus2= 180+ vetor_graus
        if v>0 and u<0:
            vetor_graus2= 180+ vetor_graus
        if u>0 and v<0:
            vetor_graus2= 360- vetor_graus
        content= f'{tempo_certo},{linha2[2]},{linha2[3]},{vetor_graus2},{linha2[4]}'
        saida.write(content)
print('terminei')



#vento_u.to_csv('vento_u.csv', index=True)

#print(conteudo['latitude'])
#
#lat_nova=[]
#lon_nova=[]
#for lat in conteudo['latitude'][:]:
#    for lon in conteudo['longitude'][:]:
#       lat_nova.append(lat)
#       lon_nova.append(lon)
##
### Crie um DataFrame com suas coordenadas (latitude e longitude)
#data = {'Latitude': lat_nova, 'Longitude': lon_nova}
#df = pd.DataFrame(data)
##
###Crie o mapa
#fig = px.scatter_geo(df, lat='Latitude', lon='Longitude')
##
### Exiba o mapa
#fig.show()
##