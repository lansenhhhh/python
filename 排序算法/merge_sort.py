#!/usr/bin/env python
# coding: utf-8

# In[15]:


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    num=len(arr)//2
    left_side=merge_sort(arr[:num])
    right_side=merge_sort(arr[num:])
    print(left_side)
    print(right_side)
    return merge(left_side,right_side)
def merge(left,right):
    l,r=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result += left[l:]
    result += right[r:]
    return result


# In[13]:





# In[ ]:




