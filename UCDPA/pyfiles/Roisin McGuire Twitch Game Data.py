#!/usr/bin/env python
# coding: utf-8

# In[97]:


#import pandas, numpy, pyplot and seaborn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

df=pd.read_csv(r'C:/Python/datasets/Twitch_game_data.csv',encoding='cp1252')


df.head()


# In[96]:


df.dtypes


# In[98]:


#Resolving potential issue where Hours Streamed contains a str 'hours', removing this and setting the value to an int
p = df['Hours_Streamed'].str
df['Hours_Streamed'] = np.where(p.endswith(' hours'),p.replace(' hours','',regex=True),p)
df.head()


# In[99]:


#set hours streamed to int
df['Hours_Streamed'] = df.Hours_Streamed.astype(np.int64)


# In[101]:


#check data types
df.dtypes


# In[27]:


#df['Game'] = df['Game'].astype(str).str.replace('<U+00E9>', 'e', regex=True)


# In[31]:


#Use .loc to call up any game
print(df.loc[df['Game'] == 'Destiny'])


# In[105]:


#There is an encoding issue with all Pokemon games due to an accent on the e in Pokemon. Code below will rectify it if needed but
#it is causing an issue wih other values in 'Game' so I have left it greyed out.

"""
df.replace(to_replace ='Pok<U+00E9>mon Omega Ruby/Alpha Sapphire',
               value ='Pokemon Omega Ruby/Alpha Sapphire',inplace=True)
           
df.replace(to_replace ='Pok<U+00E9>mon Red/Blue',
               value ='Pokemon Red/Blue',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Yellow',
               value ='Pokemon Yellow',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon FireRed/LeafGreen',
               value ='Pokemon FireRed/LeafGreen',inplace=True)

df.replace(to_replace ='Pokk<U+00E9>n Tournament',
               value ='Pokken Tournament',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Crystal',
               value ='Pokemon Crystal',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Sun/Moon',
               value ='Pokemon Sun/Moon',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon GO',
               value ='Pokemon GO',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Trading Card Game Online',
               value ='Pokemon Trading Card Game Online',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Emerald',
               value ='Pokemon Emerald',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Trading Card Game',
               value ='Trading Card Game',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon HeartGold/SoulSilver',
               value ='Pokemon HeartGold/SoulSilver',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Black/White Version 2',
               value ='Pokemon Black/White Version 2',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Ultra Sun/Ultra Moon',
               value ='Pokemon Ultra Sun/Ultra Moon',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Quest',
               value ='Pokemon Quest',inplace=True)

df.replace(to_replace ="Pok<U+00E9>mon: Let's Go, Pikachu!",
               value ="Pokemon: Let's Go, Pikachu!", inplace=True)
           
df.replace(to_replace ='Pok<U+00E9>mon Stadium 2',
               value ='Pokemon Stadium 2',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Mystery Dungeon: Rescue Team DX',
               value ='Pokemon Mystery Dungeon: Rescue Team DX',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon X/Y',
               value ='Pokemon X/Y',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Platinum',
               value ='Pokemon Platinum',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Unite',
               value ='Pokemon Unite',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Brilliant Diamond/Shining Pearl',
               value ='Pokemon Brilliant Diamond/Shining Pearl',inplace=True)

df.replace(to_replace ='New Pok<U+00E9>mon Snap',
               value ='New Pokemon Snap',inplace=True)

df.replace(to_replace ='Pok<U+00E9>mon Ruby/Sapphire',
               value ='Pokemon Ruby/Sapphire',inplace=True)
"""
print(df.loc[df['Game'] == 'Pok<U+00E9>mon Sword/Shield'])


# In[ ]:





# In[104]:


print(df.loc[df['Game'] == 'Fortnite'])


# In[67]:





# In[82]:


#Top five rank places
sns.relplot(x='Month', y='Hours_watched', data=df_Top,
            col='Rank', hue='Game', s=150)


# In[38]:


#set max row limit
pd.options.display.max_rows = 200
#df = df[df['Game'].str.contains('Pok')]
print(df['Game'])


# In[142]:


df.shape



# In[23]:


#average hours watched per year
df.groupby('Year')['Hours_watched'].mean()


# In[106]:


#average hours watched per year in line graph
df.groupby('Year')['Hours_watched'].mean().plot(kind='line', color='purple')
plt.ylabel('Hours Watched (in Millions)')

plt.show()


# In[34]:


#check shape of pivot table 
df.pivot_table(index='Game',columns= 'Year', values='Hours_watched').shape


# In[41]:


#print pivot table game views by year
df.pivot_table(index='Game',columns= 'Year', values='Hours_watched', aggfunc='max').dropna(thresh=6)


# In[144]:


#most watched, indexed by game
df1= df.pivot_table(index='Game',columns= 'Year', values='Hours_watched', aggfunc='max').dropna(thresh=0)
df.head(10)


# In[45]:


#create smaller dataframe with columns of interest
df_micro = df[['Rank','Game','Month','Year','Hours_watched']]
print(df_micro)


# In[135]:


#Check top 1/2/3/4/5 etc ranking games by month. Adjust rank number as needed
df_Top=df_micro.loc[df_micro['Rank'] <= 5]
print(df_Top)


# In[136]:


#create dataframe of top ranked games for year 2016
df2016 =df_Top.loc[df_Top['Year'] == 2016]

print(df2016)


# In[141]:


#Top Five Games on Twitch by Month, each dot correlates to that month's most watched game in that rank position, grouped by rank

sns.relplot(x='Month', y='Hours_watched', data=df2016,
            col='Rank', hue='Game', s=200)

ax.set(xlabel='Month', ylabel='Hours watched(in 100 millions)')


plt.show()


# In[134]:


#Most watched game on Twitch out of 2016
#Rank is set to '1' with the following code: df_Top=df_micro.loc[df_micro['Rank'] <= 1]
sns.relplot(x='Month', y='Hours_watched', data=df2016,
            col='Rank', hue='Game', s=150)

ax.set(xlabel='Month', ylabel='Hours watched(in 100 millions)')
plt.title("2016")

plt.show()


# In[129]:


#create dataframe of top ranked games for year 2017, 2018, 2019, 2020
df2017 =df_Top.loc[df_Top['Year'] == 2017]
df2018 =df_Top.loc[df_Top['Year'] == 2018]
df2019 =df_Top.loc[df_Top['Year'] == 2019]
df2020 =df_Top.loc[df_Top['Year'] == 2020]

print(df2017)
print(df2018)
print(df2019)
print(df2020)


# In[130]:


#create relplot for 2017 showing top ranked game by month
#Rank is set to '1' with the following code: df_Top=df_micro.loc[df_micro['Rank'] <= 1]

ax=sns.relplot(x='Month', y='Hours_watched', data=df2017,
            col='Rank', hue='Game', s=150)

ax.set(xlabel='Month', ylabel='Hours watched(in 100 millions)')
plt.title("2017")

plt.show()


# In[131]:


#create relplot for 2018 showing top ranked game by month
#Rank is set to '1' with the following code: df_Top=df_micro.loc[df_micro['Rank'] <= 1]

sns.relplot(x='Month', y='Hours_watched', data=df2018,
            col='Rank', hue='Game', s=150)
ax.set(xlabel='Month', ylabel='Hours watched(in 100 millions)')
plt.title("2018")

plt.show()



# In[114]:


#create relplot for 2019 showing top ranked game by month
#Rank is set to '1' with the following code: df_Top=df_micro.loc[df_micro['Rank'] <= 1]

ax=sns.relplot(x='Month', y='Hours_watched', data=df2019,
            col='Rank', hue='Game', s=150)
ax.set(xlabel='Month', ylabel='Hours watched(in 100 millions)')
plt.title("2019")

plt.show()


# In[133]:


#create relplot for 2020 showing top ranked game by month
#Rank is set to '1' with the following code: df_Top=df_micro.loc[df_micro['Rank'] <= 1]

sns.relplot(x='Month', y='Hours_watched', data=df2020,
            col='Rank', hue='Game', s=150)

ax.set(xlabel='Month', ylabel='Hours watched(in 100 millions)')

plt.title("2020")

plt.show()


# In[ ]:




