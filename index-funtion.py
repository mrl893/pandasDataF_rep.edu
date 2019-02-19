#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


df= pd.DataFrame({'key':['A','A','B','C','C'],
                 'VALUES':[324,657,76,3,5]})
df


# In[4]:


df.index


# In[5]:


df.info


# In[6]:


df.set_index('key')


# In[7]:


df


# In[8]:


df.index


# In[ ]:




