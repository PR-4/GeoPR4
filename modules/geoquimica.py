# -*- coding: utf-8 -*-

# --------------------------------------------
# Módulo de controle dos dados de geoquímica
# -------------------------------------------

# importando as bibliotecas necessárias
import pandas as pd
import geopandas
import numpy as np
import folium
import json


# Diretórios:
entrada = '..'+'/'+'inputs'+'/'+'geoquimicos'+'/'+'SHAPES_Atualizado'+'/'


class publico:
#SEAL
    def seal01():
        seal01 = geopandas.read_file(
            entrada+"Publicos/GQ_003_SEAL-T-340_QUANTRA/GQ_003_SEAL_T_340_QUANTRA.dbf")

        # define um CRS e ou mantém um já existente
        seal01 = seal01.set_crs(epsg="4326", inplace=True, allow_override=True)

        seal01_geoq = folium.GeoJson(data=seal01["geometry"],
                                     style_function=lambda feature: {
            'fillColor': 'green',
            'color': 'black',  # border color for the color fills
            'weight': 1,  # how thick the border has to be
            'dashArray': '5, 3'  # dashed lines length,space between them
        }, name='Aquisições geoquímicas')  # .add_to(br)

        return seal01_geoq


    def seal01_pol():
         seal01_pol = geopandas.read_file(
            entrada+"Publicos/GQ_003_SEAL-T-340_QUANTRA/GQ_003_SEAL_T_340_QUANTRA_Poligono.dbf")
            
         # define um CRS e ou mantém um já existente
         seal01_pol = seal01_pol.set_crs(epsg="4326", inplace=True, allow_override=True)

         seal01_pol_geoq = folium.GeoJson(data=seal01_pol["geometry"],
                                     style_function=lambda feature: {
            'fillColor': 'green',
            'color': 'black',  # border color for the color fills
            'weight': 1,  # how thick the border has to be
            'dashArray': '5, 3'  # dashed lines length,space between them
        }, name='Aquisições geoquímicas')
        
         return seal01_pol_geoq
         
             # def geoquimica(seal01,seal02,seal03,seal04,seal01_pol,seal02_pol,seal03_pol,seal04_pol):
    def seal02():
        seal02 = geopandas.read_file(entrada+"Publicos/GQ_003_SEAL-T-369_QUANTRA/GQ_003_SEAL-T-369_QUANTRA.dbf")

        # define um CRS e ou mantém um já existente
        seal02 = seal02.set_crs(epsg="4326", inplace=True, allow_override=True)

        seal02_geoq = folium.GeoJson(data=seal02["geometry"],
                                     style_function=lambda feature: {
            'fillColor': 'green',
            'color': 'black',  # border color for the color fills
            'weight': 1,  # how thick the border has to be
            'dashArray': '5, 3'  # dashed lines length,space between them
        }, name='Aquisições geoquímicas')  # .add_to(br)

        return seal02_geoq


    def seal02_pol():
         seal02_pol = geopandas.read_file(entrada+"Publicos/GQ_003_SEAL-T-369_QUANTRA/GQ_003_SEAL_T_369_QUANTRA_Poligono.dbf")
            
         # define um CRS e ou mantém um já existente
         seal02_pol = seal02_pol.set_crs(epsg="4326", inplace=True, allow_override=True)

         seal02_pol_geoq = folium.GeoJson(data=seal02_pol["geometry"],
                                     style_function=lambda feature: {
            'fillColor': 'green',
            'color': 'black',  # border color for the color fills
            'weight': 1,  # how thick the border has to be
            'dashArray': '5, 3'  # dashed lines length,space between them
        }, name='Aquisições geoquímicas')
        
         return seal02_pol_geoq
         
    def seal03():
        seal03 = geopandas.read_file(entrada+"Publicos/GQ_003_SEAL-T-426_QUANTRA/GQ_003_SEAL-T-426_QUANTRA.dbf")

        # define um CRS e ou mantém um já existente
        seal03 = seal03.set_crs(epsg="4326", inplace=True, allow_override=True)

        seal03_geoq = folium.GeoJson(data=seal03["geometry"],
                                     style_function=lambda feature: {
            'fillColor': 'green',
            'color': 'black',  # border color for the color fills
            'weight': 1,  # how thick the border has to be
            'dashArray': '5, 3'  # dashed lines length,space between them
        }, name='Aquisições geoquímicas')  # .add_to(br)

        return seal03_geoq


    def seal03_pol():
         seal03_pol = geopandas.read_file(entrada+"Publicos/GQ_003_SEAL-T-426_QUANTRA/GQ_003_SEAL_T_426_QUANTRA_Poligono.dbf")
            
         # define um CRS e ou mantém um já existente
         seal03_pol = seal03_pol.set_crs(epsg="4326", inplace=True, allow_override=True)

         seal03_pol_geoq = folium.GeoJson(data=seal03_pol["geometry"],
                                     style_function=lambda feature: {
            'fillColor': 'green',
            'color': 'black',  # border color for the color fills
            'weight': 1,  # how thick the border has to be
            'dashArray': '5, 3'  # dashed lines length,space between them
        }, name='Aquisições geoquímicas')
        
         return seal03_pol_geoq
         
    def seal04():
        seal04 = geopandas.read_file(entrada+"Publicos/GQ_003_SEAL-T-434_QUANTRA/GQ_003_SEAL_T_434_QUANTRA.dbf")

        # define um CRS e ou mantém um já existente
        seal04 = seal04.set_crs(epsg="4326", inplace=True, allow_override=True)

        seal04_geoq = folium.GeoJson(data=seal04["geometry"],
                                     style_function=lambda feature: {
            'fillColor': 'green',
            'color': 'black',  # border color for the color fills
            'weight': 1,  # how thick the border has to be
            'dashArray': '5, 3'  # dashed lines length,space between them
        }, name='Aquisições geoquímicas')  # .add_to(br)

        return seal04_geoq


    def seal04_pol():
         seal04_pol = geopandas.read_file(entrada+"Publicos/GQ_003_SEAL-T-434_QUANTRA/GQ_003_SEAL_T_434_QUANTRA_Poligono.dbf")
            
         # define um CRS e ou mantém um já existente
         seal04_pol = seal04_pol.set_crs(epsg="4326", inplace=True, allow_override=True)

         seal04_pol_geoq = folium.GeoJson(data=seal04_pol["geometry"],
                                     style_function=lambda feature: {
            'fillColor': 'green',
            'color': 'black',  # border color for the color fills
            'weight': 1,  # how thick the border has to be
            'dashArray': '5, 3'  # dashed lines length,space between them
        }, name='Aquisições geoquímicas')
        
         return seal04_pol_geoq


# class confidencial:
