#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly as py
import plotly.graph_objs as go
import ipywidgets as widgets
import numpy as np
from scipy import special

py.offline.init_notebook_mode(connected=True)


# In[7]:


x = np.linspace(0, np.pi, 300)

layout = go.Layout(
    title='<b>SIMPLE EXAMPLE</b>',
    yaxis=dict(
        title='<i>(Volts)</i>'
    ),
    xaxis=dict(
        title='<i>(nanoseconds)</i>'
    )
)


def update_plot(signals, freq):
    
    """
    This function updates the plot everytime a widget is changed
    """

    data = []
    for s in signals:
        trace1 = go.Scatter(
            x=x,
            y=special.jv(s, freq * x),
            mode='lines',
            name='bessel {}'.format(s),
            line=dict(
                shape='spline'
            )
        )
        data.append(trace1)

    fig = go.Figure(data=data, layout=layout)
    py.offline.iplot(fig)
    

signals = widgets.SelectMultiple(options=list(range(6)), value=(0, ), description='Bessel Order')
freq = widgets.FloatSlider(min=1, max=20, value=1, description='Freq')
widgets.interactive(update_plot, signals=signals, freq=freq)


# In[ ]:





# In[ ]:





# In[ ]:




