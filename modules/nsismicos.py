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
     def nsismico():
        nsismicos_dbf = geopandas.read_file('../inputs/nsismicos/shapefiles_nao_sismicos_13122018.dbf')
        print(nsismicos_dbf.head())
        nsismico = folium.GeoJson(data=nsismicos_dbf["geometry"],
                                   style_function=lambda feature: {'fillColor': 'yellow',
                                                                   'color': 'black',    
                                                                   'weight': 1,         
                                                                   'dashArray': '5, 3'  
                                                                   },name='Aquisições não símicas')

        return nsismico

