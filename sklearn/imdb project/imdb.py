# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:01:21 2017

@author: ylin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("movie_metadata.csv")

mcol = data.columns

data.info()

plt.plot(data.gross.sort_values(ascending=False).values)

for column in data:
    g = len(data[column].unique())
    print(column, g)

data.dtypes


for column in data:
    g = len(data[column].unique())
    print(column, g)

data["ratio"] = data.gross/data.budget

plt.plot(data.gross.sort_values(ascending=True))
plt.plot(data.gross.sort_values(ascending=False).values)

data.loc[data.gross.isnull() == True, "gross"] = np.mean(data.gross)

data.movie_title[data.ratio > 150]

data.movie_title.unique()

data.movie_title = data.movie_title.str.replace("\xa0", "")

data = data.drop_duplicates(subset="movie_title", keep="first")

data = data.drop("movie_imdb_link", axis=1)

data["profit"] = data.gross - data.budget

data.sort_values("profit", ascending=False)[["movie_title", "profit", "ratio"]]

data = data.loc[:, data.columns.sort_values(ascending=True)]

data.info()

data.country.sort_values(ascending=True).unique()


data["region"] = "N/A"
data.region.iloc[data.country == "USA"|'Canada', :] = "NorthAmerica"
data.region.iloc[data.country == "UK", :] = "UK"
data.region.iloc[data.country == 'Poland'|'Switzerland'|'Romania'|'Kyrgyzstan'|'Slovenia'|'Slovakia'|"Belgium" | "Hungary" | "Ireland" | 'Netherlands'| 'Spain'|'Italy'|'Germany'|'Greece'|'Czech Republic'|'France'| 'Georgia'|'Bulgaria'|'West Germany'| , :] = "EMEA"
data.region.iloc[data.country == 'South Korea'|'Taiwan'|'Thailand'|'China'|'Hong Kong'|'Japan'|'Philippines'|'Indonesia', :] = "ASIA"
data.region.iloc[data.country == 'Colombia'|'Mexico'|'Argentina'|'Dominican Republic'|'Chile'|'Cambodia'|'Brazil'|'Peru'|'Bahamas', :] = "SouthAmerica"
data.region.iloc[data.country == 'Iceland'|'Sweden'|'Denmark'|'Norway' , :] = "Nordic"
data.region.iloc[data.country == 'Iran'|'Libya'|'Pakistan'|'Afghanistan'|'Israel'|'Turkey', :] = "MiddleEast"
data.region.iloc[data.country == 'South Africa'|'Nigeria'|'Kenya'|'Egypt'| , :] = "Africa"
data.region.iloc[data.country == 'India', :] = "India"

[, , 'Aruba', 'Australia', 'Bahamas',
        , , , 'Cameroon', ,
       , , , , ,
       , ,  ,,
       , , , , ,
       , , , , , ,
       , , , , 'New Line',
       'New Zealand', , , 'Official site', ,
       'Panama', , , , , 'Russia',
       , , , ,
       'Soviet Union', , , , ,
       , ,  'United Arab Emirates',
       , nan]










