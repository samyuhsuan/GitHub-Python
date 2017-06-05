# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:01:21 2017

@author: ylin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import Imputer

data = pd.read_csv("movie_metadata.csv")

data.movie_title = data.movie_title.str.replace("\xa0", "")
data = data.drop("movie_imdb_link", axis=1)

#numerical and nonnumerical data columns
numeric = data._get_numeric_data().columns
non_numeric = list(set(data.columns) -  set(data._get_numeric_data().columns))

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
#numerical and non-numerical for exam
exam_num = exam[exam.Name.isin(numeric)]
exam_cat = exam[exam.Name.isin(non_numeric)]

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


#------below dealing with this specific dataset-------
    
exam_num   

#converting some categorical data that is translated as numerical data
data.title_year = data.title_year.astype("category")
for name in non_numeric:
    data[name] = data[name].astype("category")

#recategorise some numerical columns to non_numerical 
numeric = numeric - ["title_year"]
non_numeric = non_numeric + ["title_year"]
#and rerun exam_num and exam_cat
exam_num = exam[exam.Name.isin(numeric)]
exam_cat = exam[exam.Name.isin(non_numeric)]

#dealing with categorical data
#firstly title year, separate that into 4 bins 
data["title_year_c"] = np.nan
data["title_year_c"] = pd.qcut(data.title_year, 4)
#reorganise content_rating 
#using ~ to take out not in the majority
data["content_rating_c"] = "Others"
data.content_rating_c[data.content_rating.isin(["Unrated", "Not Rated"])] = "Not Rated"
data.content_rating_c[data.content_rating.isin(["TV-PG", "TV-14"])] = "PG"
data.content_rating_c[(~data.content_rating.isin(["R", "PG-13", "PG", "Approved", "TV-MA"])) & (~data.content_rating_c.isin(["PG", "Not Rated"]))] = "Others"
data.content_rating_c[data.content_rating.isin(["R", "PG-13", "PG", "Approved", "TV-MA"])] = data.content_rating
#taking care of country
data["country_c"] = "Others"
data.country_c[data.country.isin(["USA", "UK", "France", "Canada", "Germany", "Australia", "India", "Spain", "Chinae"])] = data.country 
#taking care of language
data["language_c"] = "Others"
data.language_c[data.language.isin(["English"])] = "English"

exam_num
exam_cat



dist("language", "freq")

dist("language_c", "freq")

dist("actor_1_name", "freq")



data[["budget", "gross", "imdb_score"]].corr()



















