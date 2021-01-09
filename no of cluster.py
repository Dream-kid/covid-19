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


#import seaborn as sns

#sns.regplot(x=df1['longitude'],y=df1['latitude'],fit_reg=False)
from sklearn.mixture import GaussianMixture

n_components = np.arange(1,10)

gmm_model = [GaussianMixture(n,covariance_type='tied').fit(df1) for n in n_components]

from matplotlib import pyplot as plt
plt.plot(n_components,[m.bic(df1) for m in gmm_model], label='BIC')
plt.xlabel('n_components')











