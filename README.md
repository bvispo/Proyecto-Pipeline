# Proyect-Pipeline

## Alt-Objective and hypotheis

### Objective
The objective of this proyect is learn to combine various types of tools in order o get insightfull data, from a dataset and APIs.

### Hyphothesis:
The better puncuation a city has in a quality of life index, the better it ill be positioned among the worldwide smart-city index. On the contrary, those that have worse life quality, would stand out the ranking.

## Alt-Smart Cities Index Data from Kaggle

In order to get the data, I have used a Kaggle dataset based on a recopilation of globally-recognized indexes (formalized for the evaluation of Smart City initiatives). for the year 2020.
Data available at: https://www.kaggle.com/magdamonteiro/smart-cities-index-datasets

This dataset contains several columns describing smart cities index around the world in 2020. This file contains 102 columns, which are those included in the smart 2020 worldwide smart-city index, and 10 columns where we can find the smart city name, its country and the differernt indexes based on movility, environment, government,economy,living and people.

## Alt-API-Continents
This API provides information about cities and their continents. This will allow us to go further on our data and check which continents are more developed, in terms of smart cities.


## Alt-API-Life Quality
The first API used, provides scores for housing, cost of living, startups, venture capital, travel connectivity, commute, business freedom, safety, healthcare, education, environmental quality, economy, taxation and internet access. All the latter information is summed in the "teleport_city_score", which will be added to the dataset in order to enrich the data.



## Results



## Libraries

import requests: https://pypi.org/project/requests/2.7.0/

import pandas as pd: https://pandas.pydata.org/

import numpy as np: https://numpy.org/doc/

import matplotlib.pyplot as plt: https://matplotlib.org/3.1.1/contents.html

import seaborn as sns: https://seaborn.pydata.org/