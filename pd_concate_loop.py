# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:13:40 2019

@author: hfuji
"""

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display import display

# https://stackoverflow.com/questions/28669482/appending-pandas-dataframes-generated-in-a-for-loop
# http://eforexcel.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/

target_dir = 'D:\\Develop\\Asset\\api-usdjpy-*.csv'
files = glob.glob(target_dir)

df_merged = pd.DataFrame()
for fpath in files:
    df = pd.read_csv(fpath)
    df_merged = df_merged.append(df, ignore_index=True)

# データフィルター
df_merged.dropna(subset=['Volume'])
df_sort = df_merged.sort_values('Time')
df_reset = df_sort.reset_index(drop=True)
df_reset.to_csv('index_reset.csv', index=False)

print(df_reset.info())
print(df_reset.shape)
print(df_reset.mean())
print(df_reset.shape)
print(df_reset.describe())

col_name_arr = list(df.columns.values)
print(df_merged.isnull().sum())


#df_5col = df_merged[['Time', 'Close']]
df_5col = df_merged[col_name_arr[:-1]]

df_5col.plot(kind="hist",subplots=True,layout=(2,2))    #kind="kde"でカーネル密度推定
plt.show()


# 日本語パス
jp_fdir = r'C:\Users\hfuji\OneDrive\ドキュメント\中間レポート一式'
slashed_dir = jp_fdir.replace(os.path.sep, '/')
jp_files = glob.glob(slashed_dir + '/*')


# Beauty Output
data = {'Name': ["John","Anna","Peter","Linda"],
        'Location': ["New York","Paris","Berlin","London"],
        'Age':  [24,13,53,33],}
data_pandas = pd.DataFrame(data)
display(data_pandas)
