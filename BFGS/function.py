# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 00:27:40 2019

@author: 兰森
"""
from  numpy import *
def fun(x):
    result=100*(x[0,0]**2-x[1,0])**2+(x[0,0]-1)**2
    return result
def gfun(x):
    result=zeros((2,1))
    result[0,0]=400*(x[0,0]**2-x[1,0])*x[0,0]+2*(x[0,0]-1)
    result[1,0]=-200*(x[0,0]**2-x[1,0])
    return result


