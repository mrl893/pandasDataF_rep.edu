#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


my_dict={'pc':['file','document','folder']
         ,'datetime':[3,3,4],'runs':[100,300,600]}


# In[3]:


df=pd.DataFrame(my_dict)
df


# In[4]:


#renamed columns


# In[5]:


df=df.rename(columns ={'datetime':'num'})
df


# In[6]:


# delete columns


# In[7]:


del df['runs']
df


# In[ ]:





# In[ ]:




