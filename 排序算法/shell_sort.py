#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
from numpy import *
def shell_sort(arr):
    n=len(arr)
    gap=n//2
    iter=0
    his_arr=mat(zeros((8,n)))
    while gap>0:
        for i in range(gap,n):
            j=i
            while(arr[j-gap]>arr[j] and j>=gap):
                arr[j-gap], arr[j]=arr[j],arr[j-gap]
                j-=gap
        gap=gap//2
        
        his_arr[iter,:]=mat(arr)
        iter=iter+1
    return arr,his_arr
s=random.normal(3,0.3,100)
[s_sort,his_s]=shell_sort(s)
print(his_s)
his_s=array(his_s)
plt.bar(arange(0,100,1),s_sort)


# In[8]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
#加方括号，对象是元组
fig,ax=plt.subplots(figsize=(5,4))
s=random.normal(3,0.3,100)
line,=ax.plot(arange(0,100,1),s)
print(his_s)
def update(i):
    label='frame{0}'.format(i)
    line.set_xdata(arange(0,100,1))
    line.set_ydata(his_s[i,:])
    return line,ax
anim=FuncAnimation(fig,update,frames=np.arange(0,8),interval=200)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




