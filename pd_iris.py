# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 09:31:37 2019

@author: hfuji
"""

import pandas as pd
#from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_dataset = load_iris()

# create DataFrame
all_data = iris_dataset['data']
iris_df = pd.DataFrame(all_data, columns=iris_dataset.feature_names)
target_names = ['setosa', 'versicolor', 'virginica']
# https://qiita.com/ao_log/items/fe9bd42fd249c2a7ee7a
iris_df['target'] = iris_dataset.target
iris_df.loc[iris_df['target'] == 0, 'target'] = target_names[0]
iris_df.loc[iris_df['target'] == 1, 'target'] = target_names[1]
iris_df.loc[iris_df['target'] == 2, 'target'] = target_names[2]
#pd.plotting.scatter_matrix(iris_df, alpha=0.2, figsize=(10, 10))
sns.pairplot(iris_df, hue="target")

# https://qiita.com/kenmikamin/items/b018f4618db067c3d51c
#iris_df.plot(kind="kde",subplots=True,layout=(2,2))    #kind="hist"でヒストグラム
iris_df.plot(kind="hist",subplots=True,layout=(2,2))    #kind="kde"でカーネル密度推定
plt.show()

iris_df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_length', 'target']
sns.distplot(iris_df[iris_df["target"]=="setosa"].sepal_length,kde=True,rug=True)
sns.distplot(iris_df[iris_df["target"]=="versicolor"].sepal_length,kde=True,rug=True)
plt.show()


# https://muthu.co/k-means-on-iris-dataset/
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
X = iris_df.values[:, 0:4]
model.fit(X)
labels = model.predict(X)

from sklearn.metrics import classification_report
#print(classification_report(iris_df['target'],model.labels_,target_names=target_names))
