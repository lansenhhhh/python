#!/usr/bin/env python
# coding: utf-8

# In[10]:


from numpy import *
def find_maxvalue(arr):
    max_value=arr[0]
    for index in arange(0,len(arr),1):
        if max_value<arr[index]:
            max_value=arr[index]
    return max_value
def insert_sort(arr):
    findmax_arr=[]
    for index in arange(0,len(arr),1):
        max_value=find_maxvalue(arr)
        arr.remove(max_value)
        findmax_arr.append(max_value)
    return findmax_arr



