# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:29:04 2018

@author: hfuji
"""

# 以下のモジュールを使うので、あらかじめ読み込んでおいてください
import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

# 可視化モジュール
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
#%matplotlib inline

# 小数第３まで表示
#%precision 3

hier_data_frame = DataFrame(np.arange(9).reshape((3,3))
                           ,index = [['a','a','b'],[1,2,2]]
                           ,columns = [['Osaka','Tokyo','Osaka']
                                      ,['Blue','Red','Red']]
                           )
print(hier_data_frame)

# indexに名前を付ける
hier_data_frame.index.names =['key1','key2']
# カラムに名前を付ける
hier_data_frame.columns.names =['city','color']
print(hier_data_frame)

print(hier_data_frame['Osaka'])

# 階層ごとの要約統計量：行合計
print(hier_data_frame.sum(level='key2'))

# 列合計
print(hier_data_frame.sum(level='color',axis=1))

print(hier_data_frame.drop(["b"]))



# データ1の準備
attri_data1 = {'ID':['100','101','102','103','104','106','108','110','111','113']
        ,'city':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo','Tokyo','Osaka','Kyoto','Hokkaido','Tokyo']
        ,'birth_year':[1990,1989,1992,1997,1982,1991,1988,1990,1995,1981]
        ,'name':['Hiroshi','Akiko','Yuki','Satoru','Steeve','Mituru','Aoi','Tarou','Suguru','Mitsuo']}
attri_data_frame1 = DataFrame(attri_data1)
attri_data_frame_index1 = DataFrame(attri_data1,index=['e','b','a','d','c','f','g','h','j','i'])
attri_data_frame_index1

# データ2の準備
attri_data2 = {'ID':['100','101','102','105','107']
        ,'math':[50,43,33,76,98]
        ,'English':[90,30,20,50,30]
        ,'sex':['M','F','F','M','M']
        ,'index_num':[0,1,2,3,4]}
attri_data_frame2 = DataFrame(attri_data2)
attri_data_frame2

# データのマージ（内部結合、inner　join が省略されてる、またキーは自動的に認識されるが、onで明示的に指定可能）
# また複数キーも可能、リストで指定
print("・結合テーブル")
pd.merge(attri_data_frame1,attri_data_frame2,on='ID')

# データのマージ（left）
pd.merge(attri_data_frame1,attri_data_frame2,how='left')

# データのマージ（outer）
pd.merge(attri_data_frame1,attri_data_frame2,how='outer')

# index によるマージ
pd.merge(attri_data_frame1,attri_data_frame2,left_index=True,right_on='index_num')


# データの準備
attri_data3 = {'ID':['117','118','119','120','125']
        ,'city':['Chiba','Kanagawa','Tokyo','Fukuoka','Okinawa']
        ,'birth_year':[1990,1989,1992,1997,1982]
        ,'name':['Suguru','Kouichi','Satochi','Yukie','Akari']}
attri_data_frame3 = DataFrame(attri_data3)

# concat 縦結合
concat_data = pd.concat([attri_data_frame1,attri_data_frame3])
# 注意：カラムがないとNaNになる
concat_data


#　ピボット　列が行に 
hier_data_frame.stack()

# 再配置
hier_data_frame.stack().unstack()

#　重複データ
dupli_data = DataFrame({'col1':[1,1,2,3,4,4,6,6]
                       ,'col2':['a','b','b','b','c','c','b','b']})
print("・元のデータ")
dupli_data

#　重複判定
print("・重複ありの行")
dupli_data.duplicated()

#　重複削除
print("・重複削除後のデータ")
dupli_data.drop_duplicates()


# 参照データ
city_map ={'Tokyo':'Kanto'
          ,'Hokkaido':'Hokkaido'
          ,'Osaka':'Kansai'
          ,'Kyoto':'Kansai'}
city_map

#　参照データを結合
# もし対応するデータがなかったら、NANになる。
attri_data_frame1['region'] = attri_data_frame1['city'].map(city_map)
attri_data_frame1

#　birth_year の上3つの数字・文字を取り出す
attri_data_frame1['up_two_num'] = attri_data_frame1['birth_year'].map(lambda x:str(x)[0:3])
attri_data_frame1

#　分割の粒度
birth_year_bins = [1980,1985,1990,1995,2000]

# ビン分割の実施
birth_year_cut_data = pd.cut(attri_data_frame1.birth_year,birth_year_bins)
birth_year_cut_data

# 集計結果
pd.value_counts(birth_year_cut_data)

# 名前付き
group_names = ["first1980","second1980","first1990","second1990"]
birth_year_cut_data = pd.cut(attri_data_frame1.birth_year,birth_year_bins,labels = group_names)
pd.value_counts(birth_year_cut_data)

# 数字で分割数指定可能。
# ここでは2つに分割
pd.cut(attri_data_frame1.birth_year,2)

pd.value_counts(pd.qcut(attri_data_frame1.birth_year,2))


# サイズ情報
attri_data_frame1.groupby("city").size()

# Cityを軸に、birth_yearの平均値を求める
attri_data_frame1.groupby("city")["birth_year"].mean()

attri_data_frame1.groupby(["region","city"])["birth_year"].mean()

attri_data_frame1.groupby(["region","city"],as_index=False)["birth_year"].mean()

import requests, zipfile
import io
zip_file_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00356/student.zip"
r = requests.get(zip_file_url, stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
student_data_math = pd.read_csv("student-mat.csv", sep=";")
# 列に複数の関数を適応
functions = ['count','mean','max','min']
grouped_student_math_data1 = student_data_math.groupby(['sex','address'])
grouped_student_math_data1['age','G1'].agg(functions)




# データの準備
import numpy as np
from numpy import nan as NA
import pandas as pd

sample_data_frame = pd.DataFrame(np.random.rand(10,4))

# NAにする
sample_data_frame.iloc[1,0] = NA
sample_data_frame.iloc[2:3,2] = NA
sample_data_frame.iloc[5:,3] = NA

print(sample_data_frame)
sample_data_frame.dropna()
sample_data_frame[[0,1]].dropna()
sample_data_frame.fillna(0)
sample_data_frame.fillna(method="ffill")

# 各カラムの平均値(確認用)
sample_data_frame.mean()
sample_data_frame.fillna(sample_data_frame.mean())

