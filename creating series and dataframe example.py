#!/usr/bin/env python
# coding: utf-8

# color,name,price and season.     #fruits 

# In[1]:


# import  the necessary libraries


# In[2]:


import pandas as pd


# In[3]:


raw_data ={'name':['apple','mango','banana','watermelon'],
          'color':['red','yellow','yellowish','green'],
          'price':[45,39,44,45]}


# In[4]:


fruits=pd.DataFrame(raw_data)
fruits.head()


# In[5]:


fruits['season']=['rainy','sumer','winter','spring']
fruits


# In[ ]:





# In[ ]:





# In[ ]:




