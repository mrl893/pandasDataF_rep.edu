#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt  


# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


my_dict = pd.read_csv('Desktop/police.csv')
my_dict.head()


# In[21]:


my_dict.shape


# In[22]:


my_dict.dtypes


# In[23]:


my_dict.isnull().sum()


# In[24]:


my_dict.isnull()


# In[25]:


True == 1


# In[26]:


False ==0


# # 1. remove the column that only contains missing values

# In[27]:


my_dict.dropna


# In[28]:


my_dict.columns


# In[29]:


my_dict.dropna(axis='columns',how='all').shape


# In[30]:


my_dict


# In[31]:


my_dict.shape


# In[32]:


my_dict.columns


# # 2 DO men or women speed more often?
# 
# drive_gender, violation
# 

# In[33]:


my_dict[my_dict.violation == 'Speendig'].driver_gender.value_counts(normalize=True)
my_dict.violation


# In[34]:


my_dict[my_dict.driver_gender == 'm'].violation.value_counts(normalize=True)
my_dict.driver_gender


# In[35]:


my_dict.groupby('driver_gender').violation.value_counts(normalize=True)


# In[36]:


my_dict.groupby('driver_gender').violation.value_counts(normalize=True).loc[:,'Speeding']


# In[37]:


my_dict.groupby('driver_gender').violation.value_counts(normalize=True).unstack()


# # Examining relationships
# 
# # 3Does gender affect who gets searched during a stop?
# 
# driver_gender,search_conducted

# In[38]:


my_dict.search_conducted.value_counts(normalize=True)


# In[39]:


my_dict.search_conducted.mean()


# In[40]:


my_dict.groupby('driver_gender').search_conducted.mean()


# In[41]:


my_dict.groupby(['violation','driver_gender']).search_conducted.mean()


# *handling missing values
# # 4 . why is search_type missing so often?

# In[42]:


my_dict.isnull().sum()


# In[43]:


my_dict[my_dict.search_conducted == False].search_type.value_counts(dropna=False)


# In[44]:


my_dict.search_type.value_counts(dropna=False)


# # 5 During a search, how often is the driver frisked?
# 
# 
# @ using string methods

# In[45]:


my_dict['frisk']=my_dict.search_type.str.contains('Protective Frisk')


# In[46]:


my_dict.frisk.value_counts(dropna=False)


# In[47]:


my_dict.frisk.sum()


# In[48]:


my_dict.frisk.mean()


# In[49]:


274 / (274 +2922)


# # 6 which year had the laest number of stops?
# @combining dates and times
# 

# In[50]:


my_dict.stop_date.str.slice(0,4).value_counts()


# In[51]:


combined = my_dict.stop_date.str.cat(my_dict.stop_time, sep=' ')


# In[52]:


my_dict['stop_datetime']=pd.to_datetime(combined)


# In[53]:


my_dict.dtypes


# In[58]:


my_dict.stop_datetime.dt.week.value_counts()


# In[59]:


my_dict.stop_datetime.dt.year.value_counts()


# In[63]:


my_dict.stop_datetime.dt.month.value_counts()


# In[ ]:




