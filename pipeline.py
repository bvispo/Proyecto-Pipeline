from src.cleaning_functions import *

#Cleaning
df_smart = load_csv()

dict_rename = {'Smart_Mobility ': 'Smart_Mobility',
          'Smart_Government ': 'Smart_Government',
          'Smart_Economy ': 'Smart_Economy'
          }

rename_columns (dict_rename)

drop_columns ()
download ()

#APIs
smart = load_csv_2()

smart = replace_country()

#API CONTINENTS
import requests
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("token")

url = "https://referential.p.rapidapi.com/v1/country"

querystring = {"fields":"currency,currency_num_code,currency_code,continent_code,currency,iso_a3,dial_code"}

headers = {
    'x-rapidapi-host': "referential.p.rapidapi.com",
    'x-rapidapi-key': token
    }

response = requests.request("GET", url, headers=headers, params=querystring)

continent ()
smart["Continent"] = smart["Country"].apply(continent)

#cómo hacer esto de una?
smart["Continent"] = smart["Continent"].str.replace("NA", "North America")
smart["Continent"] = smart["Continent"].str.replace("OC", "Oceania")
smart["Continent"] = smart["Continent"].str.replace("EU", "Europe")
smart["Continent"] = smart["Continent"].str.replace("AS", "Asia")

#API LIFE QUALITY

lowercase ()
cities = smart["City"] = smart["City"].apply(lowercase)

scores =[]
for city in cities:
    try: 
        response = requests.get(f"https://api.teleport.org/api/urban_areas/slug:{city}/scores/").json()
        scores.append(response["teleport_city_score"])
    except:
        print(city)
        scores.append(np.nan)

dic_quality = {}
for i in range (len(cities)):
    dic_quality.update({cities[i]:scores[i]})

smart["Life_Quality"]= smart["City"].map(dic_quality)

download_2 ()


