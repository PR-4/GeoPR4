# -*- coding: utf-8 -*-

# --------------------------------------------
# Módulo de controle dos campos de produção
# -------------------------------------------

# importando as bibliotecas necessárias
import pandas as pd
import geopandas
import numpy as np
import folium
import json


class publico:
    def bacias():
        bacias_dbf = geopandas.read_file("../inputs/bacias/Bacias/posicao_bacias.dbf")
        bacias_dbf = bacias_dbf.set_crs(
            epsg="4326", inplace=True, allow_override=True
        )  # define um CRS e ou mantém um já existente
        # bacias_dbf = bacias_dbf.to_crs(epsg = "25833", inplace = True)#transforma para outro CRS
        print(bacias_dbf.head())

        bacias = folium.GeoJson(
            data=bacias_dbf["geometry"],
            style_function=lambda feature: {
                "fillColor": "green",
                "color": "black",  # border color for the color fills
                "weight": 1,  # how thick the border has to be
                "dashArray": "5, 3",  # dashed lines length,space between them
            },
            name="Bacias Off-shore",
        )
        return bacias
