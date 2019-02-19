#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt  


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


my_dict = pd.read_csv('Desktop/police.csv')
my_dict.head()


# In[4]:


my_dict.shape


# In[5]:


my_dict.dtypes


# In[6]:


my_dict.isnull().sum()


# In[7]:


my_dict.isnull()


# In[8]:


True == 1


# In[9]:


False ==0


# # 1. remove the column that only contains missing values

# In[10]:


my_dict.dropna


# In[11]:


my_dict.columns


# In[12]:


my_dict.dropna(axis='columns',how='all').shape


# In[13]:


my_dict


# In[14]:


my_dict.shape


# In[15]:


my_dict.columns


# # 2 DO men or women speed more often?
# 
# drive_gender, violation
# 

# In[16]:


my_dict[my_dict.violation == 'Speendig'].driver_gender.value_counts(normalize=True)
my_dict.violation


# In[17]:


my_dict[my_dict.driver_gender == 'm'].violation.value_counts(normalize=True)
my_dict.driver_gender


# In[18]:


my_dict.groupby('driver_gender').violation.value_counts(normalize=True)


# In[19]:


my_dict.groupby('driver_gender').violation.value_counts(normalize=True).loc[:,'Speeding']


# In[20]:


my_dict.groupby('driver_gender').violation.value_counts(normalize=True).unstack()


# # Examining relationships
# 
# # 3Does gender affect who gets searched during a stop?
# 
# driver_gender,search_conducted

# In[21]:


my_dict.search_conducted.value_counts(normalize=True)


# In[22]:


my_dict.search_conducted.mean()


# In[23]:


my_dict.groupby('driver_gender').search_conducted.mean()


# In[24]:


my_dict.groupby(['violation','driver_gender']).search_conducted.mean()


# *handling missing values
# # 4 . why is search_type missing so often?

# In[25]:


my_dict.isnull().sum()


# In[26]:


my_dict[my_dict.search_conducted == False].search_type.value_counts(dropna=False)


# In[27]:


my_dict.search_type.value_counts(dropna=False)


# # 5 During a search, how often is the driver frisked?
# 
# 
# @ using string methods

# In[28]:


my_dict['frisk']=my_dict.search_type.str.contains('Protective Frisk')


# In[29]:


my_dict.frisk.value_counts(dropna=False)


# In[30]:


my_dict.frisk.sum()


# In[31]:


my_dict.frisk.mean()


# In[32]:


274 / (274 +2922)


# # 6 which year had the laest number of stops?
# @combining dates and times
# 

# In[33]:


my_dict.stop_date.str.slice(0,4).value_counts()


# In[34]:


combined = my_dict.stop_date.str.cat(my_dict.stop_time, sep=' ')


# In[35]:


my_dict['stop_datetime']=pd.to_datetime(combined)


# In[36]:


my_dict.dtypes


# In[37]:


my_dict.stop_datetime.dt.week.value_counts()


# In[38]:


my_dict.stop_datetime.dt.year.value_counts()


# In[39]:


my_dict.stop_datetime.dt.month.value_counts()


# # 7 how  does drugs activity change by time of day?
# 
# stop_datetime, drugs_related_stop
# 

# In[41]:


my_dict.drugs_related_stop.mean()


# In[44]:


my_dict.groupby(my_dict.stop_datetime.dt.hour).drugs_related_stop.mean().plot()


# In[45]:


my_dict.groupby(my_dict.stop_datetime.dt.time).drugs_related_stop.mean().plot()


# # 8. Do most stops occur at nigth?
# 

# In[61]:


my_dict.stop_datetime.dt.hour.value_counts().sort_index().plot()


# In[68]:


my_dict[(my_dict.stop_datetime.dt.hour > 4)& (my_dict.stop_datetime.dt.hour < 22)].shape


# In[69]:


my_dict.shape


# In[60]:


my_dict.stop_datetime.dt.time.value_counts().sort_index().plot()


# In[59]:


my_dict.stop_datetime.dt.hour.value_counts().sort_index().plot()


# In[72]:


my_dict.groupby(my_dict.stop_datetime.dt.hour).stop_date.count().plot()


# In[73]:


my_dict.groupby(my_dict.stop_datetime.dt.hour).count().plot()


# In[ ]:





# # 9. find that data in the stop_duration column and fix it
#  end you can adder plot()
#  

# In[76]:


my_dict.stop_duration.value_counts()


# In[77]:


my_dict.stop_duration.value_counts().plot()


# In[83]:


my_dict.loc[(my_dict.stop_duration == '1')|(my_dict.stop_duration == '2'), 'stop_duration']= 'NaN'


# In[ ]:


import numpy as np


# In[90]:


my_dict.loc[my_dict.stop_duration == 'NaN',['stop_duration','stop_date']]=np.nan


# In[91]:


my_dict.stop_duration.value_counts(dropna=False)


# In[86]:





# In[ ]:




