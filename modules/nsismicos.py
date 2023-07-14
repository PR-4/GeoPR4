# -*- coding: utf-8 -*-

# ----------------------------------------------------
# Módulo de controle dos dados geofísicos não sísmicos
# ---------------------------------------------------

# importando as bibliotecas necessárias
import pandas as pd
import geopandas
import numpy as np
import folium
import json


class publico:
     def espectroscopia():
        258SPEC_dbf = geopandas.read_file('../inputs/nsismicos/0258_2D_SPEC_BM_ES_grid/0258_2D_SPEC_BM_ES_grid.dbf')
        print(258SPEC_dbf.head())
        258SPEC = folium.GeoJson(data=258SPEC_dbf["geometry"],
                                   style_function=lambda feature: {'fillColor': 'yellow',
                                                                   'color': 'black',    
                                                                   'weight': 1,         
                                                                   'dashArray': '5, 3'  
                                                                   },name='Espectroscopia Aérea')

         return 258SPEC

     def gravimetria():
         264GRAV_dbf = geopandas.read_file('../inputs/nsismicos/0264_GRAV_BMES1_grid.dbf')
         print(264GRAV_dbf.head())
         264GRAV = folium.GeoJson(data=264GRAV_dbf["geometry"],
                                    style_function=lambda feature: {'fillColor': 'yellow',
                                                                    'color': 'black',    
                                                                    'weight': 1,         
                                                                    'dashArray': '5, 3'  
                                                                    },name='Gravimetria')

         return 264GRAV
