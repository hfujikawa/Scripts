# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:22:21 2018

@author: hfuji
"""

#
# Basics of Numpy
#
import numpy as np

darray = np.array([9,2,3,4,10,6,7,8,1,5])
print(darray.dtype)
print(darray.shape)

zero_data = np.zeros((2,3), dtype='i')
one_data = np.ones((2,3), dtype='f')

darray.sort()
revarry = darray[::-1]


import numpy.random as rand

rand.seed(0)
norm_rand_darray = rand.randn(10)


# https://note.nkmk.me/python-timeit-measure/
import timeit

N = 10**6
norm_data = [rand.random() for _ in range(N)]
np_rand_data = np.array(norm_data)

loop = 100
result = timeit.timeit('sum(norm_data)', globals=globals(), number=loop)
print(result/loop)
result = timeit.timeit('np.sum(np_rand_data)', globals=globals(), number=loop)
print(result/loop)


#
# Basics of Scipy
#
import scipy as sp
import scipy.linalg as linalg
from scipy.optimize import minimize_scalar

mat_data = np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
print("det = ", linalg.det(mat_data))
print("inv = \n", linalg.inv(mat_data))
print("multiply = \n", mat_data.dot(linalg.inv(mat_data)))

eig_val, eig_vec = linalg.eig(mat_data)
print("eigen value = ", eig_val)
print("eigen vector = \n", eig_vec)


def quad_func(x):
    return (x**2 + 2*x + 1)

from scipy.optimize import newton
print("Newton method = ", newton(quad_func, 0))
print("Brent method = \n", minimize_scalar(quad_func, method="Brent"))



#
# Basics of Pandas
#
from pandas import Series, DataFrame
import pandas as pd

pd_data = pd.Series([0,1,2,3,4,5,6,7,8,9])
print(pd_data)
print("data: ", pd_data.values)
print("index: ", pd_data.index)

pd_index_data = pd.Series([0,1,2,3,4,5,6,7,8,9],
                          index=['a','b','c','d','e','f','g','h','i','j'])
print(pd_index_data)
print("data: ", pd_index_data.values)
print("index: ", pd_index_data.index)

attri_data1 = {'ID':['100','101','102','103','104']
        ,'city':['Tokyo','Osaka','Kyoto','Hokkaidao','Tokyo']
        ,'birth_year':[1990,1989,1992,1997,1982]
        ,'name':['Hiroshi','Akiko','Yuki','Satoru','Steeve']}
attri_data_frame1 = DataFrame(attri_data1)
print(attri_data_frame1)
attri_data_frame_index1 = DataFrame(attri_data1,index=['a','b','c','d','e'])
print(attri_data_frame_index1)
# 転置
attri_data_frame1.T
# 列名の指定（１つ）
attri_data_frame1.birth_year
# 列名の指定(複数の場合)
attri_data_frame1[["ID","birth_year"]]
#　条件（フィルター）
attri_data_frame1[attri_data_frame1['city']=='Tokyo']
#　条件（フィルター、複数の値）
attri_data_frame1[attri_data_frame1['city'].isin(['Tokyo','Osaka'])]
# データの列の削除
attri_data_frame1.drop(['birth_year'],axis=1)

# 別のデータの準備
attri_data2 = {'ID':['100','101','102','105','107']
        ,'math':[50,43,33,76,98]
        ,'English':[90,30,20,50,30]
        ,'sex':['M','F','F','M','M']}
attri_data_frame2 = DataFrame(attri_data2)
print(attri_data_frame2)
# データのマージ（内部結合、詳しくは次の章で）
pd.merge(attri_data_frame1,attri_data_frame2)
# データのグループ集計(詳しくは次の章で)
attri_data_frame2.groupby("sex")["math"].mean()

# データの準備
attri_data2 = {'ID':['100','101','102','103','104']
        ,'city':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo']
        ,'birth_year':[1990,1989,1992,1997,1982]
        ,'name':['Hiroshi','Akiko','Yuki','Satoru','Steeve']}
attri_data_frame2 = DataFrame(attri_data2)
attri_data_frame_index2 = DataFrame(attri_data2,index=['e','b','a','d','c'])
print(attri_data_frame_index2)
# indexによるソート
attri_data_frame_index2.sort_index()
# 値によるソート、デフォルトは昇順
attri_data_frame_index2.birth_year.sort_values()
# 値があるかどうかの確認
attri_data_frame_index2.isin(["Tokyo"])
#　欠損値の取り扱い
# name をすべてnanにする
attri_data_frame_index2.name = np.nan
attri_data_frame_index2.isnull()
# nullを判定し、合計する
attri_data_frame_index2.isnull().sum()



#
# Basics of Matplotlib
#
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

#
# 散布図
import numpy.random as random

#　シード値の固定
random.seed(0)
# x軸のデータ
x = np.random.randn(30)
# y軸のデータ
y = np.sin(x) + np.random.randn(30)

# plot
plt.plot(x, y, "o")

#以下でも散布図が描ける
#plt.scatter(x, y)

# title
plt.title("Title Name")
# Xの座標名
plt.xlabel("X")
# Yの座標名
plt.ylabel("Y")

# gridの表示
plt.grid(True)

#
# 連続曲線
np.random.seed(0)
# データの範囲
numpy_data_x = np.arange(1000)

# 乱数の発生と積み上げ
numpy_random_data_y = np.random.randn(1000).cumsum()

# label=とlegendでラベルをつけることが可能
plt.plot(numpy_data_x,numpy_random_data_y,label="Label")
plt.legend()

plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

#
# sin関数

# 2行1列のグラフの1つ目
plt.subplot(2,1,1)
x = np.linspace(-10, 10,100)
plt.plot(x, np.sin(x)) 

# 2行1列のグラフの2つ目
plt.subplot(2,1,2)
y = np.linspace(-10, 10,100)
plt.plot(y, np.sin(2*y)) 

plt.grid(True)

#
# 二次関数
x = np.arange(-10, 10)
plt.plot(x, quad_func(x)) 
plt.grid(True)

#
# histogram
random.seed(0)
plt.hist(np.random.randn(10**5)*10 + 50, bins=60,range=(20,80))
plt.grid(True)


