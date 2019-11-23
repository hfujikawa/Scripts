# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 08:56:35 2019

@author: hfuji
"""

import pandas as pd
import datetime

fpath = 'D:/Develop/Asset/api-usdjpy-2m-1115.csv'
df = pd.read_csv(fpath)

df['Date'] = pd.to_datetime(df['Time']).dt.date

min_date = df['Date'].min()
max_date = df['Date'].max()
min_date_str = min_date.strftime('%Y-%m-%d')
max_date_str = max_date.strftime('%Y-%m-%d')
start_date = '{} 00:00:00'.format(min_date_str)
end_date = '{} 23:59:59'.format(max_date_str)


# https://qiita.com/kawagucchi_suzuki/items/a1b3e1ca142a4454934c
# 対象時間を選定
tlist = list(pd.date_range(start_date, end_date, freq='6H'))
# 対象時間データを抽出（２時間）
for i in range(len(tlist)-1):
    df_sel = df[(df['Time'] >= str(tlist[i])) & (df['Time'] < str(tlist[i+1]))]
    print(i, tlist[i], tlist[i+1], len(df_sel.index))
