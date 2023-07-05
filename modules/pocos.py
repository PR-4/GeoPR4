# importando as bibliotecas necessárias
import pandas as pd
import geopandas as gpd
import folium

class PR4:
    def pocosRecebidos():
        # Importando dados
        recebido = pd.read_excel('../inputs/pocos/pocos_recebidos_e_selecao.xlsx',
                         sheet_name='RECEBIDOS',
                         header=0,
                         decimal=',',
                         engine='openpyxl',
                         usecols=['POCO', 'BACIA', 'TIPO', 'PROFUNDIDADE_SONDADOR_M',
                                  'LATITUDE_BASE_DD', 'LONGITUDE_BASE_DD', 'AGP',
                                  'PC', 'SISMICA', 'GEOQUIMICA', 'ATINGIU_PRESAL']
                         )
        recebido = gpd.GeoDataFrame(recebido, 
                                    geometry = gpd.points_from_xy(recebido.LATITUDE_BASE_DD, 
                                                                  recebido.LONGITUDE_BASE_DD))
        recebido.set_crs(epsg="4326", inplace = True, allow_override= True)

        # Criando lista para marcadores
        markers = []

        # Iteração dos dados para popup de marcadores
        for _, row in recebido.iterrows():
            # Criando o conteúdo do popup
            popup_content = f"<h5><b>INFORMAÇÕES GERAIS</b></h5>"
            popup_content += f"<b>Nome do poço:</b> {row['POCO']}<br>"
            popup_content += f"<b>Bacia:</b> {row['BACIA']}<br>"
            popup_content += f"<b>Tipo do poço:</b> {row['TIPO']}<br>"
            popup_content += f"<b>Profundidade:</b> {row['PROFUNDIDADE_SONDADOR_M']}<br>"
            popup_content += f"<h5><b>DADOS ACESSÓRIOS</b></h5>"
            if pd.notnull(row['AGP']):
                popup_content += f"<b>AGP:</b> {'Sim' if row['AGP'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['PC']):
                popup_content += f"<b>Perfil Composto:</b> {'Sim' if row['PC'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['SISMICA']):
                popup_content += f"<b>Sísmica do poço:</b> {'Sim' if row['SISMICA'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['GEOQUIMICA']):
                popup_content += f"<b>Geoquímica do poço:</b> {'Sim' if row['GEOQUIMICA'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['ATINGIU_PRESAL']):
                popup_content += f"<b>Atingiu Pré-Sal?:</b> {'Sim' if row['ATINGIU_PRESAL'] == 'S' else 'Não'}<br>"
            popup_content += f"<h5><b>DADOS PRIMÁRIOS</b></h5>"
            popup_content += f"<b>COT:</b> <br>"
            popup_content += f"<b>Rock Eval:</b> <br>"
            popup_content += f"<b>Biomarcadores:</b> <br>"
            popup_content += f"<b>Geoquímica Inorgânica:</b> <br>"

            # Criar marcador de círculos
            marker = folium.Circle(
                 [row['LATITUDE_BASE_DD'], 
                  row['LONGITUDE_BASE_DD']],
                 popup=folium.Popup(popup_content,
                                    max_width=1000,
                                    lazy=True),
                 color='crimson',
                 radius=1000,
                 fill=True,
            )

            # Adicionar marcadores na lista 
            markers.append(marker)

        # Criar grupo para os marcadores
        pocos_group = folium.FeatureGroup(name='Pocos Recebidos', 
                                          show=True)
        for marker in markers:
            marker.add_to(pocos_group)

        # Retornar o grupo
        return pocos_group
    
    def pocosSelGePreSal():
        # Importando dados
        selecaoGePreSal = pd.read_excel('../inputs/pocos/pocos_recebidos_e_selecao.xlsx',
                                         sheet_name='SELECAO_GERADORA_PRE_SAL',
                                         header=0,
                                         decimal=',',
                                         engine='openpyxl',
                                         usecols=['POCO', 'BACIA', 
                                                  'TIPO', 'PROFUNDIDADE_SONDADOR_M',
                                                  'LATITUDE_BASE_DD', 'LONGITUDE_BASE_DD',
                                                  'AGP', 'PC', 'SISMICA', 'GEOQUIMICA', 
                                                  'ATINGIU_PRESAL']
                                                  )
        selecaoGePreSal = gpd.GeoDataFrame(selecaoGePreSal,
                                           geometry = gpd.points_from_xy(selecaoGePreSal.LATITUDE_BASE_DD, 
                                                                         selecaoGePreSal.LONGITUDE_BASE_DD))
        selecaoGePreSal.set_crs(epsg="4326", inplace = True, allow_override= True)
        
        # Criando lista para marcadores
        markers = []

        # Iteração dos dados para popup de marcadores
        for _, row in selecaoGePreSal.iterrows():
            # Criando o conteúdo do popup
            popup_content = f"<h5><b>INFORMAÇÕES GERAIS</b></h5>"
            popup_content += f"<b>Nome do poço:</b> {row['POCO']}<br>"
            popup_content += f"<b>Bacia:</b> {row['BACIA']}<br>"
            popup_content += f"<b>Tipo do poço:</b> {row['TIPO']}<br>"
            popup_content += f"<b>Profundidade:</b> {row['PROFUNDIDADE_SONDADOR_M']}<br>"
            popup_content += f"<h5><b>DADOS ACESSÓRIOS</b></h5>"
            if pd.notnull(row['AGP']):
                popup_content += f"<b>AGP:</b> {'Sim' if row['AGP'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['PC']):
                popup_content += f"<b>Perfil Composto:</b> {'Sim' if row['PC'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['SISMICA']):
                popup_content += f"<b>Sísmica do poço:</b> {'Sim' if row['SISMICA'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['GEOQUIMICA']):
                popup_content += f"<b>Geoquímica do poço:</b> {'Sim' if row['GEOQUIMICA'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['ATINGIU_PRESAL']):
                popup_content += f"<b>Atingiu Pré-Sal?:</b> {'Sim' if row['ATINGIU_PRESAL'] == 'S' else 'Não'}<br>"
            popup_content += f"<h5><b>DADOS PRIMÁRIOS</b></h5>"
            popup_content += f"<b>COT:</b> <br>"
            popup_content += f"<b>Rock Eval:</b> <br>"
            popup_content += f"<b>Biomarcadores:</b> <br>"
            popup_content += f"<b>Geoquímica Inorgânica:</b> <br>"

            # Criar marcador de círculos
            marker = folium.Circle(
                 [row['LATITUDE_BASE_DD'], 
                  row['LONGITUDE_BASE_DD']],
                 popup=folium.Popup(popup_content,
                                    max_width=1000,
                                    lazy=True),
                 color='darkblue',
                 radius=1000,
                 fill=True,
            )

            # Adicionando marcadores na lista
            markers.append(marker)

        # Criar grupo para os marcadores
        pocos_group = folium.FeatureGroup(name='Pocos Seleção\nGeradora PreSal', 
                                          show=True)
        for marker in markers:
            marker.add_to(pocos_group)

        # Retornando o grupo
        return pocos_group
    
    def pocosPriPedPetANP():
        # Importando dados
        primeiroPedPetANP = pd.read_excel('../inputs/pocos/pocos_recebidos_e_selecao.xlsx',
                                          sheet_name='1_PEDIDO_PETICIONADO_ANP',
                                          header=0,
                                          decimal=',',
                                          engine='openpyxl',
                                          usecols=['POCO', 'BACIA', 
                                                   'TIPO', 'PROFUNDIDADE_SONDADOR_M',
                                                   'LATITUDE_BASE_DD', 'LONGITUDE_BASE_DD',
                                                   'AGP', 'PC', 'SISMICA', 'GEOQUIMICA', 
                                                   'ATINGIU_PRESAL']
                                                   )
        primeiroPedPetANP = gpd.GeoDataFrame(primeiroPedPetANP,
                                             geometry = gpd.points_from_xy(primeiroPedPetANP.LATITUDE_BASE_DD, 
                                                                           primeiroPedPetANP.LONGITUDE_BASE_DD))
        primeiroPedPetANP.set_crs(epsg="4326", inplace = True, allow_override= True)
        
        # Criando lista para marcadores
        markers = []

        # Iteração dos dados para popup de marcadores
        for _, row in primeiroPedPetANP.iterrows():
            # Criando o conteúdo do popup
            popup_content = f"<h5><b>INFORMAÇÕES GERAIS</b></h5>"
            popup_content += f"<b>Nome do poço:</b> {row['POCO']}<br>"
            popup_content += f"<b>Bacia:</b> {row['BACIA']}<br>"
            popup_content += f"<b>Tipo do poço:</b> {row['TIPO']}<br>"
            popup_content += f"<b>Profundidade:</b> {row['PROFUNDIDADE_SONDADOR_M']}<br>"
            popup_content += f"<h5><b>DADOS ACESSÓRIOS</b></h5>"
            if pd.notnull(row['AGP']):
                popup_content += f"<b>AGP:</b> {'Sim' if row['AGP'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['PC']):
                popup_content += f"<b>Perfil Composto:</b> {'Sim' if row['PC'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['SISMICA']):
                popup_content += f"<b>Sísmica do poço:</b> {'Sim' if row['SISMICA'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['GEOQUIMICA']):
                popup_content += f"<b>Geoquímica do poço:</b> {'Sim' if row['GEOQUIMICA'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['ATINGIU_PRESAL']):
                popup_content += f"<b>Atingiu Pré-Sal?:</b> {'Sim' if row['ATINGIU_PRESAL'] == 'S' else 'Não'}<br>"
            popup_content += f"<h5><b>DADOS PRIMÁRIOS</b></h5>"
            popup_content += f"<b>COT:</b> <br>"
            popup_content += f"<b>Rock Eval:</b> <br>"
            popup_content += f"<b>Biomarcadores:</b> <br>"
            popup_content += f"<b>Geoquímica Inorgânica:</b> <br>"

            # Criar marcador de círculos
            marker = folium.Circle(
                 [row['LATITUDE_BASE_DD'], 
                  row['LONGITUDE_BASE_DD']],
                 popup=folium.Popup(popup_content,
                                    max_width=1000,
                                    lazy=True),
                 color='green',
                 radius=1000,
                 fill=True,
            )

            # Adicionando marcadores na lista
            markers.append(marker)

        # Criar grupo para os marcadores
        pocos_group = folium.FeatureGroup(name='Pocos Primeiro\nPedido Peticionado', 
                                          show=True)
        for marker in markers:
            marker.add_to(pocos_group)

        # Retornando o grupo
        return pocos_group

    def pocosUFF():
        # Importando dados
        pocosNaUFF = pd.read_excel('../inputs/pocos/pocos_recebidos_e_selecao.xlsx',
                                      sheet_name='POCO_UFF',
                                      header=0,
                                      decimal=',',
                                      engine='openpyxl',
                                      usecols=['POCO', 'BACIA', 
                                               'TIPO', 'PROFUNDIDADE_SONDADOR_M',
                                               'LATITUDE_BASE_DD', 'LONGITUDE_BASE_DD',
                                               'AGP', 'PC', 'SISMICA', 'GEOQUIMICA', 
                                               'ATINGIU_PRESAL']
                                               )
        pocosNaUFF = gpd.GeoDataFrame(pocosNaUFF,
                                      geometry = gpd.points_from_xy(pocosNaUFF.LATITUDE_BASE_DD, 
                                                                    pocosNaUFF.LONGITUDE_BASE_DD))
        pocosNaUFF.set_crs(epsg="4326", inplace = True, allow_override= True)
        
        # Criando lista para marcadores
        markers = []

        # Iteração dos dados para popup de marcadores
        for _, row in pocosNaUFF.iterrows():
            # Criando o conteúdo do popup
            popup_content = f"<h5><b>INFORMAÇÕES GERAIS</b></h5>"
            popup_content += f"<b>Nome do poço:</b> {row['POCO']}<br>"
            popup_content += f"<b>Bacia:</b> {row['BACIA']}<br>"
            popup_content += f"<b>Tipo do poço:</b> {row['TIPO']}<br>"
            popup_content += f"<b>Profundidade:</b> {row['PROFUNDIDADE_SONDADOR_M']}<br>"
            popup_content += f"<h5><b>DADOS ACESSÓRIOS</b></h5>"
            if pd.notnull(row['AGP']):
                popup_content += f"<b>AGP:</b> {'Sim' if row['AGP'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['PC']):
                popup_content += f"<b>Perfil Composto:</b> {'Sim' if row['PC'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['SISMICA']):
                popup_content += f"<b>Sísmica do poço:</b> {'Sim' if row['SISMICA'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['GEOQUIMICA']):
                popup_content += f"<b>Geoquímica do poço:</b> {'Sim' if row['GEOQUIMICA'] == 'Existe' else 'Não'}<br>"
            if pd.notnull(row['ATINGIU_PRESAL']):
                popup_content += f"<b>Atingiu Pré-Sal?:</b> {'Sim' if row['ATINGIU_PRESAL'] == 'S' else 'Não'}<br>"
            popup_content += f"<h5><b>DADOS PRIMÁRIOS</b></h5>"
            popup_content += f"<b>COT:</b> <br>"
            popup_content += f"<b>Rock Eval:</b> <br>"
            popup_content += f"<b>Biomarcadores:</b> <br>"
            popup_content += f"<b>Geoquímica Inorgânica:</b> <br>"

            # Criar marcador com popup
            #marker = folium.Marker(
            #    [row['LATITUDE_BASE_DD'], 
            #     row['LONGITUDE_BASE_DD']],
            #    popup=folium.Popup(popup_content, 
            #                       lazy=True),
            #    icon=folium.Icon(color='red', 
            #                     icon='info-sign')
            #)

            # Criar marcador de círculos
            marker = folium.Circle(
                 [row['LATITUDE_BASE_DD'], 
                  row['LONGITUDE_BASE_DD']],
                 popup=folium.Popup(popup_content,
                                    max_width=1000,
                                    lazy=True),
                 color='yellow',
                 radius=1000,
                 fill=True,
            )

            # Adicionando marcadores na lista
            markers.append(marker)

        # Criar grupo para os marcadores
        pocos_group = folium.FeatureGroup(name='Pocos UFF', 
                                          show=True)
        for marker in markers:
            marker.add_to(pocos_group)

        # Retornando o grupo
        return pocos_group