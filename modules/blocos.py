# -*- coding: utf-8 -*-

# --------------------------------------------
# Módulo de controle dos blocos
# -------------------------------------------

# importando as bibliotecas necessárias
import pandas as pd
import geopandas
import numpy as np
import folium
import json


class publico:

    def blocos():
        blocos_dbf = geopandas.read_file('../inputs/blocos/BLOCOS_EXPLORATORIOS.dbf')
        print(blocos_dbf.head())
        blocos = folium.GeoJson(data=blocos_dbf["geometry"],
                                style_function=lambda feature: {
                                'fillColor': 'blue',
                                'color': 'black',     #border color for the color fills
                                'weight': 1,          #how thick the border has to be
                                'dashArray': '5, 3'  #dashed lines length,space between them
                                },name='Campos em aberto')
        return blocos

