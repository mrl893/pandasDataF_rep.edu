#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


df =pd.DataFrame({'key':[123,4,65]})
df


# In[4]:


df['new']=5
df


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df.plot('key','new');
df.plot('new','key');


# In[10]:


df.plot('key','new')


# In[8]:


import matplotlib.pylab as plt


# In[9]:


fig, axes = plt.subplots(nrows=1,ncols=2, figsize=(15,5))
fig.subplots_adjust(hspace=0.8)
df.plot(ax = axes[1]);
df['key'].plot(ax = axes[0])
df['new'].plot(ax = axes[1]);
axes[0].set_title('adsand',fontsize=25, color='r');
axes[0].set_xlabel('R-morel',fontsize=25, color='r');
axes[0].legend(['asd']);


# In[ ]:




