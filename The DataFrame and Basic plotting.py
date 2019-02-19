#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('config', "inlinebackend.figure_format='svg'")


# In[2]:


x = np.linspace(0,4 * np.pi,100)
volts = np.sin(x)  +  0.25 * np.random.rand(len(x))
currents = np.cos(x) + 0.25 * np.random.rand(len(x))

plt.plot(x, volts, label='volt')
plt.plot(x, currents, label='current')
plt.legend()
plt.show()


# In[5]:


signal_dict = {
    'volts': volts,
    'currents': currents   
}

signal_df = pd.DataFrame(signal_dict)
signal_df[['currents','volts']].plot()
plt.show()


# In[ ]:




