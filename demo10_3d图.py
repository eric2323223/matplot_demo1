#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-14 下午8:02
# @Author  : Leon
# @Site    : 
# @File    : demo10_3d图.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

x= np.arange(-4,4,0.2)
y= np.arange(-4,4,0.2)
X,Y = np.meshgrid(x,y)
R = np.sqrt(X**2+Y**2)
Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
#映射，实际上也就是等高线图
#zdir:沿这个方向投影
#'offset': 投影位置
ax.contour(X,Y,Z,zdir='z',offset=-4,cmap='rainbow')
ax.set_zlim(-2,2)
plt.show()