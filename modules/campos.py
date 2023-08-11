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
    def campos():
        campos_dbf = geopandas.read_file("../inputs/campos/CAMPOS_PRODUCAO.dbf")
        print(campos_dbf.head())
        campos = folium.GeoJson(
            data=campos_dbf["geometry"],
            style_function=lambda feature: {
                "fillColor": "red",
                "color": "black",
                "weight": 1,
                "dashArray": "5, 3",
            },
            name="Campos em produção",
        )
        return campos
