#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append('F:\机器学习\python文件\BFGS')
import matplotlib.pyplot as plt
from numpy import *
from bfgs import BFGS
from function import *
from mpl_toolkits.mplot3d import Axes3D
x0=mat([[-1.2],[1]])
result1=BFGS(fun,gfun,x0)
n=len(result1)
fig=plt.figure(figsize=(20,8))
ax1=fig.add_subplot(121,projection='3d')
ax2=fig.add_subplot(122)
ax2.plot(arange(0,n,1),result1)
x1=arange(-1,1,0.1)
x2=arange(-1,1,0.1)
Z=zeros((len(x1),len(x2)))
for i in arange(0,len(x1),1):
    for j in arange(0,len(x2),1):
        x=mat([[x1[i]],[x2[j]]])
        Z[i,j]=fun(x)

[X,Y]=meshgrid(x1,x2)
ax1.plot_surface(X,Y,Z)

