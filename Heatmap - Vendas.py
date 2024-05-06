# coding: utf-8

#Bibliotecas
import pandas as pd
import plotly.express as px



#importando planilha e exibindo a base
base = pd.read_excel('Mapa.xlsx')
base



# Defina o token de acesso do Mapbox (no codigo oficial tem meu token, mas vou subir no Git com uma nomeação para as pessoas colocarem seus propios tokens)
token = 'Coloque_seu_token_aqui'
px.set_mapbox_access_token(token)

fig = px.density_mapbox(
    data_frame=base, 
    lat='Latitude',
    lon='Longitude',
    z='Vendas',
    radius=30,
    center=dict(lat=-23.700, lon=-46.5555),
    zoom=8,
    mapbox_style='satellite'
)

fig.show()





