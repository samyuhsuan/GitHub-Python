# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:01:21 2017

@author: ylin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("movie_metadata.csv")

data.movie_title = data.movie_title.str.replace("\xa0", "")
data = data.drop("movie_imdb_link", axis=1)

#numerical and nonnumerical data columns
numeric = data._get_numeric_data().columns
non_numeric = list(set(data.columns) -  set(data._get_numeric_data().columns))
data[numeric].info()
data[non_numeric].info()

#identifying data level by their unique values per column 
levelLength=[]
levelName=[]
for column in data:
    g = len(data[column].unique())
    levelLength.append(g)
    levelName.append(column)
level = pd.DataFrame([levelName, levelLength])
level = level.transpose()
level.columns = ["Name", "UniqueValue"]
level = level.sort_values("UniqueValue", ascending=False)

#identifying amount of missing data by columns: object: missing
missingLength = []
missingName = []
for column in data:
    g = data[column][data[column].isnull() == True] 
    missingName.append(column)
    missingLength.append(len(g))
missing = pd.DataFrame(data=[missingName, missingLength])
missing = missing.transpose()
missing.columns = ["Name", "MissingValueLength"]
missing = missing.sort_values("MissingValueLength", ascending=False)

#merging missing and level
exam = level.merge(missing[["Name", "MissingValueLength"]], on="Name", how="left")

#drop duplicates of data 
data.drop_duplicates(subset="movie_title", keep="first", inplace=True)

#function dist() for the distribution of a specified column's levels
#this will sort bt the largest counts, to sort by index use .sort_index
def dist(g, h):
    temp = data[g].value_counts().reset_index()
    temp.columns = [g, "freq"]
    temp["percentage"] = temp.freq / np.sum(temp.freq)
    temp.percentage = temp.percentage.round(2)
    print(temp.sort_values(h, ascending=False))

dist("country", "freq")
dist("language", "freq")

data["num_voted_users"].value_counts()

plt.hist(data["num_voted_users"], bins=100)

pd.qcut(data.duration, 3).value_counts()
pd.qcut(data.title_year, 4).value_counts()
dist("duration", "freq")

data.corr()

exam[exam.Name.isin(numeric)]
exam[exam.Name.isin(non_numeric)]
     
data[data.country.isin(["Russia"])]
     
data[numeric]
     
data.info()

data.describe()

data[data._get_numeric_data().columns].head()



