# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:43:15 2019

@author: hfuji
"""

import pandas as pd
#from modin import pandas as pd
import time
import glob
import os

#target_dir = 'D:/Develop/Asset'
target_dir = 'D:/Develop/Scripts'

start = time.time()
df_merged = pd.DataFrame()

'''
time measure[sec]
csv    zip    pkl
------------------------
7.8    9.1    5.2
7.7    9.1    5.2
7.8    9.1    5.5
'''
#files = glob.glob(target_dir + '/DAT_ASCII_USDJPY_M1*.csv')
#files = glob.glob(target_dir + '/api-usdjpy*.csv')
#files = glob.glob(target_dir + '/*Sales*.csv')
#files = glob.glob(target_dir + '/*Sales*.zip')
files = glob.glob(target_dir + '/*Sales*.pkl')
for fpath in files:
#    df = pd.read_csv(fpath, sep=';', names=('Time','Open','High','Low','Close', 'Volume'),
#                     index_col='Time', parse_dates=True)
#    df = pd.read_csv(fpath)
    df = pd.read_pickle(fpath)
    basename = os.path.basename(fpath)
    outfname = basename[:-4] + '.pkl'
#    df.to_pickle(outfname)
#    df_merged = df_merged.add(df, ignore_index=True)
    df_merged = df_merged.add(df)

print('elapsed time: ', time.time() - start)
df_merged.to_csv('api-usdjpy_joined.csv')
