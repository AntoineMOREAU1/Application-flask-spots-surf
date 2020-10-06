# scrapy shell 'https://www.surf-report.com/meteo-surf/cap-gris-nez-s1108.html'
# scrapy shell 'https://www.surf-report.com/meteo-surf/france/'
# scrapy crawl Spot2

import scrapy
from scrapy import Request
from ..items import ArticleItem
import re
import numpy as np

class ExampleSpider(scrapy.Spider):
    name = 'Spot2'
    allowed_domains = ['www.surf-report.com']
    start_urls = ['https://www.surf-report.com/meteo-surf/france/',
                  'https://www.surf-report.com/meteo-surf/france/?pageId=2'
                 ]


    def parse(self, response):
        all_links = {
            name:response.urljoin(url) for name,url in zip(
            response.css(".grid_1 .card-content .title").css('b::text').extract(),
            response.css(".grid_1 .card-content .title").css('a::attr(href)').extract()
            )
        }
       # x=0
        for link in all_links.values():
            #x=x+1
           # if x<10:
            yield Request(link, callback=self.meteo_parse)
                #print(link)
                
    def meteo_parse(self, response):
        for i in response.css(".container.white-protection"):

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
                        swell_one_day.append(float(swell_and_interval[i]))

                        if i == 8 or i == 18 or i == 28 or i == 38 or i == 48 or i == 58 :
                            swell_by_day.append(swell_one_day)
                            swell_one_day=[]
            
            swell_day_0 = round(np.mean(swell_by_day[0]),2)
            swell_day_1 = round(np.mean(swell_by_day[1]),2)
            swell_day_2 = round(np.mean(swell_by_day[2]),2)
            swell_day_3 = round(np.mean(swell_by_day[3]),2)
            swell_day_4 = round(np.mean(swell_by_day[4]),2)
            
            
            
            
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
                    temp_air_one_day.append(float(temp_air[i]))

                    if i == 4 or i == 9 or i == 14 or i == 19 or i == 24 or i == 39 :
                        temp_air_by_day.append(temp_air_one_day)
                        temp_air_one_day=[]
                        
            temp_air_day_0 = round(np.mean(temp_air_by_day[0]),2)
            temp_air_day_1 = round(np.mean(temp_air_by_day[1]),2)
            temp_air_day_2 = round(np.mean(temp_air_by_day[2]),2)
            temp_air_day_3 = round(np.mean(temp_air_by_day[3]),2)
            temp_air_day_4 = round(np.mean(temp_air_by_day[4]),2)                   
                        
                        

            #Récupération vitesse du vent par jour et heure 
            vitesse_vent = response.css(".forecast-tab").css(".wind").css("span::text").extract()
            vitesse_vent_one_day = []
            vitesse_vent_by_day =[]
            x=0
            for j in range(1,6):

                x = x+5
                for i in range(-5+x,0+x): 
                    vitesse_vent_one_day.append(float(vitesse_vent[i]))

                    if i == 4 or i == 9 or i == 14 or i == 19 or i == 24 or i == 39 :
                        vitesse_vent_by_day.append(vitesse_vent_one_day)
                        vitesse_vent_one_day=[]
                        
            vitesse_vent_day_0 = round(np.mean(vitesse_vent_by_day[0]),2)
            vitesse_vent_day_1 = round(np.mean(vitesse_vent_by_day[1]),2)
            vitesse_vent_day_2 = round(np.mean(vitesse_vent_by_day[2]),2)
            vitesse_vent_day_3 = round(np.mean(vitesse_vent_by_day[3]),2)
            vitesse_vent_day_4 = round(np.mean(vitesse_vent_by_day[4]),2)      

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
           #['Ciel couvert',#'Ciel peu nuageux',#'Ciel nuageux',#'Averses de grêle', #'Ciel très nuageux', #'Pluie et neige faible', #'Averses de pluie', #'Voile de nuages élevés',#'Averses de grésil',#'Ciel clair', #'Pluie faible']

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
        
            #Récupération de l'url de la page du spot
            url_brut_list = response.css(".menu-spot-container").css(".active").css('a::attr(href)').extract()
            url_brut_str = "".join(url_brut_list)
            url_clean_spot = response.urljoin(url_brut_str)     

                        
            yield ArticleItem(
                name_spot = name_spot,
                day_0 = day_0,
                day_1 = day_1,
                day_2 = day_2,
                day_3 = day_3,
                day_4 = day_4,
                swell_by_day = swell_by_day,
                interval_by_day = interval_by_day,
                vitesse_vent_by_day = vitesse_vent_by_day,
                weather_by_day = weather_by_day,
                orientation_swell_by_day = orientation_swell_by_day,
                orientation_wind_by_day = orientation_wind_by_day,
                temp_air_by_day = temp_air_by_day,
                swell_day_0 = swell_day_0,
                swell_day_1 = swell_day_1,
                swell_day_2 = swell_day_2,
                swell_day_3 = swell_day_3,
                swell_day_4 = swell_day_4,
                temp_air_day_0 = temp_air_day_0,
                temp_air_day_1 = temp_air_day_1,
                temp_air_day_2 = temp_air_day_2,
                temp_air_day_3 = temp_air_day_3,
                temp_air_day_4 = temp_air_day_4,
                vitesse_vent_day_0 = vitesse_vent_day_0,
                vitesse_vent_day_1 = vitesse_vent_day_1,
                vitesse_vent_day_2 = vitesse_vent_day_2,
                vitesse_vent_day_3 = vitesse_vent_day_3,
                vitesse_vent_day_4 = vitesse_vent_day_4,
                url_clean_spot = url_clean_spot,
                )
            
            
            