# Importando as bibliotecas necessárias
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

# Módulos internos
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
import pocos
from pocos import PR4 as pr
import bathmetry
from bathmetry import bath as ba 

####################################################
#--------------PROGRAMA PRINCIPAL------------------#
####################################################


# Define o mapa geral
br = folium.Map(location=[-22.0579041,-36.964808],
                zoom_start=5.96,
                tiles=None,
                control_scale=True)

# Define algumas camadas de mapa padao
folium.TileLayer('cartodbpositron',name='claro').add_to(br)
folium.TileLayer('cartodbdark_matter',name='escuro').add_to(br)

# Adiciona camadas de satélites especiais
ly.satelite().add_to(br) # ESRI Imagery
ly.topo().add_to(br) # ESRI Topo
ly.oceanBase().add_to(br) # Ocean Basemap

# Blocos Exploratórios
bl.blocos().add_to(br)

# Campos 
cp.campos().add_to(br)

# Bacias
bc.bacias().add_to(br)

# Batimetria 
ba.bathmetry().add_to(br)

# Dados não-sísmicos
ns.mag297().add_to(br)

# Santos Outer-high and square selection
#bl.outerhigh().add_to(br)
#bl.square_selection().add_to(br)

# Dados de poços da PR4
pr.pocosRecebidos().add_to(br)
pr.pocosSelGePreSal().add_to(br)
pr.pocosPriPedPetANP().add_to(br)
pr.pocosUFF().add_to(br)

# Dados de Geoquímica
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

# Adicionando plugins no mapa
plugins.Fullscreen(position='topright').add_to(br) # Tela cheia
draw = plugins.Draw(export=True) # Adiciona ferramentas de desenho
draw.add_to(br)

br.add_child(folium.LatLngPopup()) # Adiciona Lat e Lon clicando
br.add_child(folium.LayerControl()) # Adiciona controle das camadas
minimap = plugins.MiniMap(toggle_display=True) # Adiciona minimap
br.add_child(minimap)
final.save('GeoPR4.html') # Salva o mapa
webbrowser.open_new_tab('GeoPR4.html') # Abre o mapa no browser
