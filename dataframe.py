#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


import pandas as pd


# In[5]:


# create fake data


# In[6]:


d = {'key':['a','a','b'],
    'value':[23,24,7]}


# In[7]:


# create dataframe


# In[8]:


df = pd.dataframe(d)
df


# In[9]:


df = pd.DataFrame(d)
df


# In[10]:


# group by key


# In[11]:


group = df.groupby('key')


# In[12]:


# get sum


# In[13]:


df_sum = group.sum()
df_sum


# In[ ]:
