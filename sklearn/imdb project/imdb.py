# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:01:21 2017

@author: ylin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movie = pd.read_csv("movie_metadata.csv")

mcol = movie.columns

movie.info()

plt.plot(movie.gross.sort_values(ascending=False).values)

movie.info()

from sklearn 