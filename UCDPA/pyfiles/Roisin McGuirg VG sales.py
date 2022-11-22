#!/usr/bin/env python
# coding: utf-8

# In[18]:


#import pandas, numpy, pyplot and seaborn
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

#Parse and Read csv 
df = pd.read_csv(r"C:\Python\datasets\vgsales.csv")

#call df
df


# In[33]:


#Create smaller df called df_micro
df_micro = df[['Rank','Name','Genre','Year','Publisher','Global_Sales']]


print(df_micro)


# In[14]:


df_Top=df_micro.loc[df_micro['Rank'] <= 10]
print(df_Top)


# In[34]:


#use seaborn relplot to best selling games by year and copies
ax= sns.relplot(x='Year', y='Global_Sales', data=df_Top,
           hue='Name', s=150)

#set labels
ax.set(xlabel='Year', ylabel='Copies of Game Sold (Millions)')


# In[ ]:




