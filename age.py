# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

df = pd.read_csv('covid.csv')
#print('a')
df.dropna()
#print(df.head())
df1 = df.filter(['age','sex'],axis=1)


df1.dropna()


df1.dropna(subset=['sex'], inplace=True)
df1.dropna(subset=['age'], inplace=True)
df1['age']= df1['age'].apply(str)
df1= df1[df1['age'].str.len()< 3]
df1=df1.replace('male',2)
df1=df1.replace('Male',2)
df1=df1.replace('Female',1)
df1=df1.replace('female',1)
#print(df1.head())
#df1.to_csv('temp.csv',index=False, header=True)

df1=df1.astype(int)
print(df1.head())
#ax = df1.plot.hist(df1.iloc[:,0],bins=100, alpha=0.5)
ax = df1['age'].plot.hist(bins=100,stacked=True, alpha=0.5)
#df1.boxplot(by='age')
#df1.to_csv('temp.csv',index=False, header=True)









