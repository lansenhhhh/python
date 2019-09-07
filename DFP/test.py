# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 00:27:40 2019

@author: 兰森
"""
import sys
sys.path.append('F:\机器学习\python程序\DFP')
from DFP import *
import matplotlib.pyplot as plt
from numpy import *
x0=mat([[-1.2],[1]])
result1=DFP(fun,gfun,x0)
n=len(result1)
fig,ax=plt.subplots(figsize=(10,8))
x=arange(0,n,1)
y=result1
ax.plot(x,y)
plt.show()
