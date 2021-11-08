from cleaning_apis import load_csv_2
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

#AQUI HAY QUE METER LA LLAMADA A LA API??????

smart["Continent"] = smart["Country"].apply(continent)

#cómo hacer esto de una?
smart["Continent"] = smart["Continent"].str.replace("NA", "North America")
smart["Continent"] = smart["Continent"].str.replace("OC", "Oceania")
smart["Continent"] = smart["Continent"].str.replace("EU", "Europe")
smart["Continent"] = smart["Continent"].str.replace("AS", "Asia")

#API LIFE QUALITY
cities = smart["City"] = smart["City"].apply(cf.lowercase)

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
