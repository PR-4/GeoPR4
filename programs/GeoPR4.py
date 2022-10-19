# importando as bibliotecas necessárias
import pandas as pd
import geopandas
import folium
from folium.raster_layers import WmsTileLayer
from folium.raster_layers import TileLayer
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

####################################################
#----------PROGRAMA PRINCIPAL---------------------#
##################################################


#Define o mapa geral
br = folium.Map(location=[-22.0579041,-36.964808],zoom_start=5.96,tiles=None)#define o mapa inicial

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
ns.nsismico().add_to(br) 


# Dados de geoquímica
#pb.seal01().add_to(br)
pb.seal01_pol().add_to(br)
#pb.seal02().add_to(br)
pb.seal02_pol().add_to(br)
#pb.seal03().add_to(br)
pb.seal03_pol().add_to(br)
#pb.seal04().add_to(br)
final  = pb.seal04_pol().add_to(br) # a última camada sempre e a camada a ser salva

# Salva e visualiza o GeoPR4
br.add_child(folium.LatLngPopup())
br.add_child(folium.LayerControl())
final.save('GeoPR4.html')#salva mapa
webbrowser.open_new_tab('GeoPR4.html')# vê o mapa

