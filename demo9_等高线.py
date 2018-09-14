#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-14 下午7:48
# @Author  : Leon
# @Site    : 
# @File    : demo9_等高线.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,100)
y = np.linspace(-3,3,100)

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

#将原始数据变成网格数据
X,Y=np.meshgrid(x,y)
plt.contour(X,Y,f(X,Y),10,alpha=0.8,cmap=plt.cm.hot)

C=plt.contour(X,Y,f(X,Y),10,colors='black',linewidth=0.5)
plt.clabel(C,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()