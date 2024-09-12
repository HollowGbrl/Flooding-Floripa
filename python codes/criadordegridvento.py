import xarray as xr
import time
import folium
import pandas as pd

#definição do arquivo de entrada, aqui pode ser inserido um codigo para baixar o arquivo do era
netcdf_file = 'd:/Gabriel/finaltcc/vento_era5_hora_2020/adaptor.mars.internal-1725379068.4670866-15320-9-10b4d5a0-b0c2-4d30-a3f6-d67d06e5f80c.nc'
conteudo = xr.open_dataset(netcdf_file)

#edite as variaveis abaixo para definir a região de interesse
lat_min = -26.75
lat_max = -28.35
lon_max = -46.5
lon_min = -48.5

arquivo_x = '../finaltcc/vento_era5_hora_2020/windy.amu'
arquivo_y = '../finaltcc/vento_era5_hora_2020/windy.amv'

data = 'hours since 2020-01-01 00:00:00 +00:00'

conteudo = conteudo.sel(latitude=slice(lat_min, lat_max), longitude=slice(lon_min, lon_max))


n_cols = f'{conteudo.sizes["longitude"]}'
n_rows = f'{conteudo.sizes["latitude"]}'
x_llcenter = 737151.19 #lat do ponto mais ao sul da região de interesse
y_llcenter = 6836292.3 #lon do ponto mais ao oeste da região de interesse
dx = 25000              ##resolução do grid de vento no eixo x em metros, no caso 25km, baseado nos dados do era5 de 0.25 graus
dy = 25000              ##resolução do grid de vento no eixo y em metros, no caso 25km, baseado nos dados do era5 de 0.25 graus

#definição do header dos arquivos de saida para funcionar no delft (é bem chato n pode mudar mto e se tirar os comentarios ele não aceita o arquivo)
header1 = f'### START OF HEADER\n### This file is created by Deltares\n### Additional commments\nFileVersion\t=\t1.03\nfiletype\t=\tmeteo_on_equidistant_grid\nNODATA_value\t=\t-9999.0\nn_cols\t=\t{n_cols}\nn_rows\t=\t{n_rows}\ngrid_unit\t=\tm\nx_llcenter\t=\t{x_llcenter}\ny_llcenter\t=\t{y_llcenter}\ndx\t=\t{dx}\ndy\t=\t{dy}\nn_quantity\t=\t1\nquantity1\t=\tx_wind\nunit1\t=\tm s-1\n### END OF HEADER\n'
header2 = f'### START OF HEADER\n### This file is created by Deltares\n### Additional commments\nFileVersion\t=\t1.03\nfiletype\t=\tmeteo_on_equidistant_grid\nNODATA_value\t=\t-9999.0\nn_cols\t=\t{n_cols}\nn_rows\t=\t{n_rows}\ngrid_unit\t=\tm\nx_llcenter\t=\t{x_llcenter}\ny_llcenter\t=\t{y_llcenter}\ndx\t=\t{dx}\ndy\t=\t{dy}\nn_quantity\t=\t1\nquantity1\t=\ty_wind\nunit1\t=\tm s-1\n### END OF HEADER\n'

#função que cria os aquivos de saida x e v, um codigo só pros dois.

def verpontos(conteudo):
    with open ('pontosvento.csv', 'w') as liltxt:
        liltxt.write('lat,lon\n')
        for lat in conteudo['latitude'].values:
            for lon in conteudo['longitude'][:].values:
                liltxt.write(f'{lat},{lon}\n')
    data = pd.read_csv('pontosvento.csv', delimiter=',')
    # Create a map object
    m = folium.Map(location=[data['lat'].mean(), data['lon'].mean()], zoom_start=10)
    # Add markers for each point
    for index, row in data.iterrows():
        folium.Marker([row['lat'], row['lon']]).add_to(m)
    m.save('mapa_pontosvento.html')

def cria_arquivo(conteudo, data, header1, header2):
    contador=0
    with open(arquivo_x, 'w') as saidax, open(arquivo_y, 'w') as saiday:
        saidax.write(header1)
        saiday.write(header2)
        for tempo in conteudo['time'][:]:
            saidax.write(f'TIME = {contador} {data}\n')
            saiday.write(f'TIME = {contador} {data}\n')
            for lat in conteudo['latitude'][:]:
                for lon in conteudo['longitude'][:]:
                    ponto = conteudo.sel(latitude=lat, longitude=lon, method='nearest')
                    u = ponto['u10'].isel(time=contador).values
                    v = ponto['v10'].isel(time=contador).values
                    #aqui eu arredondo os valores, mas se houver grande certeza do dado e pouca preocupação com armazenamento não é necessario arredondar.
                    saidax.write(f'{round(float(u), 1)}\t')
                    saiday.write(f'{round(float(v), 1)}\t')
                saidax.write('\n')
                saiday.write('\n')
            #aqui pode ser alterado a resolução do eixo tempo, nesse caso o dado era de hora em hora, por isso de 1 em 1.
            contador+=1
    #print('terminei tudo =)', time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))


#descomente as funções que necessita

#cria_arquivo(conteudo, data, header1, header2)
verpontos(conteudo)
