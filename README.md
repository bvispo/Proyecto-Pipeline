# Proyect-Pipeline


![foto](https://github.com/bvispo/Proyecto-Pipeline/blob/main/images/smartcity.jpg)

## Objective and hypotheis

### Objective
The objective of this proyect is learn to combine various types of tools in order to get insightfull data, from a dataset and APIs.

### Hyphothesis:
The better puncuation a city has in a Life Quality index, the better it will be positioned among the worldwide Smart City index. On the contrary, those that have worse life quality, would stand at the bottom of the ranking.

## Smart Cities Index Data from Kaggle

In order to get the data, I have used a Kaggle dataset based on a recopilation of globally-recognized indexes (formalized for the evaluation of Smart City initiatives). for the year 2020.
Data available at: [Smart City Index](https://www.kaggle.com/magdamonteiro/smart-cities-index-datasets)

This dataset contains several columns describing the Smart City worldwide index in 2020. This file contains 102 columns, which are those included in the 2020 worldwide Smart City index, and 10 columns where we can find the smart city name, its country and the differernt indexes based on movility, environment, government,economy,living and people.

## API: Continents
This API provides information about cities and their continents. This will allow us to go further on our data and check which continents are more developed, in terms of smart cities.
API available at: [API Continents](https://rapidapi.com/referential/api/referential/ 
)  

## API: Life Quality
ThIS API, provides scores for housing, cost of living, startups, venture capital, travel connectivity, commute, business freedom, safety, healthcare, education, environmental quality, economy, taxation and internet access. All the latter information is summed up in the "teleport_city_score", which will be added to the dataset as "Life_Quality" in order to enrich the data.

API available at: [Api Life Quality](https://developers.teleport.org/api/)


## Results

The Life Quality does infer in the position the city has on the Smart City worldwide index.


## Libraries

[import requests](https://pypi.org/project/requests/2.7.0/)

[import pandas as pd](https://pandas.pydata.org/)

[import numpy as np](https://numpy.org/doc/)

[import matplotlib.pyplot as plt](https://matplotlib.org/3.1.1/contents.html)

[import seaborn as sns](https://seaborn.pydata.org/)