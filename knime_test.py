# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 06:25:49 2019
https://www.t-kahi.com/entry/2019/08/19/172246
@author: hfuji
"""

#Python Source 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import mglearn
from IPython.display import display
from sklearn.datasets import make_blobs
X, y = make_blobs(random_state=42)
print(X)
print(y)
input_table = pd.DataFrame(X)

input_table.plot(kind='scatter', x=0, y=1)



from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)
kmeans.fit(input_table)

predict = pd.DataFrame(kmeans.predict(input_table),columns=['predict'])
new_input = input_table.reset_index(drop=True)

results = new_input.join(predict)

output_table = results.reset_index()