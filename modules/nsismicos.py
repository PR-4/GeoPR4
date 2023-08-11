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
    def spec258():
        """
        Shape contendo a distribuição espacial dos dados de espectroscopia da Bacia de Espírito Santo.
        """
        SPEC258_dbf = geopandas.read_file(
            "../inputs/nsismicos/0258_2D_SPEC_BM_ES_grid/0258_2D_SPEC_BM_ES_grid.dbf"
        )
        print(SPEC258_dbf.head())
        SPEC258 = folium.GeoJson(
            data=SPEC258_dbf["geometry"],
            style_function=lambda feature: {
                "fillColor": "yellow",
                "color": "black",
                "weight": 1,
                "dashArray": "5, 3",
            },
            name="Espectroscopia Aérea",
        )
        return SPEC258

    def grav264():
        """
        Shapefile contendo a distribuição espacial dos dados de gravimetria da bacia do Espírito Santo.
        """
        GRAV264_dbf = geopandas.read_file(
            "../inputs/nsismicos/0264_GRAV_BMES1_grid/0264_GRAV_BMES1_grid.dbf"
        )
        print(GRAV264_dbf.head())
        GRAV264 = folium.GeoJson(
            data=GRAV264_dbf["geometry"],
            style_function=lambda feature: {
                "fillColor": "yellow",
                "color": "black",
                "weight": 1,
                "dashArray": "5, 3",
            },
            name="Gravimetria",
        )

        return GRAV264

    def grav297():
        """
        Shapefile contendo a distribuição espacial dos dados de gravimetria da bacia do Sergipe-Alagoas.
        """
        GRAV297_dbf = geopandas.read_file(
            "../inputs/nsismicos/0297_GRAV_3D_BM_SEAL_9_grid/0264_GRAV_BMES1_grid.dbf"
        )
        print(GRAV297_dbf.head())
        GRAV297 = folium.GeoJson(
            data=GRAV297_dbf["geometry"],
            style_function=lambda feature: {
                "fillColor": "yellow",
                "color": "black",
                "weight": 1,
                "dashArray": "5, 3",
            },
            name="Gravimetria",
        )
        return GRAV297

    def mag297():
        """
        Shapefile contendo a distribuição espacial dos dados de magnetometria da bacia do Sergipe-Alagoas.
        """
        MAG297_dbf = geopandas.read_file(
            "../inputs/nsismicos/0297_MAG_3D_BM_SEAL_9_grid/0297_MAG_3D_BM_SEAL_9_grid.dbf"
        )
        print(MAG297_dbf.head())
        MAG297 = folium.GeoJson(
            data=MAG297_dbf["geometry"],
            style_function=lambda feature: {
                "fillColor": "yellow",
                "color": "black",
                "weight": 1,
                "dashArray": "5, 3",
            },
            name="Magnetometria",
        )
        return MAG297
