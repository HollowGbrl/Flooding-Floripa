import geopandas as gpd
import matplotlib.pyplot as plt
from geobr import read_state
from geobr import read_municipality
from geobr import lookup_muni
estado= 'Santa Catarina'
cidade= 'Florianopolis'

def getstates():
    # Download the shapefile for all states in Brazil
    brazil_states = read_state(year=2020)
    return brazil_states
def getcity(estado, cidade):
    code= lookup_muni(cidade)
    fixcode= code['code_state'].iloc[0]
    brazil_cities = read_municipality(code_muni=fixcode, year=2020)
    return brazil_cities

def mapcreate(geral, local):
    
    # Plot the data
    fig, ax = plt.subplots()
    geral.plot(ax=ax, color='lightgrey')
    if local == cidade:
        code= lookup_muni(local)
        fixcode= code['code_muni'].iloc[0]
        mapcity = geral[geral['code_muni'] == fixcode]
        mapcity.plot(ax=ax, color='blue')
        plt.xlim(-54,-48)
    # Filter for Santa Catarina
    elif local == estado:
        mapstate = geral[geral['name_state'] == local]
        mapstate.plot(ax=ax, color='red')
        plt.xlim(-74,-32)
    plt.show()

def mapcreatecity(geral, local):
    code= lookup_muni(local)
    fixcode= code['code_muni'].iloc[0]
    mapcity = geral[geral['code_muni'] == fixcode]
    mapcity.plot(color='blue')
    plt.show()

mapcreatecity(getcity(estado, cidade), cidade)

