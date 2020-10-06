from flask import Flask, redirect, url_for
from flask import render_template, render_template_string, request
from jinja2 import Template

from pymongo import MongoClient
from elasticsearch import Elasticsearch
from flask_pymongo import PyMongo

import pprint

import dash
import dash_core_components as dcc
import dash_html_components as html

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ScrapSurfSpot.ScrapSurfSpot.spiders import Spot2
from ScrapSurfSpot.scraper import Scraper

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


import os


client = MongoClient("0.0.0.0:27018") 
database_spot = client.spotSurf
database_spot['scrapy_items'].drop()
collection = database_spot['scrapy_items']

#Supression du fichier csv  
if os.path.exists('spots.csv'):
    os.remove('spots.csv')
   

app = Flask(__name__) 

scraper = Scraper()
scraper.run_spider()

dash_app_0 = dash.Dash(__name__, server=app, routes_pathname_prefix = '/dash_0/') 
dash_app_1 = dash.Dash(__name__, server=app, routes_pathname_prefix = '/dash_1/')
dash_app_2 = dash.Dash(__name__, server=app, routes_pathname_prefix = '/dash_2/') 
dash_app_3 = dash.Dash(__name__, server=app, routes_pathname_prefix = '/dash_3/')
dash_app_4 = dash.Dash(__name__, server=app, routes_pathname_prefix = '/dash_4/')


############# DASHBOARD ###################
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

vitesse_vent_day_0 = dataset['vitesse_vent_day_0']
vitesse_vent_day_1 = dataset['vitesse_vent_day_1']
vitesse_vent_day_2 = dataset['vitesse_vent_day_2']
vitesse_vent_day_3 = dataset['vitesse_vent_day_3']
vitesse_vent_day_4 = dataset['vitesse_vent_day_4']


#Histogrammes day 0
histo_swell_day_0 = px.histogram( swell_day_0, x = swell_day_0,  nbins=15,labels={'x': 'Tailles du swell en mètres'},title="Histogramme des tailles de swell selon les spots")
histo_temp_air_day_0 = px.histogram( temp_air_day_0, x = temp_air_day_0,nbins=15,labels={'x': "température de l'air en °C "},title='Histogramme des températures en fonction des spots')
histo_vitesse_vent_day_0 = px.histogram( vitesse_vent_day_0, x = vitesse_vent_day_0, nbins=15,labels={'x': 'vitesse du vents en km/h'},title='Histogramme des vitesses de vent en fonction des spots')

#Histogrammes day 1
histo_swell_day_1 = px.histogram( swell_day_1, x = swell_day_1,  nbins=15,labels={'x': 'Tailles du swell en mètres'},title="Histogramme des tailles de swell selon les spots")
histo_temp_air_day_1 = px.histogram( temp_air_day_1, x = temp_air_day_1,nbins=15,labels={'x': "température de l'air en °C "},title='Histogramme des températures en fonction des spots')
histo_vitesse_vent_day_1 = px.histogram( vitesse_vent_day_1, x = vitesse_vent_day_1, nbins=15,labels={'x': 'vitesse du vents en km/h'},title='Histogramme des vitesses de vent en fonction des spots')

#Histogrammes day 2
histo_swell_day_2 = px.histogram( swell_day_2, x = swell_day_2,  nbins=15,labels={'x': 'Tailles du swell en mètres'},title="Histogramme des tailles de swell selon les spots")
histo_temp_air_day_2 = px.histogram( temp_air_day_2, x = temp_air_day_2,nbins=15,labels={'x': "température de l'air en °C "},title='Histogramme des températures en fonction des spots')
histo_vitesse_vent_day_2 = px.histogram( vitesse_vent_day_2, x = vitesse_vent_day_2, nbins=15,labels={'x': 'vitesse du vents en km/h'},title='Histogramme des vitesses de vent en fonction des spots')

#Histogrammes day 3
histo_swell_day_3 = px.histogram( swell_day_3, x = swell_day_3,  nbins=15,labels={'x': 'Tailles du swell en mètres'},title="Histogramme des tailles de swell selon les spots")
histo_temp_air_day_3 = px.histogram( temp_air_day_3, x = temp_air_day_3,nbins=15,labels={'x': "température de l'air en °C "},title='Histogramme des températures en fonction des spots')
histo_vitesse_vent_day_3 = px.histogram( vitesse_vent_day_3, x = vitesse_vent_day_3, nbins=15,labels={'x': 'vitesse du vents en km/h'},title='Histogramme des vitesses de vent en fonction des spots')

#Histogrammes day 4
histo_swell_day_4 = px.histogram( swell_day_4, x = swell_day_4,  nbins=15,labels={'x': 'Tailles du swell en mètres'},title="Histogramme des tailles de swell selon les spots")
histo_temp_air_day_4 = px.histogram( temp_air_day_4, x = temp_air_day_4,nbins=15,labels={'x': "température de l'air en °C "},title='Histogramme des températures en fonction des spots')
histo_vitesse_vent_day_4 = px.histogram( vitesse_vent_day_4, x = vitesse_vent_day_4, nbins=15,labels={'x': 'vitesse du vents en km/h'},title='Histogramme des vitesses de vent en fonction des spots')


dash_app_0.layout = html.Div(children=[
    html.H1(children='Aperçu des conditions sur les différents spots en France '),

    html.Div(children="""Afin d’affiner vos recherches dans le choix de votre spot voici 
    un aperçu des conditions sur les différents spots en France.  
    """),
    
    html.H2(children=''),
    dcc.Graph(
        id='histo_swell_day_0',
        figure=histo_swell_day_0,
    ),

    html.H2(children=''),
    dcc.Graph(
        id='histo_temp_air_day_0',
        figure=histo_temp_air_day_0,
    ),
    html.H2(children=''),
    dcc.Graph(
        id='histo_vitesse_vent_day_0',
        figure=histo_vitesse_vent_day_0,
    ),
])

dash_app_1.layout = html.Div(children=[
    html.H1(children='Aperçu des conditions sur les différents spots en France '),

    html.Div(children="""Afin d’affiner vos recherches dans le choix de votre spot voici 
    un aperçu des conditions sur les différents spots en France.  
    """),
    
    html.H2(children=''),
    dcc.Graph(
        id='histo_swell_day_1',
        figure=histo_swell_day_1,
    ),

    html.H2(children=''),
    dcc.Graph(
        id='histo_temp_air_day_1',
        figure=histo_temp_air_day_1,
    ),
    html.H2(children=''),
    dcc.Graph(
        id='histo_vitesse_vent_day_1',
        figure=histo_vitesse_vent_day_1,
    ),
])

dash_app_2.layout = html.Div(children=[
    html.H1(children='Aperçu des conditions sur les différents spots en France '),

    html.Div(children="""Afin d’affiner vos recherches dans le choix de votre spot voici 
    un aperçu des conditions sur les différents spots en France.  
    """),
    
    html.H2(children=''),
    dcc.Graph(
        id='histo_swell_day_2',
        figure=histo_swell_day_2,
    ),

    html.H2(children=''),
    dcc.Graph(
        id='histo_temp_air_day_2',
        figure=histo_temp_air_day_2,
    ),
    html.H2(children=''),
    dcc.Graph(
        id='histo_vitesse_vent_day_2',
        figure=histo_vitesse_vent_day_2,
    ),
])

dash_app_3.layout = html.Div(children=[
    html.H1(children='Aperçu des conditions sur les différents spots en France '),

    html.Div(children="""Afin d’affiner vos recherches dans le choix de votre spot voici 
    un aperçu des conditions sur les différents spots en France.  
    """),
    
    html.H2(children=''),
    dcc.Graph(
        id='histo_swell_day_3',
        figure=histo_swell_day_3,
    ),

    html.H2(children=''),
    dcc.Graph(
        id='histo_temp_air_day_3',
        figure=histo_temp_air_day_3,
    ),
    html.H2(children=''),
    dcc.Graph(
        id='histo_vitesse_vent_day_3',
        figure=histo_vitesse_vent_day_3,
    ),
])

dash_app_4.layout = html.Div(children=[
    html.H1(children='Aperçu des conditions sur les différents spots en France '),

    html.Div(children="""Afin d’affiner vos recherches dans le choix de votre spot voici 
    un aperçu des conditions sur les différents spots en France.  
    """),
    
    html.H2(children=''),
    dcc.Graph(
        id='histo_swell_day_4',
        figure=histo_swell_day_4,
    ),

    html.H2(children=''),
    dcc.Graph(
        id='histo_temp_air_day_4',
        figure=histo_temp_air_day_4,
    ),
    html.H2(children=''),
    dcc.Graph(
        id='histo_vitesse_vent_day_4',
        figure=histo_vitesse_vent_day_4,
    ),
])
############# DASHBOARD ###################



@app.route('/')
def accueil():
    documents = collection.find({'swell_day_0':  {'$gt':0}})
    response = []

    for document in documents:
        response.append(document) 

    return render_template('index.html', spot = response)

@app.route('/spot_choice', methods=['GET', 'POST'])
def spot_choice():
    documents = collection.find({'swell_day_0':  {'$gt':0}})
    response_1 = []
    i=0

    for document in documents:
        response_1.append(document)       
        response_1[i]['name_spot'] = "".join(response_1[i]['name_spot'])
        i= i +1 

    if request.method == 'POST':
        vague_select = request.form.get('vague_select')
        air_select = request.form.get('air_select')
        day_select = request.form.get('day_select')
        wind_select = request.form.get('wind_select')
        day_0 = False
        day_1 = False
        day_2 = False
        day_3 = False
        day_4 = False

        if day_select == "day_0" :
            documents = collection.find({'swell_day_0':  {'$gte':float(vague_select)}, 'temp_air_day_0':  {'$gte':float(air_select)}, 'vitesse_vent_day_0':  {'$lte':float(wind_select)}})        
            response = []
            day_0 = True
            i=0
            for document in documents:
                response.append(document)   
                response[i]['name_spot'] = "".join(response[i]['name_spot'])
                i= i +1 

        elif day_select == "day_1" :
            documents = collection.find({'swell_day_1':  {'$gte':float(vague_select)}, 'temp_air_day_1':  {'$gte':float(air_select)}, 'vitesse_vent_day_1':  {'$lte':float(wind_select)}})        
            response = []
            day_1 = True
            i=0
            for document in documents:
                response.append(document)   
                response[i]['name_spot'] = "".join(response[i]['name_spot'])
                i= i +1 
        elif day_select == "day_2" :
            documents = collection.find({'swell_day_2':  {'$gte':float(vague_select)}, 'temp_air_day_2':  {'$gte':float(air_select)}, 'vitesse_vent_day_2':  {'$lte':float(wind_select)}})        
            response = []
            day_2 = True
            i=0
            for document in documents:
                response.append(document) 
                response[i]['name_spot'] = "".join(response[i]['name_spot'])
                i= i +1 
        elif day_select == "day_3" :
            documents = collection.find({'swell_day_3':  {'$gte':float(vague_select)}, 'temp_air_day_3':  {'$gte':float(air_select)}, 'vitesse_vent_day_3':  {'$lte':float(wind_select)}})        
            response = []
            day_3 = True
            i=0
            for document in documents:
                response.append(document) 
                response[i]['name_spot'] = "".join(response[i]['name_spot'])
                i= i +1 
        elif day_select == "day_4" :
            documents = collection.find({'swell_day_4':  {'$gte':float(vague_select)}, 'temp_air_day_4':  {'$gte':float(air_select)}, 'vitesse_vent_day_4':  {'$lte':float(wind_select)}})        
            response = []
            day_4 = True
            i=0
            for document in documents:
                response.append(document) 
                response[i]['name_spot'] = "".join(response[i]['name_spot'])
                i= i +1 
        return render_template('choose_spot.html', spot2 = response, spot = response_1, day_select = day_select, day_0= day_0, day_1= day_1, day_2= day_2, day_3= day_3, day_4= day_4,)
   
    else :
        documents = collection.find({'swell_day_0':  {'$gt':3}} )
        response = []
        i=0

        for document in documents:
            response.append(document)   
            response[i]['name_spot'] = "".join(response[i]['name_spot'])
            i= i +1 
        return render_template('choose_spot.html', spot = response_1, spot2=response)
    
if __name__ == "__main__":
    app.run(debug=True, port=2700, use_reloader= False)

