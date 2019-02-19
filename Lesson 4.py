
# coding: utf-8

# In[1]:


import pandas as pd
import sys


# In[2]:


print('python version: ' + sys.version)
print('pandas version: ' + pd.__version__)


# # our small data set

# In[3]:


dict=[0,1,2,3,4,5,6,7,8,9]


# # create dataframe

# In[4]:


df=pd.DataFrame(dict)
df


# # lets change the name of the column

# In[5]:


df.columns=["Crud"]
df


# # lets add a column

# In[6]:


df['num10']=10
df


# # lets mofify our new column

# In[7]:


df['num10']= df['num10'] + 15
df


# # we can delete columns

# In[8]:


del df['num10']
df


# # lets add a couple of columns

# In[9]:


df['Create']=5
df['Read']=10
df['Update']=15
df['Delete']=20
df


# # if  we wanted, we could change the name of the index

# In[10]:


Y=['A','B','C','D','E','F','G','H','I','J']
df.index=Y
df


# # we can now start to select pieces of the dataframe unig loc

# In[11]:


df.loc['A']


# # df.loc[inclusive:inclusive]

# In[12]:


df.loc['A':'D']


# # df.iloc[inclusive:exclusive]
# # Note: .iloc is strictly integer position based. It is available from [version 0.11.0] (http://pandas.pydata.org/pandas-docs/stable/whatsnew.html#v0-11-0-april-22-2013) 

# In[13]:


df.iloc[0:3]


# # we can also select using the column name

# In[15]:


df['Crud']


# In[19]:


df[['Crud' ,'Create','Read','Update','Delete']]


# In[20]:


df[['Crud','Delete']]


# # df.ix[rows,columns]
# # replaces the deprecated ix function
# # df.ix[0:5,'Create']

# In[21]:


df.loc[df.index[0:3],'Crud']


# # replaces the deprecated ix function
# # df.ix[5:,'Create']

# In[25]:


df.loc[df.index[5:],'Create']


# # replaces the deprecated ix function
# # df.ix[:3,['Create', 'Update']]

# In[26]:


df.loc[df.index[:3],['Create','Read']]


# # Select top N number of records (default = 5)

# In[27]:


df.head()


# # Select bottom N number of records (default = 5)

# In[28]:


df.tail()

