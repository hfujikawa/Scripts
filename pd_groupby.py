# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 08:05:56 2019
https://qiita.com/propella/items/a9a32b878c77222630ae
@author: hfuji
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'city': ['osaka', 'osaka', 'osaka', 'osaka', 'tokyo', 'tokyo', 'tokyo'],
    'food': ['apple', 'orange', 'banana', 'banana', 'apple', 'apple', 'banana'],
    'price': [100, 200, 250, 300, 150, 200, 400],
    'quantity': [1, 2, 3, 4, 5, 6, 7]
})

print(df)

cities = list(df['city'].unique())
foods = list(df['food'].unique())

# https://github.com/pandas-dev/pandas/issues/4882
df_merged = pd.DataFrame()
for group_name, df_tmp in df.groupby(['city', 'food']):
    print(group_name, len(df_tmp.index))
    df_merged = df_merged.append(df_tmp, ignore_index=True)

print(df_merged)
    

print(df.groupby(['city', 'food']).mean())
print(df.groupby(['city', 'food']).std())
print(df.groupby(['city', 'food']).describe())

print(df.groupby(['city', 'food', 'price']).sum())

print(df.groupby('city').get_group('osaka'))

print(df.groupby('city').size())

