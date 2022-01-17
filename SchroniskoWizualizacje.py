#!/usr/bin/env python
# coding: utf-8

# In[146]:


# źródło : https://www.kaggle.com/jmolitoris/adoptable-dogs
# The data is a compilation of information on dogs who were available for adoption on December 12, 2019 
# in the Hungarian Database of Homeless Pets. In total, there were 2,937 dogs in the database. 
# It contains information on dogs' names, breed, color, age, sex, the date they were found, 
# and some characteristics of their personalities.


# In[147]:


import pandas as pd


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', '')

import seaborn as sns
import numpy as np


# In[148]:


df=pd.read_csv("ShelterDogs.csv",delimiter=",",decimal=".")


# In[149]:


df.head(10)


# 

# In[150]:



df.fillna("no data", inplace = True)


# In[151]:


df.head(10)


# In[152]:


df


# In[ ]:





# In[153]:


#Małe psy lubiące ludzi i koty

df1 = df[(df['sex']=="male")&(df['size']=="small")&(df['likes_people']=="yes")&(df['get_along_cats']=="yes") ]


# In[154]:


df1


# In[155]:


#Średni wiek dla kategorii "Małe psy lubiące ludzi i koty"
df1['age'].mean() 


# In[156]:


#Suczki lubiące dzieci, w wieku poniżej 6 lat z krótką sierścią
df2= df[(df['sex']=="female")&(df['likes_children']=="yes")&(df['likes_children']=="yes")&(df['age']<6.0)&(df['coat']=="short") ]


# In[157]:



df2


# In[158]:


#stosunek płci
df['sex'].value_counts()


# In[159]:


#procent samiczek 
female = df['sex'].value_counts()[0]  #pierwsza linia
male = df['sex'].value_counts()[1]    #druga linia
total= female + male
procent=float(female) / total

print("Samiczek jest " + str(procent) + " %")


# In[ ]:


#Ilość piesków w danych kolorach


# In[160]:


df['color'].value_counts()


# In[161]:



df['color'].value_counts().plot(kind='barh')


# In[165]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




