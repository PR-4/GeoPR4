# importando as bibliotecas necessárias
import pandas as pd
import geopandas
import numpy as np
import folium
import json


class bath:
    def bathmetry():
        bathmetry_dbf = geopandas.read_file(
            "../inputs/bathmetry/GEBCO_santos_basin_bath_contours.dbf"
        )
        bathmetry_dbf = bathmetry_dbf.set_crs(
            epsg="4326", inplace=True, allow_override=True
        )  # define um CRS e ou mantém um já existente
        # bacias_dbf = bacias_dbf.to_crs(epsg = "25833", inplace = True)#transforma para outro CRS
        print(bathmetry_dbf.head())

        bathmetry = folium.GeoJson(
            data=bathmetry_dbf["geometry"],
            style_function=lambda feature: {
                "color": "black",  # border color for the color fills
                "weight": 0.5,  # how thick the border has to be
                "dashArray": None,
                "opacity": 0.5,  # dashed lines length,space between them
            },
            name="Linhas Batimétricas",
        )
        return bathmetry
