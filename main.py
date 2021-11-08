# This are the libraries used:
import numpy as np 
import pandas as pd


# Notebook: 1.Cleaning Smart Cities:

def load_csv():
    return pd.read_csv("../data/Smart_City_index.csv",encoding = "ISO-8859-1")

df_smart = load_csv

def rename_columns (dict_rename):
    return df_smart.rename(columns=dict_rename, inplace=True)

def drop_columns ():
    return df_smart.drop(["Id", "SmartCity_Index_relative_Edmonton"], axis=1, inplace=True)

def download ():
    return df_smart.to_csv("../data/clean_smart.csv")



