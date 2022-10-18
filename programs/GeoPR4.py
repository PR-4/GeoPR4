# importando as bibliotecas necessárias
import pandas as pd
import geopandas
import numpy as np
import matplotlib.pyplot as plt
import folium
from folium.raster_layers import WmsTileLayer
from folium.raster_layers import TileLayer
import webbrowser
import pydeck as pdk



#Define o mapa geral
br = folium.Map(location=[-22.0579041,-36.964808],zoom_start=5.96,tiles=None)#define o mapa inicial
#Define algumas camadas de mapa padao
folium.TileLayer('cartodbpositron',name='claro').add_to(br)
folium.TileLayer('cartodbdark_matter',name='escuro').add_to(br)
#Adiciona camadas de satélites especiais
'''
            "http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer" // World Topographic Map
            "http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer" // World Street Map
            "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer" // Light Gray Canvas
            "http://services.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer" // National Geographic World Map
            "http://services.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer" // Ocean Basemap
            "http://services.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer" // Terrain with Labels
            "http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer" // World Imagery
'''

url = (
    'http://services.arcgisonline.com/arcgis/rest/services/World_Imagery'
    + '/MapServer/tile/{z}/{y}/{x}'
)
WmsTileLayer(
    url=url,
    layers=None,
    name='ESRI Imagery',
    attr='ESRI World Imagery',
).add_to(br)

World_Topo_Map = (
    'http://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map'
    + '/MapServer/tile/{z}/{y}/{x}'
)
WmsTileLayer(
    url=World_Topo_Map,
    layers=None,
    name='ESRI Topo Map',
    attr='ESRI Topo Map',
).add_to(br)



#Adiciona imagens de bandas de satélites
#src1 = (
#    'http://map1.vis.earthdata.nasa.gov/wmts-webmerc/VIIRS_SNPP_CorrectedReflectance_BandsM3-I3-M11/'
#    + 'default/{time}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg'
#)

#TileLayer(
#    tiles=src1,
#    subdomains='abc',
#    name='VIIRS',
#    attr='NASA VIIRS',
#    overlay=True,
#    layer='VIIRS_SNPP_CorrectedReflectance_BandsM11-I2-I1',
#    tileMatrixSet='GoogleMapsCompatible_Level9',
#    time='2022-01-09',
#    tileSize=256,
#).add_to(br)


#src2 = (
#    'http://map1.vis.earthdata.nasa.gov/wmts-webmerc/{layer}/'
#    + 'default/{time}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg'
#)

#TileLayer(
#    tiles=src2,
#    subdomains='abc',
#    name='VIIRS',
#    attr='NASA VIIRS',
#    overlay=True,
#    layer='VIIRS_SNPP_CorrectedReflectance_TrueColor',
#    tileMatrixSet='GoogleMapsCompatible_Level9',
#    time='2019-11-10',
#    tileSize=256,
#).add_to(br)

#src3 = (
#    'http://map1.vis.earthdata.nasa.gov/wmts-webmerc/{layer}/'
#    + 'default/{time}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg'
#)

#TileLayer(
#    tiles=src3,
#    subdomains='abc',
#    name='True Color',
#    attr='NASA VIIRS',
#    overlay=True,
#    layer='VIIRS_SNPP_CorrectedReflectance_TrueColor',
#    tileMatrixSet='GoogleMapsCompatible_Level9',
#    time='2019-11-11',
#    tileSize=256,
#).add_to(br)


#TileLayer(
#    tiles=src3,
#    subdomains='abc',
#    name='Bands M11-12',
#    attr='NASA VIIRS',
#    overlay=True,
#    show=False,
#    layer='VIIRS_SNPP_CorrectedReflectance_BandsM11-I2-I1',
#    tileMatrixSet='GoogleMapsCompatible_Level9',
#    time='2019-11-11',
#    tileSize=256,
#).add_to(br)

#TileLayer(
#    tiles=src3,
#    subdomains='abc',
#    name='Bands M3-13',
#    attr='NASA VIIRS',
#    overlay=True,
#    show=False,
#    layer='VIIRS_SNPP_CorrectedReflectance_BandsM3-I3-M11',
#    tileMatrixSet='GoogleMapsCompatible_Level9',
#    time='2019-11-11',
#    tileSize=256,
#).add_to(br)


#Adiciona o shapefile

#blocos exploratórios

blocos_dbf = geopandas.read_file('../inputs/blocos/BLOCOS_EXPLORATORIOS.dbf')


print(blocos_dbf.head())


blocos = folium.GeoJson(data=blocos_dbf["geometry"],
        style_function=lambda feature: {
        'fillColor': 'blue',
        'color': 'black',     #border color for the color fills
        'weight': 1,          #how thick the border has to be
        'dashArray': '5, 3'  #dashed lines length,space between them
    }).add_to(br)

#blocos.save('blocos.html')#salva mapa
#webbrowser.open_new_tab('blocos.html')# vê o mapa


#Campos 

campos_dbf = geopandas.read_file('../inputs/campos/CAMPOS_PRODUCAO.dbf')


print(campos_dbf.head())



campos = folium.GeoJson(data=campos_dbf["geometry"],
        style_function=lambda feature: {
        'fillColor': 'red',
        'color': 'black',     #border color for the color fills
        'weight': 1,          #how thick the border has to be
        'dashArray': '5, 3'  #dashed lines length,space between them
    }).add_to(br)



#br.add_child(folium.LatLngPopup())
#br.add_child(folium.LayerControl())
#campos.save('campos.html')#salva mapa
#webbrowser.open_new_tab('campos.html')# vê o mapa

#Bacias

#bacias_dbf = geopandas.read_file('../inputs/bacias/bacias.dbf')


#print(bacias_dbf.head())



#bacias = folium.GeoJson(data=bacias_dbf["geometry"],
#        style_function=lambda feature: {
#        'fillColor': 'green',
#        'color': 'black',     #border color for the color fills
#        'weight': 1,          #how thick the border has to be
#        'dashArray': '5, 3'  #dashed lines length,space between them
#    }).add_to(br)
#bacias.save('bacias.html')#salva mapa
#webbrowser.open_new_tab('bacias.html')# vê o mapa


# Dados não-sísmicos

nsismicos_dbf = geopandas.read_file('../inputs/nsismicos/shapefiles_nao_sismicos_13122018.dbf')


print(nsismicos_dbf.head())



nsismicos = folium.GeoJson(data=campos_dbf["geometry"],
        style_function=lambda feature: {
        'fillColor': 'yellow',
        'color': 'black',     #border color for the color fills
        'weight': 1,          #how thick the border has to be
        'dashArray': '5, 3'  #dashed lines length,space between them
    }).add_to(br)



br.add_child(folium.LatLngPopup())
br.add_child(folium.LayerControl())
nsismicos.save('GeoPR4.html')#salva mapa
webbrowser.open_new_tab('GeoPR4.html')# vê o mapa

