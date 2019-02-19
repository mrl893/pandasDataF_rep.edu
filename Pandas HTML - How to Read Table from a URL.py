#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


d =pd.read_html('https://www.bankrate.com/cd.aspx')


# In[4]:


type(d)


# In[5]:


len(d)


# In[6]:


df=d[0]
df


# In[8]:


d[1]


# In[11]:


d[1].info()


# In[ ]:




