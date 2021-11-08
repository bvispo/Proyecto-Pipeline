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
    return pd.read_csv("Data/Smart_City_index.csv",encoding = "utf-8")

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


    #   API LIFE QUALITY

def lowercase (x):
    return x.lower()

def download_2():
    return smart.to_csv("Data/continent_smart.csv", index=False)