#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly
from plotly import __version__
print(__version__)
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot


# In[2]:


init_notebook_mode(connected=True)


# In[3]:


# to save the chart to plotly cloud of plotly emterprise, use 'plotly.plotly.iplot'.


# In[4]:


iplot([{'x':[1,2,3,4,5], 'y':[1,2,3,6,4,1]}])


# In[5]:


import plotly.graph_objs as go
import numpy as np


# In[6]:


x = np.random.randn(2000)
y = np.random.randn(2000)
iplot([go.Histogram2dcontour(x=x,y=y, contours=dict(coloring='heatmap')),
      go.Scatter(x=x,y=y, mode='markers', marker=dict(color='white',size=3,opacity=0.3))],
   show_link=False)


# In[ ]:




