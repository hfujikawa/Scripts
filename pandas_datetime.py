# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:22:30 2019

@author: hfuji
"""

import pandas as pd
import datetime

date_str = '2018/2/1 12:30'
date_dt = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M')
print(date_dt)
# 2018-02-01 12:30:00

print(type(date_dt))
# <class 'datetime.datetime'>


df = pd.read_csv('sample.csv')
print(df)
print('nan sum: ', df.isnull().sum())

df = df.dropna(how='all')
print(df)