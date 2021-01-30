# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:32:54 2020

@author: Kirsch
"""

import pandas as pd
import datetime
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


df = pd.read_csv(r"..\Data\SAdata\2013_A.csv")


groups = df.groupby("RecorderID")['Unitsread'].apply(lambda x: len(x))

groups1 = df.groupby("ProfileID")['Unitsread'].apply(lambda x: len(x))

groups1 = groups1[groups1>8700]


df= df[df["ProfileID"].isin(groups1.index)]

grp = df.groupby("ProfileID")['Unitsread'].sum()

grp = grp[grp>2]

df= df[df["ProfileID"].isin(grp.index)]



year = pd.date_range("01/01/2013 00:00", "31/12/2013 23:00", freq="1h")

d = [None]*415
add = [None]*415
ids = list(grp.index)
for i in range(len(d)):
    d[i] = df[df["ProfileID"] == ids[i]]
    r = d[i]["Datefield"]
    years = [x.strftime("%Y-%m-%d %H:%M:%S") for x in year]
    main_list = np.setdiff1d(list(years),list(r))
    
    add[i] = pd.DataFrame({"RecorderID": "BTW001", "ProfileID":ids[i], "Datefield": main_list,"Unitsread": np.nan, "Valid": 1})
    
    #d[i] = d[i].append(add[i])
    
    #d[i] = d[i].sort_values(['ProfileID', 'Datefield'])
    
    #d[i] = d[i].reset_index(drop = True)
    
    df = df.append(add[i])
    
df = df.sort_values(['ProfileID', 'Datefield'])

df = df.reset_index(drop = True)

