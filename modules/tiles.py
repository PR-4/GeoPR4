# -*- coding: utf-8 -*-

# --------------------------------------------
# Módulo fontes de dados de satélite
# -------------------------------------------

# importando as bibliotecas necessárias
import folium
from folium.raster_layers import WmsTileLayer
from folium.raster_layers import TileLayer

'''
            "http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer" // World Topographic Map
            "http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer" // World Street Map
            "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer" // Light Gray Canvas
            "http://services.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer" // National Geographic World Map
            "http://services.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer" // Ocean Basemap
            "http://services.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer" // Terrain with Labels
            "http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer" // World Imagery
'''


class esri:
     def satelite():
          url = ('http://services.arcgisonline.com/arcgis/rest/services/World_Imagery' + '/MapServer/tile/{z}/{y}/{x}')

          satelite = WmsTileLayer(url=url,
                            layers=None,
                            name='ESRI Imagery',
                            attr='ESRI World Imagery',
                            )
          return satelite


     def topo():
         World_Topo_Map = ('http://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map' + '/MapServer/tile/{z}/{y}/{x}')
        
         topography = WmsTileLayer(url=World_Topo_Map,
                              layers=None,
                              name='ESRI Topo Map',
                              attr='ESRI Topo Map',
                              )
         return topography
     
     def oceanBase():
         OceanBaseMap = ('https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}')
        
         topography = WmsTileLayer(url=OceanBaseMap,
                              layers=None,
                              name='Ocean Basemap',
                              attr='Tiles (C) Esri -- Sources: GEBCO, NOAA, CHS, OSU, UNH, CSUMB, National Geographic, DeLorme, NAVTEQ, and Esri',
                              )
         return topography


# Adiciona imagens de bandas de satélites
# src1 = (
#    'http://map1.vis.earthdata.nasa.gov/wmts-webmerc/VIIRS_SNPP_CorrectedReflectance_BandsM3-I3-M11/'
#    + 'default/{time}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg'
# )

# TileLayer(
#    tiles=src1,
#    subdomains='abc',
#    name='VIIRS',
#    attr='NASA VIIRS',
#    overlay=True,
#    layer='VIIRS_SNPP_CorrectedReflectance_BandsM11-I2-I1',
#    tileMatrixSet='GoogleMapsCompatible_Level9',
#    time='2022-01-09',
#    tileSize=256,
# ).add_to(br)


# src2 = (
#    'http://map1.vis.earthdata.nasa.gov/wmts-webmerc/{layer}/'
#    + 'default/{time}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg'
# )

# TileLayer(
#    tiles=src2,
#    subdomains='abc',
#    name='VIIRS',
#    attr='NASA VIIRS',
#    overlay=True,
#    layer='VIIRS_SNPP_CorrectedReflectance_TrueColor',
#    tileMatrixSet='GoogleMapsCompatible_Level9',
#    time='2019-11-10',
#    tileSize=256,
# ).add_to(br)

# src3 = (
#    'http://map1.vis.earthdata.nasa.gov/wmts-webmerc/{layer}/'
#    + 'default/{time}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg'
# )

# TileLayer(
#    tiles=src3,
#    subdomains='abc',
#    name='True Color',
#    attr='NASA VIIRS',
#    overlay=True,
#    layer='VIIRS_SNPP_CorrectedReflectance_TrueColor',
#    tileMatrixSet='GoogleMapsCompatible_Level9',
#    time='2019-11-11',
#    tileSize=256,
# ).add_to(br)


# TileLayer(
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
# ).add_to(br)

# TileLayer(
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
# ).add_to(br)
