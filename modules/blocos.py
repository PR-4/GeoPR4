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
        blocos_dbf = geopandas.read_file("../inputs/blocos/BLOCOS_EXPLORATORIOS.dbf")
        print(blocos_dbf.head())
        blocos = folium.GeoJson(
            data=blocos_dbf["geometry"],
            style_function=lambda feature: {
                "fillColor": "blue",
                "color": "black",  # border color for the color fills
                "weight": 1,  # how thick the border has to be
                "dashArray": "5, 3",  # dashed lines length,space between them
            },
            name="Campos em aberto",
        )
        return blocos

    def outerhigh():
        outerhigh_dbf = geopandas.read_file(
            "../inputs/shapes/Santos_outerhigh/santos_outer_high.dbf"
        )
        # outerhigh_dbf = outerhigh_dbf.set_crs(epsg = "4326", inplace = True, allow_override= True) #define um CRS e ou mantém um já existente
        # print(outerhigh_dbf.head())
        outerhigh = folium.GeoJson(
            data=outerhigh_dbf["geometry"],
            style_function=lambda feature: {
                "fillColor": "green",
                "color": "black",  # border color for the color fills
                "weight": 1,  # how thick the border has to be
                "dashArray": "5, 3",  # dashed lines length,space between them
            },
            name="Santos External High",
        )
        return outerhigh

    def square_selection():
        square_dbf = geopandas.read_file(
            "../inputs/shapes/Santos_outerhigh/square_selection/santos_external_high_squareShape.dbf"
        )
        # square_dbf = square_dbf.set_crs(epsg = "4326", inplace = True, allow_override= True) #define um CRS e ou mantém um já existente
        print(square_dbf.head())
        square = folium.GeoJson(
            data=outerhigh_dbf["geometry"],
            style_function=lambda feature: {
                "fillColor": "gray",
                "color": "black",  # border color for the color fills
                "weight": 1,  # how thick the border has to be
                "dashArray": "5, 3",  # dashed lines length,space between them
            },
            name="Square selection",
        )
        return square_selection
