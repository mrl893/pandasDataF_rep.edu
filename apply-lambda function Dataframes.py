#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


d={'val':[123,6,8]}
df=pd.DataFrame(d)
df


# In[5]:


df['new'] = 5
df


# In[6]:


df['sum']=df.apply(lambda x: x['new']+100, axis=1)
df


# In[ ]:




