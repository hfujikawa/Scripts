# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 08:56:35 2019

@author: hfuji
"""

import pandas as pd
import datetime
import glob
import time

target_dir = 'D:/Develop/Asset/'
files = glob.glob(target_dir + 'csv-usdjpy*.csv')
max_date =  datetime.date(1900,1,1)
min_date =  datetime.date(2099,12,31)
for fpath in files:
    df = pd.read_csv(fpath)
    names = df.columns.values
    newnames = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    for i in range(len(newnames)):
        names[i] = newnames[i]
    df['Date'] = pd.to_datetime(df['Time']).dt.date
    
    if min_date > df['Date'].min():
        min_date = df['Date'].min()
    if max_date < df['Date'].max():
        max_date = df['Date'].max()

min_date_str = min_date.strftime('%Y-%m-%d')
max_date_str = max_date.strftime('%Y-%m-%d')
start_date = '{} 00:00:00'.format(min_date_str)
end_date = '{} 23:59:59'.format(max_date_str)
# https://qiita.com/kawagucchi_suzuki/items/a1b3e1ca142a4454934c
# 対象時間を選定
tlist = list(pd.date_range(start_date, end_date, freq='6H'))

for fpath in files:
#    fpath = 'D:/Develop/Asset/api-usdjpy-2m-1115.csv'
    df = pd.read_csv(fpath)
    names = df.columns.values
    newnames = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    for i in range(len(newnames)):
        names[i] = newnames[i]
    df['Date'] = pd.to_datetime(df['Time']).dt.date
    
    
    # 対象時間データを抽出（6時間）
    for i in range(len(tlist)-1):
        df_sel = df[(df['Time'] >= str(tlist[i])) & (df['Time'] < str(tlist[i+1]))]
        if len(df_sel.index) > 0:
            print(i, tlist[i], tlist[i+1], len(df_sel.index))
