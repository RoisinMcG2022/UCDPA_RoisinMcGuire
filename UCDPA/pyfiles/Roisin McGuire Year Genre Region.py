#!/usr/bin/env python
# coding: utf-8

# In[91]:


#Import pandas, numpy, pyplot from matplotlib and seaborn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#Read CSV file Year_Genre_Region
df=pd.read_csv(r'C:/Python/datasets/year_genre_region.csv', delimiter=',')

#Print first five rows
print(df.loc[df['region'] == 'Japan'])


# In[67]:


#Check how many unique variables are in Region
df["region"].unique()


# In[80]:


#Global Game Sales by Region, 1980-2020
ax=sns.relplot(x='release_year', y='sales',
          data=df,
          kind='line',
          hue='region')

#ax.set_xticks(range(len(df)), labels=range(1980, 2016))

ax.set(xlabel='Year', ylabel='Sales in Dollars(billions)')

plt.show()


# In[85]:


#Pivot table showing the average figures for all genres from (1991-2016), remove thresh to see complete data with incomplete years.
df.pivot_table(index='release_year', columns='genre', values='sales', aggfunc=['mean']).dropna(thresh=5)



# In[86]:


#Create pivot table showing region sales since the 1980's
df.pivot_table(index='release_year', columns='region', values='sales', aggfunc=['max']).dropna(thresh=5).plot(kind='bar', figsize=(15,8))
plt.show()


# In[87]:


#Set decade bucket to get a clearer view of region sales since the 1980's
df['decade'] = [release_year//10*10 for release_year in df.release_year]

df.head()


# In[84]:


#Display region buckets

df.pivot_table(index='decade', columns='region', values='sales', aggfunc=['max']).dropna(thresh=5).plot(kind='bar', figsize=(15,8))

plt.xticks(rotation=45)
plt.xlabel('Decade')
plt.ylabel('Sales in Billions')

plt.show()


# In[88]:


#find how many unique variables are in genre
df["genre"].unique()


# In[10]:


#df[(df.genre== 'Action') & (df.region == 'North America')]

#(df.loc[df['genre'] == 'Action'])


# In[89]:


sns.relplot(x='release_year', 
            y='sales', 
            data =df, palette=['yellow', 'green', 'orange', 'pink', 'red', 'maroon', 'purple', 'blue', 'cyan', 'violet', 'brown', 'black'],
           hue='genre')


# In[98]:


#release year and sales showing genre and grouped my region.
sns.relplot(x='release_year', 
            y='sales', 
            data =df,
           col='region',
           hue='genre')


# In[62]:


df_pivot=pd.pivot_table(df, values='sales', columns='genre', index='release_year').dropna(thresh=12)

df_pivot


# In[55]:


df2 = df_pivot.reset_index()

df2.to_csv('C:/Python/datasets/year_genre.csv', index =True)

#genre_wide = sns.load_dataset("df2").pivot("release_year", "sales", "genre")

#sns.relplot(data=genre_wide, kind="line")


# In[56]:


df2.dtypes


# In[90]:


df2.set_index('release_year')
df['release_year'] = df.release_year.astype(np.int64)
df2


# In[72]:


#Identify the best performing genre by year

#df2.set_index('release_year')

#df2['Top_Genre'] = df[['Action','Adventure','Fighting','Misc','Platform','Puzzle','Racing','Role-Playing','Shooter','Simulation','Sports','Strategy']].idxmax(axis=1)

#df2['Top_Genre'] = df2.idxmax(axis=1)

#df2.head()

df2.dtypes



# In[ ]:





# In[ ]:





# In[ ]:




