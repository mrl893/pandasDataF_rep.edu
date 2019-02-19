#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


df =pd.read_clipboard()
df


# In[6]:


df.loc[::1,'Details'] = None
df


# In[9]:


df['Details'].isna()


# In[8]:


df[df['Details'].isna()]


# In[10]:


df.dropna()


# In[11]:


df


# In[12]:


df.fillna(0)


# In[13]:


df.fillna(method='bfill')


# In[ ]:




