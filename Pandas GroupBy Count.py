#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


df =pd.read_clipboard()
df


# In[12]:


group =df.groupby(['values','key'])


# In[13]:


group.count()


# In[ ]:




