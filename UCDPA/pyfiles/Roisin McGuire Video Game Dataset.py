#!/usr/bin/env python
# coding: utf-8

# In[16]:


#import pandas, numpy, pyplot and seaborn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#read dataset from csv file
df=pd.read_csv(r'C:/Python/datasets/Video_Games_Dataset.csv')
pd.set_option('display.max_rows', 100)

#view top 20 rows
df.head(20)


# In[5]:


#get max, min and mean global sales
df['Global_Sales'].max()
#df['Global_Sales'].min()
#df['Global_Sales'].mean()


# In[13]:


Genre_by_Year = df.groupby(["Genre", "Platform", "Year"])["Genre"].count()
pd.set_option('display.max_rows',200)
print(Genre_by_Year)


# In[12]:


#Which genre sold the most in a year, Action sold 3
Genre_by_Year.max()


# In[14]:


#large variety of genres across decades so there is a lot of null values 
df.pivot_table(index='Year', columns='Genre', values='Global_Sales', aggfunc=['max']).dropna(thresh=6)


# In[17]:


#1996 and 1999 showing a peak in role-playing games (Pokemon on Gameboy), Mario Kart 2008 Racing, 
#New Super Mario Bros. on Wii 2009 is Platform, Wii Fit Plus is Sports.

#create bar chart from pivot table
df.pivot_table(index='Year', columns='Genre', values='Global_Sales', aggfunc=['max']).dropna(thresh=6).plot(kind='bar', figsize=(15,8))

plt.show()


# In[18]:


#Average globl sales for Action
df.loc[df['Genre'] == 'Action', 'Global_Sales'].mean()


# In[19]:


#Average Global Sales for Sports
df.loc[df['Genre'] == 'Sports', 'Global_Sales'].mean()


# In[20]:


#Average global sales for Platformers
df.loc[df['Genre'] == 'Platform', 'Global_Sales'].mean()


# In[21]:


#Average global sales for Role-Playing
df.loc[df['Genre'] == 'Role-Playing', 'Global_Sales'].mean()


# In[22]:


#Average Global sales for Racing
df.loc[df['Genre'] == 'Racing', 'Global_Sales'].mean()


# In[40]:


#Create bar graph showing genre sales by copies using groupby()

ax=df.groupby('Genre')['Global_Sales'].max().plot(kind='bar', figsize=(15,8),color=['pink', 'red', 'maroon', 'purple', 'blue', 'cyan'])

#set x and y labels
ax.set(xlabel='Genre', ylabel='Copies of Game Sold (Millions)')


# In[24]:


#Show max global sales for Genres by year
df.groupby(['Year','Genre'])['Global_Sales'].max()


# In[28]:


#Min and Max sales by genre
df.groupby('Genre')['Global_Sales'].agg(['min','max'])


# In[27]:


#Min and Max sales by genre plot
ax=df.groupby('Genre')['Global_Sales'].agg(['min','max']).plot(kind='bar', figsize=(15,8),color=['pink','purple'])
ax.set(xlabel='Genre', ylabel='Copies of Game Sold (Millions)')
plt.show()


# In[37]:


#Yearly sales
ax=df.groupby(['Year'])['Global_Sales'].max().plot(kind='bar', figsize=(15,8), color=['brown','red', 'orange', 'yellow'])
ax.set(xlabel='Year', ylabel='Copies of Game Sold (Millions)')
plt.show()


# In[ ]:




