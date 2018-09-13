#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-7 下午7:47
# @Author  : Leon
# @Site    : 
# @File    : demo2_设置坐标轴.py
# @Software: PyCharm


import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,100)
y1=2*x+1
y2=x**2

#xy范围
plt.xlim(-1,2)
plt.ylim((-2,3))

#x,y描述
plt.xlabel('I am X')
plt.ylabel('I am Y')

new_ticks = np.linspace(-2,2,11)
print(new_ticks)
#plt.yticks([-1,0,1,2,3],['level1','level2','level3','level4','level5'])
plt.xticks(new_ticks)
plt.plot(x,y1,color='red',linewidth=5.0,linestyle='-')
plt.plot(x,y2,color='blue',linewidth=1.0,linestyle='--')
plt.show()