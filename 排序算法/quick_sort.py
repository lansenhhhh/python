#!/usr/bin/env python
# coding: utf-8

# In[9]:


def quick_sort(arr):
    if len(arr) <2:
        return arr
    key = arr[0]
    left_side = [i for i in arr[1:] if i < key]
    right_side = [i for i in arr[1:] if i >= key]
    print(left_side)
    left_side = quick_sort(left_side)
    right_side = quick_sort(right_side)
    return left_side + [key] + right_side


# In[19]:


quick_sort([1,4,3,2,6])


# In[11]:


[1,2,3]+[1]


# In[ ]:





# In[ ]:




