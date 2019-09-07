# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 00:27:40 2019

@author: 兰森
"""

import sys
sys.path.append('F:\机器学习\python程序\DFP')
from function import *
from numpy import *
##x0为列
def DFP(fun,gfun,x0):
    result=[]
    iter=0
    max_iter=500
    rho=0.55
    sigma=0.4
    num_dim=shape(x0)[0]
    Gk=eye(num_dim)
    while(iter<max_iter):
        gk=mat(gfun(x0))
        pk=-mat(Gk)*gk#使用矩阵乘法
        m=0
        mk=0
        while(m<20):
            newf=fun(x0+rho**m*pk)
            oldf=fun(x0)
            if(newf<oldf+sigma*rho**m*gk.T*pk):
                mk=m
                break
            m=m+1
            
        #DFP校正
        x=x0+rho**m*pk
        sk=x-x0
        yk=gfun(x)-gk #误差
        if(sk.T*yk>0):
            Gk=Gk+(sk*sk.T)/(sk.T*yk)-(Gk*yk*yk.T*Gk)/(yk.T*Gk*yk)
        iter=iter+1
        x0=x
        result.append(fun(x0))
    return result 

