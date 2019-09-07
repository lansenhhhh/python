#!/usr/bin/env python
# coding: utf-8

# In[27]:


from numpy import *
def Bubble(arr):
    num_arr=len(arr)
    for index in arange(0,len(arr),1):
        for j in arange(0,num_arr-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=[arr[j+1],arr[j]]
        num_arr=len(arr)-1
    return arr
Bubble([1,4,2,3,8,6,3])


# In[ ]:





# In[ ]:




