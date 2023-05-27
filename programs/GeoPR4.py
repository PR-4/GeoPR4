# importando as bibliotecas necessárias
import pandas as pd
import geopandas as gpd
import folium
from folium.raster_layers import WmsTileLayer
from folium.raster_layers import TileLayer
from folium import plugins
import json
import requests
import webbrowser
import pydeck as pdk

# modulos internos
import sys
sys.path.insert(0,'../modules')
import geoquimica
from geoquimica import publico as pb
import tiles 
from tiles import esri as ly
import blocos
from blocos import publico as bl
import campos
from campos import publico as cp
import bacias
from bacias import publico as bc
import nsismicos
from nsismicos import publico as ns
import debug as d

####################################################
#----------PROGRAMA PRINCIPAL---------------------#
##################################################


#Define o mapa geral
br = folium.Map(location=[-22.0579041,-36.964808],zoom_start=5.96,tiles=None,control_scale=True)#define o mapa inicial

#Define algumas camadas de mapa padao
folium.TileLayer('cartodbpositron',name='claro').add_to(br)
folium.TileLayer('cartodbdark_matter',name='escuro').add_to(br)

#Adiciona camadas de satélites especiais
ly.satelite().add_to(br)
ly.topo().add_to(br)

#blocos exploratórios
bl.blocos().add_to(br)

#Campos 
cp.campos().add_to(br)


#Bacias
bc.bacias().add_to(br)



# Dados não-sísmicos
#ns.nsismico().add_to(br)

# Dados de poços da ANP

# Dados de poços do requititados do PR4
#recebidas = pd.read_csv('../inputs/recebidos.csv',index_col = 0, sep=',', header=0, decimal=',')
#recebidas = recebidas.drop(columns=['LATITUDE_BASE_4C','LONGITUDE_BASE_4C','DATUM_HORIZONTAL','PROFUNDIDADE_SONDADOR_M','AGP'])
#print(recebidas)
#recebidas = gpd.GeoDataFrame(recebidas,geometry = gpd.points_from_xy(recebidas.LATITUDE_BASE_DD, recebidas.LONGITUDE_BASE_DD))
#recebidas.set_crs(epsg="4326", inplace = True, allow_override= True)
#recebidas.info()
#Adding points to the map
#for i, row in recebidas.iterrows():
#    folium.Marker([row['LATITUDE_BASE_DD'], row['LONGITUDE_BASE_DD']],popup="PR4 - recebidos",
#    icon=folium.Icon(color="green", icon="", prefix='fa')).add_to(br)







# Dados de poços de possíveis geradoras do pré-sal
presal = pd.read_csv('../inputs/presal.csv',index_col = 0, sep=',', header=0, decimal=',')
presal = presal.drop(columns=['LATITUDE_BASE_4C','LONGITUDE_BASE_4C','DATUM_HORIZONTAL','PROFUNDIDADE_SONDADOR_M','AGP'])
print(presal)
presal = gpd.GeoDataFrame(presal,geometry = gpd.points_from_xy(presal.LATITUDE_BASE_DD, presal.LONGITUDE_BASE_DD))
presal.set_crs(epsg="4326", inplace = True, allow_override= True)
presal.info()
#Adding points to the map
for i, row in presal.iterrows():
    folium.Marker([row['LATITUDE_BASE_DD'], row['LONGITUDE_BASE_DD']],popup='PR4 pré-sal geradora',
    icon=folium.Icon(color="red", icon="", prefix='fa')).add_to(br)


# Dados de poços de possíveis geradoras do pré-sal que estão na UFF
presaluff = pd.read_csv('../inputs/presal_uff.csv',index_col = 0, sep=',', header=0, decimal=',')
presaluff = presaluff.drop(columns=['LATITUDE_BASE_4C','LONGITUDE_BASE_4C','DATUM_HORIZONTAL','PROFUNDIDADE_SONDADOR_M','AGP'])
print(presaluff)
presaluff = gpd.GeoDataFrame(presaluff,geometry = gpd.points_from_xy(presaluff.LATITUDE_BASE_DD, presaluff.LONGITUDE_BASE_DD))
presaluff.set_crs(epsg="4326", inplace = True, allow_override= True)
presaluff.info()
#Adding points to the map
for i, row in presaluff.iterrows():
    folium.Marker([row['LATITUDE_BASE_DD'], row['LONGITUDE_BASE_DD']],popup='PR4 pré-sal',
    icon=folium.Icon(color="blue", icon="", prefix='fa')).add_to(br)



#Adiciona o poço que está na UFF e temos dados geofísicos
folium.Marker([-23.43707556,-40.72695083], popup='1-BRSA-1007-RJS. Geradora pré-sal presente na UFF com dados geofísicos recebidos',
              icon=folium.Icon(color='green')).add_to(br)


# Dados de geoquímica
#pb.seal01().add_to(br)
pb.seal01_pol().add_to(br)
#pb.seal02().add_to(br)
pb.seal02_pol().add_to(br)
#pb.seal03().add_to(br)
pb.seal03_pol().add_to(br)
#pb.seal04().add_to(br)
final  = pb.seal04_pol().add_to(br) # a última camada sempre e a camada a ser salva

#d.debug()
# Salva e visualiza o GeoPR4

# add full screen button to map
plugins.Fullscreen(position='topright').add_to(br)
draw = plugins.Draw(export=True)# add draw tools to map
draw.add_to(br)

br.add_child(folium.LatLngPopup())
br.add_child(folium.LayerControl())
minimap = plugins.MiniMap(toggle_display=True)
br.add_child(minimap)
final.save('GeoPR4.html')#salva mapa
webbrowser.open_new_tab('GeoPR4.html')# vê o mapa

