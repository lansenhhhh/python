#!/usr/bin/env python
# coding: utf-8

# In[20]:


from numpy import *
def selection_sort(arr):
    n=len(arr)
    for i in arange(0,len(arr)-1):
        min_index=i
        for j in arange(i+1,n):
            #在未排序数组里面索引进行更新
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]
        print('-----》',arr)
selection_sort([1,4,0,3,2,6])
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




