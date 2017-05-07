# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:09:52 2017

@author: ylin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.read_csv("NextData2.csv")

data = data[data["Advertiser Currency"].isnull() == False]

data = data.loc[:, ['Date', 
       'Environment', 'Impressions',
       'Active View: Measurable Impressions',
       'Active View: Viewable Impressions', 'Clicks', 'Total Conversions',
       'Revenue (Adv Currency)']]

data.columns = ['Date', 
       'Environment', 'Impressions',
       'mImpressions','vImpressions', 'Clicks', 'Conversions',
       'Spend']

data["CTR"] = data.Clicks / data.Impressions
data["Viewability"] = data.vImpressions / data.mImpressions
data["CPA"] = data.Spend / data.Conversions


data = data[data.Impressions != 0]

X = data.loc[0:1349, ['Environment', 'Viewability']].values
y = data.loc[0:1349, "CTR"].values


from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN", strategy="mean", axis = 0)

imputer = imputer.fit(X[:, 1:2])

X[:, 1:2] = imputer.transform(X[:,1:2])

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

X[:,0] = LabelEncoder().fit_transform(X[:,0])

dummy = OneHotEncoder(categorical_features=[0])

X = dummy.fit_transform(X).toarray()

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression().fit(X_train, y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_test[:, 2], y_pred)
plt.scatter(X_test[:, 2], y_test, color="Red")
plt.show()

plt.scatter(X_test[:, 1], y_pred)
plt.scatter(X_test[:, 1], y_test, color="Red")
plt.show()

plt.scatter(X_test[:, 0], y_pred)
plt.scatter(X_test[:, 0], y_test, color="Red")
plt.show()

import statsmodels.formula.api as sm

X = np.append(arr=np.ones((len(X[:,0]), 1)).astype(int), values = X, axis=1)

X_opt = X

sm.OLS(endog=y, exog=X_opt).fit().summary()


