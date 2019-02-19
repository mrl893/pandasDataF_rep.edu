
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:



Weather_data ={
    'Day' :['1/1/017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'Temperature' :[32,25,28,24,32,31],
    'Windspeed':[6,7,2,7,4,2],
    'Event' :['Rain','Sunny','Snow','Snow','Rain','Sunny']}

df = pd.DataFrame(Weather_data )
df


# Export the dataframe to a text file. We can name the file births1880.txt. The function to_csv will be used to export. The file will be saved in the same location of the notebook unless specified otherwise.

# In[3]:


get_ipython().run_line_magic('pinfo', 'df.to_csv')


# In[4]:


df.to_csv('weather_data.txt',index=False,header=False)


# In[5]:


get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# In[6]:


Location = (r'C:\Users\master\weather_data.csv')
df = pd.read_csv(Location)


# In[7]:


df.info()


# In[8]:


df


# In[9]:


df.tail()


# In[10]:


df = pd.read_csv(Location, names=['Rain','Sunny'])
df.head(5)


# In[11]:


Sorted = df.sort_values(['Rain'], ascending=False)
Sorted.head(1)


# In[12]:


df['Rain'].max()


# In[13]:


# Create graph
df['Rain'].plot.bar()

print("The most popular name")
df.sort_values(by='Rain', ascending=False)


# In[14]:


df['Rain'].plot.bar()

