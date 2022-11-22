#!/usr/bin/env python
# coding: utf-8

# In[148]:


#Import pandas, numpy, pyplot from matplotlib and seaborn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#Read CSV file Year_Genre_Region
df=pd.read_csv(r'C:/Python/datasets/year_genre_region.csv')

#Print first five rows
df.head()


# In[149]:


df['region'].unique()


# In[150]:


#Data cleaning, white spaces in regions problematic,use np.where() to rectify

#np.where() syntax wrong, needs reworking

"""
p = df['region'].str
df['region'] = np.where(p.contains(' '),p.replace(' ','_',regex=True),p)
"""
df


# In[151]:


#Set decade bucket to get a clearer view of region sales since the 1980's
df['decade'] = [release_year//10*10 for release_year in df.release_year]

df.head(20)


# In[152]:


#Sales by decade and Region 
df2 = df.pivot_table(index='decade', columns='region', values='sales').dropna(thresh=0)


# In[129]:


df2


# In[130]:


df2.shape


# In[153]:


#Sales by year and region
df1= df.pivot_table(index='release_year', columns='region', values='sales').dropna(thresh=0)
df1


# In[154]:


df1.shape


# In[155]:


genre_totals = df['genre'].value_counts()
genre_totals


# In[ ]:





# In[ ]:





# In[ ]:




