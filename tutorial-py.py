#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


# In[3]:


# The inital set of baby names
names = ['Bob','Jessica','Mary','John','Mel']


# In[4]:


# This will ensure the random samples below can be reproduced. 
# This means the random samples will always be identical.

get_ipython().run_line_magic('pinfo', 'random.seed')


# In[5]:


get_ipython().run_line_magic('pinfo', 'random.randint')


# In[6]:


get_ipython().run_line_magic('pinfo', 'len')


# In[7]:


get_ipython().run_line_magic('pinfo', 'range')


# In[8]:


get_ipython().run_line_magic('pinfo', 'zip')


# In[9]:


random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

# Print first 10 records
random_names[:10]


# In[10]:


# The number of births per name for the year 1880
births = [random.randint(low=0,high=1000) for i in range(1000)]
births[:10]


# In[11]:


BabyDataSet = list(zip(random_names,births))
BabyDataSet[:10]


# In[12]:


df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df[:10]


# In[13]:


get_ipython().run_line_magic('pinfo', 'df.to_csv')


# In[14]:


df.to_csv('births1880.txt',index=False,header=False)


# In[15]:


get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# In[20]:


location = r'C:\Users\master\Downloads\hostdoc'
df =pd.read_csv(location)


# In[21]:


df.info()


# In[22]:


df.head()


# In[23]:


df = pd.read_csv(Location, header=None)
df.info()


# In[24]:


df.tail()


# In[25]:


df = pd.read_csv(Location, names=['Names','Births'])
df.head(5)


# In[26]:


import os
os.remove(Location)


# In[27]:


# Method 1:
df['Names'].unique()


# In[28]:


# If you actually want to print the unique values:
for x in df['Names'].unique():
    print(x)


# In[29]:


# Method 2:
print(df['Names'].describe())


# In[30]:


get_ipython().run_line_magic('pinfo', 'df.groupby')


# In[31]:


# Create a groupby object
name = df.groupby('Names')

# Apply the sum function to the groupby object
df = name.sum()
df


# In[32]:


# Method 1:
Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)


# In[33]:


# Method 2:
df['Births'].max()


# In[34]:


# Create graph
df['Births'].plot.bar()

print("The most popular name")
df.sort_values(by='Births', ascending=False)


# In[ ]:




