# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 08:56:22 2018

@author: hfuji
"""

import numpy as np
import numpy.random as rand
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# webからデータを取得したり、zipファイルを扱うためのモジュール
import requests, zipfile
from io import StringIO
import io

# データがあるurl の指定
zip_file_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00356/student.zip"

# データをurlから取得する
r = requests.get(zip_file_url, stream=True)

# zipfileを読み込み展開する
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

student_data_math = pd.read_csv("./student-mat.csv")
student_data_math.head()
# データの読み込み
# 区切りが;ついているので注意
student_data_math = pd.read_csv("./student-mat.csv", sep=";")
# どんなデータがあるかざっと見る
student_data_math.head()
# すべてのカラムの情報等チェック
student_data_math.info()



from sklearn import linear_model

# 線形回帰のインスタンスを生成
clf = linear_model.LinearRegression()

# 説明変数に "一期目の数学の成績" を利用
# ilocはデータフレームから、行と列を指定して取り出す。loc[:, ['G1']]は、G1列のすべての列を取り出すことをしている
# marixの型に直しているので、注意
# https://ntnl-it-wiz.blogspot.com/2018/11/pandasasmatrixvalues.html
#X = student_data_math.loc[:, ['G1']].as_matrix()
X = student_data_math.loc[:, ['G1']].values

# 目的変数に "最終の数学の成績" を利用
#Y = student_data_math['G3'].as_matrix()
Y = student_data_math['G3'].values

# 予測モデルを計算、ここでa,bを算出
clf.fit(X, Y)
 
# 回帰係数
print("回帰係数:", clf.coef_)

# 切片 
print("切片:", clf.intercept_)

# 先ほどと同じ散布図
plt.scatter(X, Y)
plt.xlabel("G1 grade")
plt.ylabel("G3 grade")

# その上に線形回帰直線を引く
plt.plot(X, clf.predict(X))
plt.grid(True)

# 決定係数、寄与率とも呼ばれる
print("決定係数:", clf.score(X, Y))


