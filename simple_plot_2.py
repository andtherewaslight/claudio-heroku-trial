#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widget


get_ipython().run_line_magic('matplotlib', 'widget')



# In[2]:


slider_f = widget.FloatSlider(value = 5., min= 0., max = 10., step = 0.1, description = 'Frequency')
display(slider_f)
fig,ax = plt.subplots()
x=np.linspace(0,5.,300)
ax.set_title('Cosine plot')
line, = ax.plot(x,np.cos(2*np.pi*slider_f.value*x))
def replot(change):
    line.set_ydata(np.cos(2*np.pi*slider_f.value*x))
    fig.canvas.draw()
    
    

slider_f.observe(replot)


# In[ ]:




