# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

df = pd.read_csv('ok.csv')
#print('a')
df.dropna()
#print(df.head())
df1 = df.filter(['longitude','latitude'],axis=1)
#print(df1.head())


df1.dropna()


df1.dropna(subset=['longitude'], inplace=True)
df1.dropna(subset=['latitude'], inplace=True)
#df1.to_csv('temp.csv',index=False, header=True)


import seaborn as sns

sns.regplot(x=df1['longitude'],y=df1['latitude'],fit_reg=False)
from sklearn.cluster import KMeans

kmeans= KMeans(n_clusters=15,init='k-means++',max_iter=3000,n_init=10,random_state=0)
model=kmeans.fit(df1)
predicted_values= kmeans.predict(df1)

from matplotlib import pyplot as plt
plt.scatter(df1['longitude'],df1['latitude'],c=predicted_values,cmap='plasma')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=200,c='black',alpha=.5)












