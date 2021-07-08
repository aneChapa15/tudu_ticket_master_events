#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math 
from dataclasses import dataclass
import requests
import json
import os
import urllib
import urllib.request
import unidecode

family = []#classifications 0 family
segment = []#classifications 0 segment name
genre = [] #subcategoria
event_name = []#name
location = []#location
event_type = []#type
url = []#url
address = []#_embedded venues 0 address line1
city = []#_embedded venues 0 city name
state = []#["_embedded"]["venues"][0]["state"]["name"]
country = []#_embedded venues 0 country name
venue_name = []#_embedded venues 0 name
date = []#dates start localDate
time = []#dates start localTime
status = []#dates status code
currency = []#priceRanges 0 currency
max_price = []#priceRanges 0 max
min_price = []#priceRanges 0 min
idLugar = []#_embedded venues 0 id
descripcion = []#info
phone_number = []#_embedded venues 0 boxOfficeInfo phoneNumberDetail
facebook = []#["_embedded"]["attractions"][0]["externalLinks"]["facebook"]
homepage = []
latitude = []#["_embedded"]["venues"][0]["location"]["latitude"]
longitude = []#["_embedded"]["venues"][0]["location"]["longitude"]
images_1 = []#["_embedded"]["events"][0]["images"]
images_2 = []#["_embedded"]["events"][1]["images"]
images_3 = []#["_embedded"]["events"][2]["images"]
images_4 = []
images_5 = []
images_6 = []
images_7 = []
images_8 = []
images_9 = []
images_10 = []
event_id = []#["_embedded"]["events"][0]["id"]
my_top_directory_path = "C:/DevION/Projects/tudu_get_events/"

# locations
locations = pd.read_csv(my_top_directory_path + "locations.csv")
locations_latitude  = locations["lat"]
locations_longitude = locations["long"]

categories = pd.read_csv(my_top_directory_path + "categories.csv")
my_categories  = categories["category"]
all_my_events_data = []
base_url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey=IBTP659NotGYFqF1RE2xbbHrMufUVmhH"

my_old_events_csv = pd.read_csv(my_top_directory_path + "events_old.csv")
old_list_of_ids = my_old_events_csv["id"]

for idx in range(len(locations_latitude)):
    my_location = str(locations_latitude[idx])+","+str(locations_longitude[idx])
    print(my_location)
    for idy in range(len(my_categories)) :     
        params = {
            #"city": ["México, DF", "Ciudad de Mexico", "cdmx"],
            "latlong": my_location,
            "countryCode": "MX",
            "classificationName":  my_categories[idy],
            "size":99,
            #"startDateTime": "2021-06-15T00:00:00Z",
            #"keyword":"Sports",
            #"endDateTime": "2020-11-19T00:00:00Z"
            #"apikey": api_key
        }
        response = requests.get(base_url,params=params)
        events_data = response.json()
        all_my_events_data.append(events_data)
        print(my_categories[idy])  
        #response = requests.get(base_url, params=params)
        # convert response to json

my_list_of_ids = []            
            
json_object = json.dumps(all_my_events_data, indent = 4)
with open(my_top_directory_path + "my_json_output.json", "w") as outfile:
    outfile.write(json_object)        

#loop for all locations saved
for event in all_my_events_data :
    #loop for all events per location
    for e in event["_embedded"]["events"]:
        found_a_duplicate = False
        my_id = e["id"].lower()
        for i in old_list_of_ids :
            if (my_id == i.lower()):
                found_a_duplicate = True
        for i in my_list_of_ids:
            if (my_id == i.lower()):
                found_a_duplicate = True
        if(not(found_a_duplicate)): 
            my_list_of_ids.append(str(my_id.lower()))
            location.append(e["_embedded"]["venues"][0]["city"]["name"])
            event_name.append(e["name"])
            event_type.append(e["type"])
            segment.append(e["classifications"][0]["segment"]["name"])
            genre.append(e["classifications"][0]["genre"]["name"])
            family.append(e["classifications"][0]["family"])
            url.append(e["url"])
            address.append(e["_embedded"]["venues"][0]["address"]["line1"])
            city.append(e["_embedded"]["venues"][0]["city"]["name"])
            state.append(e["_embedded"]["venues"][0]["state"]["name"])
            country.append(e["_embedded"]["venues"][0]["country"]["name"])
            venue_name.append(e["_embedded"]["venues"][0]["name"])
            date.append(e["dates"]["start"]["localDate"])
            #time.append(e["dates"]["start"]["localTime"])
            status.append(e["dates"]["status"]["code"])
            event_id.append(my_id)
            idLugar.append(e["_embedded"]["venues"][0]["id"])
            latitude.append(e["_embedded"]["venues"][0]["location"]["latitude"])
            longitude.append(e["_embedded"]["venues"][0]["location"]["longitude"])

            images_1.append(e["images"][0]["url"])
            images_2.append(e["images"][1]["url"])
            images_3.append(e["images"][2]["url"])
            images_4.append(e["images"][3]["url"])
            images_5.append(e["images"][4]["url"])
            images_6.append(e["images"][5]["url"])
            images_7.append(e["images"][6]["url"])
            images_8.append(e["images"][7]["url"])
            images_9.append(e["images"][8]["url"])
            images_10.append(e["images"][9]["url"])

            #generate a directory for this location to save 10 images 
           #newpath = my_top_directory_path + "images/" + ''.join(filter(str.isalnum, unidecode.unidecode(location[-1]).strip())) + \
           #           "/"+''.join(filter(str.isalnum, unidecode.unidecode(event_name[-1]).strip()))
            newpath = my_top_directory_path + "images/"
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            image_1_name = os.path.join(newpath, event_id[-1]+"_a.jpg")
           # urllib.request.urlretrieve(images_1[-1], image_1_name)
            image_2_name = os.path.join(newpath, event_id[-1]+"_b.jpg")
           # urllib.request.urlretrieve(images_2[-1], image_2_name)
            image_3_name = os.path.join(newpath, event_id[-1]+"_c.jpg")
           # urllib.request.urlretrieve(images_3[-1], image_3_name)
            image_4_name = os.path.join(newpath, event_id[-1]+"_d.jpg")
           # urllib.request.urlretrieve(images_4[-1], image_4_name)
            image_5_name = os.path.join(newpath, event_id[-1]+"_e.jpg")
           # urllib.request.urlretrieve(images_5[-1], image_5_name)
            image_6_name = os.path.join(newpath, event_id[-1]+"_f.jpg")
           # urllib.request.urlretrieve(images_6[-1], image_6_name)
            image_7_name = os.path.join(newpath, event_id[-1]+"_g.jpg")
           # urllib.request.urlretrieve(images_7[-1], image_7_name)
            image_8_name = os.path.join(newpath, event_id[-1]+"_h.jpg")
           # urllib.request.urlretrieve(images_8[-1], image_8_name)
            image_9_name = os.path.join(newpath, event_id[-1]+"_i.jpg")
           # urllib.request.urlretrieve(images_9[-1], image_9_name)
            image_10_name = os.path.join(newpath, event_id[-1]+"_j.jpg")
           # urllib.request.urlretrieve(images_10[-1], image_10_name)
            print("getting images for event: "+event_name[-1])
            
            try:
                time.append(e["dates"]["start"]["localTime"])
            except:
                time.append("null")
            try:
                currency.append(e["priceRanges"][0]["currency"])
            except:
                currency.append("null")
            try:
                max_price.append(e["priceRanges"][0]["max"])
            except:
                max_price.append("null")
            try:
                min_price.append(e["priceRanges"][0]["min"])
            except:
                min_price.append("null")
            try:
                descripcion.append(e["info"])
            except:
                descripcion.append("null")
            try:
                phone_number.append(e["_embedded"]["venues"][0]["boxOfficeInfo"]["phoneNumberDetail"])
            except:
                phone_number.append("null")
            try:
                facebook.append(e["_embedded"]["attractions"][0]["externalLinks"]["facebook"])
            except:
                facebook.append("null")
            try:
                homepage.append(e["_embedded"]["attractions"][0]["externalLinks"]["homepage"])
            except:
                homepage.append("null") 

events_info = pd.DataFrame({
    "location":location,
    "id":event_id,
    "IdLugar":idLugar,
    "Nombre":event_name,
    "Descripcion":descripcion,
    "Direccion":address,
    "Municipio":city,
    "Estado":state,
#    "Telefono":phone_number,
    "Facebook":facebook,
    "homepage":homepage,
    "Latitud":latitude,
    "Longitud":longitude,
    "websitecontact":url,
    "Categoria":segment,
    "Genero": genre,
    #"Email contact":"opina@ticketmaster.com.mx",
    #"Website contact":url,
    "Fecha":date,
    "Hora":time,
    "Lugar":venue_name,
#    "Imagenes":images
#     "event_type":event_type,
#     "family":family,
#     "url":url,
#     "country":country,
#     "status":status,
#     "currency":currency,
#     "max_price":max_price,
#     "min_price":min_price
})
events_info.to_csv(my_top_directory_path + "events.csv", index = False)