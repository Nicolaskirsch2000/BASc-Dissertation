# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:26:11 2020

@author: Kirsch
"""

import pandas as pd
import datetime
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


df = pd.read_csv(r"..\Data\Londondata\london2.csv", sep = ";")

#Get the year of observation
df["year"] = pd.to_datetime(df["DateTime"]).dt.year
df.index = df.index - 3840

#Isolate the year 2013
df = df[df["year"] == 2013]

#Get rid of Null values
#df["KWH/hh (per half hour) "] = df["KWH/hh (per half hour) "].replace('Null',0)

#Get values as float
df["KWH/hh (per half hour) "] = pd.to_numeric(df["KWH/hh (per half hour) "], downcast="float")

#Change format of dataframe, have Time as col and person as row
e = df.groupby('LCLid')['KWH/hh (per half hour) '].apply(lambda df: df.reset_index(drop=True)).unstack()

#Give column name
time =  df.iloc[range(0,17532),3]
e.columns = time


#Get data from 1st January
e1 = e.iloc[:,range(0,48)]
e1 = e1.drop(["MAC000016","MAC000050"])

#Get data from 31st May
e2 = e.iloc[:,range(7205,7253)]
e2 = e2.drop(["MAC000016","MAC000050"])

#Create PCA model
pca = PCA(n_components=2)
pca.fit(e1)


#Plot the results 
plt.figure()
X1 = pca.transform(e1)
plt.scatter(X1[:, 0], X1[:, 1], marker = '+', alpha=0.5, color = "blue", label ="01/01/2013" )
X2 = pca.transform(e2)
plt.scatter(X2[:, 0], X2[:, 1], marker = '+', alpha=0.5, color = "orange", label = "31/05/2013")
plt.legend()
plt.title("PCA Analysis for smart meter London data on 31/05/2013 and 01/01/2013")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
