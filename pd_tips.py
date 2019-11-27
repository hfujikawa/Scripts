# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 06:36:20 2019

@author: hfuji
"""

import pandas as pd

# https://stackoverflow.com/questions/34397982/pandas-dataframe-access-multiple-items-with-not-equal-to
fpath = 'D:/Develop/Scripts/TableSample.csv'
df = pd.read_csv(fpath)

df1 = df[(df['Train'] != 'DeutscheBahn') & (df['Train'] != 'SNCF')]

df2 = df.query("Train not in ['DeutscheBahn', 'British Rails', 'SNCF']")

df3 = df[(df['DayofMonth'] == 2) & (df['DayOfWeek'] == 6)]
