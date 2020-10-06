""" 
# scrapy shell 'https://www.surf-report.com/meteo-surf/cap-gris-nez-s1108.html'
# scrapy shell 'https://www.surf-report.com/meteo-surf/france/'
# scrapy crawl SurfSpot

import scrapy
from scrapy import Request
from ..items import ArticleItem
import re

class ExampleSpider(scrapy.Spider):
    name = 'SurfSpot'
    allowed_domains = ['www.surf-report.com']
    start_urls = ['https://www.surf-report.com/meteo-surf/france/',
                  'https://www.surf-report.com/meteo-surf/france/?pageId=2'
                 ]
 
    def parse(self, response):
        #Différents liens peremettant l'accés aux infos sur les spots 
        links = response.css(".grid_1 .card-content .title").css('a::attr(href)').extract()
        i=0
        #Création d'url propre pour les liens 
        for url in links[:10]:
            links[i] = response.urljoin(url)
            i=i+1

        #Application de la fonction "parse_meteo" pour chaque liens     
        for link in links[:5]:
            yield response.follow(link, self.parse_meteo)
            
        
    def parse_meteo(self, response):
        #Extraction du nom du spot via la barre de recherche 
             
        #a = response.css("#searchQuery").extract()          
        #B = a[0].split('"')
        #name_spot =[]
        #name_spot = B[7].split(',')
        name_spot=response.css(".searchBarInputContainer").css("input::attr(placeholder)").extract()
        days = response.css(".forecast-tab").css(".title").css("b::text").extract()
        day_0 = days[0]
        day_1 = days[1]
        day_2 = days[2]
        day_3 = days[3]
        day_4 = days[4]
       
    
        #Récupération de toutes les tailles de swell et des intervalles entre les vaguez  
        swell_and_interval = response.css(".forecast-tab").css(".swell").css("span::text").extract()
        
        #Calcul des listes des tailles de swell à différentes heures (données pour 5 horaires différentes) et différents jours
        swell_one_day = []
        swell_by_day =[]
        x=0
        for j in range(1,6):
            
            x = x+10
            for i in range(-10+x,0+x): 
                if i%2 == 0:
                    swell_one_day.append(swell_and_interval[i])
                    
                    if i == 8 or i == 18 or i == 28 or i == 38 or i == 48 or i == 58 :
                        swell_by_day.append(swell_one_day)
                        swell_one_day=[]
      
    
        #Calcul des listes des intervalles de swell à différentes heures (5 horaires différentes) et différents jours (4 jours)
        interval_one_day = []
        interval_by_day =[]
        x=0
        for j in range(1,6):
            
            x = x+10
            for i in range(-10+x,0+x): 
                if i%2 != 0:
                    interval_one_day.append(swell_and_interval[i])
                    
                    if i == 9 or i == 19 or i == 29 or i == 39 or i == 49 or i == 59 :
                        interval_by_day.append(interval_one_day)
                        interval_one_day=[]

       #Récupération des températures de l'air par jour et heure 
        temp_air = response.css(".forecast-tab").css(".micro").css("span::text").extract()
        temp_air_one_day = []
        temp_air_by_day =[]
        x=0
        for j in range(1,6):
            
            x = x+5
            for i in range(-5+x,0+x): 
                temp_air_one_day.append(temp_air[i])

                if i == 4 or i == 9 or i == 14 or i == 19 or i == 24 or i == 39 :
                    temp_air_by_day.append(temp_air_one_day)
                    temp_air_one_day=[]
      
        #Récupération vitesse du vent par jour et heure 
        vitesse_vent = response.css(".forecast-tab").css(".wind").css("span::text").extract()
        vitesse_vent_one_day = []
        vitesse_vent_by_day =[]
        x=0
        for j in range(1,6):
            
            x = x+5
            for i in range(-5+x,0+x): 
                vitesse_vent_one_day.append(vitesse_vent[i])

                if i == 4 or i == 9 or i == 14 or i == 19 or i == 24 or i == 39 :
                    vitesse_vent_by_day.append(vitesse_vent_one_day)
                    vitesse_vent_one_day=[]
        
        
        #Calcule du temps qu'il fait grâce aux logos              
        weather = response.css(".forecast-tab").css(".weather").css("img::attr(alt)").extract()
        weather_one_day = []
        weather_by_day =[]
        x=0
        for j in range(1,6):
            
            x = x+5
            for i in range(-5+x,0+x): 
                weather_one_day.append(weather[i])

                if i == 4 or i == 9 or i == 14 or i == 19 or i == 24 or i == 39 :
                    weather_by_day.append(weather_one_day)
                    weather_one_day=[]
              
 #['Ciel couvert',
 #'Ciel peu nuageux',
 #'Ciel nuageux',
 #'Averses de grêle',
 #'Ciel très nuageux',
 #'Pluie et neige faible',
 #'Averses de pluie',
 #'Voile de nuages élevés',
 #'Averses de grésil',
 #'Ciel clair',
 #'Pluie faible']
        
        #Orientation du swell             
        orientation_swell = response.css(".forecast-tab").css(".swell").css("img::attr(alt)").extract()
        orientation_swell_one_day = []
        orientation_swell_by_day =[]
        x=0
        for j in range(1,6):
            
            x = x+5
            for i in range(-5+x,0+x): 
                orientation_swell_one_day.append(orientation_swell[i])

                if i == 4 or i == 9 or i == 14 or i == 19 or i == 24 or i == 39 :
                    orientation_swell_by_day.append(orientation_swell_one_day)
                    orientation_swell_one_day=[]
                    
        #Orientation du vent             
        orientation_wind = response.css(".forecast-tab").css(".wind").css("img::attr(alt)").extract()
        orientation_wind_one_day = []
        orientation_wind_by_day =[]
        
        x=0
        for j in range(1,6):
            x = x+5
            for i in range(-5+x,0+x): 
                orientation_wind_one_day.append(orientation_wind[i])

                if i == 4 or i == 9 or i == 14 or i == 19 or i == 24 or i == 39 :
                    orientation_wind_by_day.append(orientation_wind_one_day)
                    orientation_wind_one_day=[]
                                  
        
        yield ArticleItem(
                name_spot : name_spot,
                temp_air_by_day : temp_air_by_day, 
                interval_by_day : interval_by_day,
                swell_by_day : swell_by_day,
                vitesse_vent_by_day : vitesse_vent_by_day,
                weather_by_day : weather_by_day,
                orientation_wind_by_day : orientation_wind_by_day,
                orientation_swell_by_day : orientation_swell_by_day,
                day_0 : day_0,
                day_1 : day_1,
                day_2 : day_2,
                day_3 : day_3,
                day_4 : day_4,
            
            )    
        
        
""" 
        