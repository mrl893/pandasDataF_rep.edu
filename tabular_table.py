#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


orders = pd.read_table('http://bit.ly/chiporders')


# In[3]:


orders.head()


# In[4]:


user_cols = ['user_id','age','gender','occupation','zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)


# In[5]:


users.head()


# # how to i  read  a tabular data into pandas?

# In[ ]:




