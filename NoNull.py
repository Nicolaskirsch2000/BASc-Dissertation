# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:57:09 2020

@author: Kirsch
"""
import pandas as pd
import numpy as np



df = pd.read_csv(r"..\Data\Londondata\Power-Networks-LCL-June2015(withAcornGps)v2_34.csv")

for i in range(1,3): 
    dataframe = pd.read_csv(r"..\Data\Londondata\Power-Networks-LCL-June2015(withAcornGps)v2_"+str(i)+".csv")
    df = df.append(dataframe)



#Get the year of observation
df["year"] = pd.to_datetime(df["DateTime"]).dt.year
df.index = df.index - 3840


#Isolate the year 2013
df = df[df["year"] == 2013]

#Group by LCLid and keep only those with enough entries in 2013
df['KWH/hh (per half hour) '] = df['KWH/hh (per half hour) '].replace('Null',np.nan)
groups = df.groupby("LCLid")['KWH/hh (per half hour) '].apply(lambda x: len(x))


house1 = df[df["LCLid"] == "MAC000036"]
