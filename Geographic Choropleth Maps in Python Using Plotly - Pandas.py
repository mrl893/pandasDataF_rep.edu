#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.tools as tls


# In[2]:


tls.set_credentials_file(username='bigdatagal', api_key='hvginfgvwe')


# In[3]:


address ='C:/Users/master/Desktop/States.csv'
state = pd.read_csv(address)
state.columns = ['code','region','pop','satv','satm','percent','dollars','pay']
state.head()


# In[18]:


state['text']='SATv'+state['satv'].astype(str)+'SATm'+state['satm'].astype(str)+'<br>'+'States'+state['code']

data=[dict(type='choropleth',autocolorscales=False,loctions=state['code'], z=state['dollars'],locationmode= ['ISO-3', 'USA-states', 'country names'],
             text=state['text'],colorscales= 'custom-colorscales',colorbar= dict(title='Thousand dollars'))]
data


# In[19]:


layout =dict(tilte='State Spending on Public Education,in $k/student',
        geo=dict(scope='usa',projection=dict(type='albers usa'),showlakes=True,
                lakecolor='rgb(66,165,245)',),)
layout


# In[30]:


fig= dict(data=data, layout=layout) 
py.plot(fig, filename='d3-cloropleth-map')


# In[ ]:





# In[ ]:




