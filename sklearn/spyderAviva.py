# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:11:20 2017

@author: ylin
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Aviva.csv")
data = data.drop(['Exchange ID', 'Advertiser Currency'], axis=1)
data.columns = ['CW', 'CH', 'AdPosition', 'Exchange', 'Device', 'Impressions', 'mImpressions', 'vImpressions', 'Clicks', 'Conversions', 'Spend']

data.CW = data.CW.apply(str)
data.CH = data.CH.apply(str)


data["size"] = data.CW + "x" + data.CH

data["CTR"] = data.Clicks / data.Impressions
data["Viewability"] = data.vImpressions / data.mImpressions
data["CPM"] = data.Spend / data.Impressions * 1000
data["CPA"] = data.Spend / data.Conversions

averageCPA = np.sum(data.Spend) / np.sum(data.Conversions)

data.loc[data.CPA == np.inf, "CPA"] = averageCPA

data.head()

from sklearn.preprocessing import 

