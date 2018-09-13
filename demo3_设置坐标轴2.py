#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-7 下午8:07
# @Author  : Leon
# @Site    : 
# @File    : demo3_设置坐标轴2.py
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
plt.yticks([-1,0,1,2,3],['level1','level2','level3','level4','level5'])
plt.xticks(new_ticks)

#gca get current axis
#设置坐标轴边框
ax = plt.gca()
ax.spines['right'].set_color('red')
ax.spines['top'].set_color('none')

#把X轴的刻度设置为bottom，Y设置位'left'
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#设置bottom,left到零点
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.plot(x,y1,color='red',linewidth=5.0,linestyle='-')
plt.plot(x,y2,color='blue',linewidth=1.0,linestyle='--')
plt.show()