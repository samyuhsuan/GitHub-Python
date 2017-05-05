# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:09:52 2017

@author: ylin
"""

import pandas as pd
import numpy as np

data = pd.read_csv("NextData2.csv")

data = data[data["Advertiser Currency"].isnull() == False]

data = data.loc[:, ['Date', 
       'Environment', 'Impressions',
       'Active View: Measurable Impressions',
       'Active View: Viewable Impressions', 'Clicks', 'Total Conversions',
       'Revenue (Adv Currency)']]