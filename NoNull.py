# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:57:09 2020

@author: Kirsch
"""
import pandas as pd
import numpy as np



df = pd.read_csv(r"..\Data\Londondata\Power-Networks-LCL-June2015(withAcornGps)v2_34.csv")

#Get the year of observation
df["year"] = pd.to_datetime(df["DateTime"]).dt.year
df.index = df.index - 3840


#Isolate the year 2013
df = df[df["year"] == 2013]

#Group by LCLid and keep only those with enough entries in 2013
df['KWH/hh (per half hour) '] = df['KWH/hh (per half hour) '].replace('Null',np.nan)
groups = df.groupby("LCLid")['KWH/hh (per half hour) '].apply(lambda x: len(x))
groups = groups[groups >=17520]
l = list(groups.index)
df = df[df["LCLid"].isin(l)]



#Change format of dataframe, have Time as col and person as row
e = df.groupby('LCLid')['KWH/hh (per half hour) '].apply(lambda df: df.reset_index(drop=True)).unstack()


#Give column name
time =  df.iloc[range(0,17532),2]
e.columns = time

print("fffffffff")