import folium
import pandas as pd
import numpy as np
import csv
import folium, branca
import folium as features
import numpy
import plotly.graph_objs as go
import plotly
import plotly.express as px

import matplotlib.pyplot as plt
import random


dataset = pd.read_csv('spots.csv')
swell_day_0 = dataset['swell_day_0']
swell_day_1 = dataset['swell_day_1']
swell_day_2 = dataset['swell_day_2']
swell_day_3 = dataset['swell_day_3']
swell_day_4 = dataset['swell_day_4']

temp_air_day_0 = dataset['temp_air_day_0']
temp_air_day_1 = dataset['temp_air_day_1']
temp_air_day_2 = dataset['temp_air_day_2']
temp_air_day_3 = dataset['temp_air_day_3']
temp_air_day_4 = dataset['temp_air_day_4']



'''
# Etat du swell sur les différents spots pour les différents jours 
plt.hist(swell_day_0, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()

plt.hist(swell_day_1, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()

plt.hist(swell_day_2, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()

plt.hist(swell_day_3, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()

plt.hist(swell_day_4, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()


# Température de l'air les différents spots pour les différents jours 
plt.hist(temp_air_day_0, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()

plt.hist(temp_air_day_1, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()

plt.hist(temp_air_day_2, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()

plt.hist(temp_air_day_3, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()

plt.hist(temp_air_day_4, range = (0, 10), bins = 50, color = 'grey', edgecolor = 'red')
plt.xlabel('nombre de spots')
plt.ylabel('swell en métres ')
plt.title('nombre de spot en fonction du swell')
plt.show()
'''




import dash
import dash_core_components as dcc
import dash_html_components as html





histo1 = px.histogram( swell_day_0 , x = swell_day_0 )
histo_swell_day_0 = px.histogram( swell_day_0 , x = swell_day_0 )
histo_swell_day_0 = px.histogram( swell_day_0 , x = swell_day_0 )
histo_swell_day_0 = px.histogram( swell_day_0 , x = swell_day_0 )


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Projet anlayse de données en python'),
    html.H2(children='Contexte'),

    html.Div(children="""De nos jours, les immenses avancées technologiques et techniques dans de nombreux 
    domaines tel que le transport, la santé, l'énergie, l’informatique.... 
    """),
    html.Div(children="""Nous permettent d’améliorer notre niveau et notre confort de vie, 
    malgrès cela de nombreuses inégalitées subsistent 
    sur notre planète et de nombreux pays ne bénéficient pas de ces avancées.
        
    """),
    html.Div(children="""En effet de nombreux pays majoritairement sur le continent Africain ne bénéficie même pas des 
    infrastructures élémentaires tel que l'accès à l’eau potable, aux soins, ou à des services d’assainissements.
        
    """),
    html.Div(children="""A travers l’étude de données que j’ai effectuée j’ai souhaité mettre en évidence ces
     inégalités de moyens qu’il y’a entre les différents pays et les conséquences direct que celles-ci engendrent.
        
    """),
    
    html.H2(children='Graphiques'),
    dcc.Graph(
        id='histo1',
        figure=histo1,
    ),

])

app.run_server(debug=True)