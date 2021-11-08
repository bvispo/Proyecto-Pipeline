# This are the libraries used:
import numpy as np 
import pandas as pd
import requests
from pandas import json_normalize
import numpy as np 
import pandas as pd
import os


# Notebook: 1.Cleaning Smart Cities:

def load_csv():
    return pd.read_csv("../Data/Smart_City_index.csv",encoding = "utf-8")

df_smart = load_csv()

def rename_columns (dict_rename):
    return df_smart.rename(columns=dict_rename, inplace=True)

def drop_columns ():
    return df_smart.drop(["Id", "SmartCity_Index_relative_Edmonton"], axis=1, inplace=True)

def download ():
    df_smart.to_csv("Data/clean_smart.csv")


# Notebook: 2.Cleaning APIs

def load_csv_2():
    return pd.read_csv("Data/clean_smart.csv", encoding = "utf-8")

smart = load_csv_2

def replace_country():
    return smart["Country"].str.replace("United States", "United States Of America")

    #  API CONTINENT:

def continent(country):
    for dicc in response.json():
        if country == "China":
            return "AS"
        elif country == dicc["value"]:
            return dicc["continent_code"]

#cómo hacer esto de una?    
smart["Continent"] = smart["Continent"].str.replace("NA", "North America")
smart["Continent"] = smart["Continent"].str.replace("OC", "Oceania")
smart["Continent"] = smart["Continent"].str.replace("EU", "Europe")
smart["Continent"] = smart["Continent"].str.replace("AS", "Asia")

    #   API LIFE QUALITY

def lowercase (x):
    return x.lower()

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


def download():
    return smart.to_csv("../data/continent_smart.csv", index=False)