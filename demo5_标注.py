#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-12 下午8:04
# @Author  : Leon
# @Site    : 
# @File    : demo5_标注.py
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

plt.plot(x,y1,color='red',linewidth=2.0,linestyle='-')
plt.plot(x,y2,color='blue',linewidth=1.0,linestyle='--')

x0=0.5
y0=2*x0 + 1
#画点
plt.scatter(x0,y0,s=100,color='b')
#画虚线
plt.plot([x0,x0],[y0,0],'g--',lw=2)

plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xytext=(+30,-30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

plt.text(-2,2,r'$this\ is\ the\ text$',fontdict={'size':'24','color':'b'})
plt.show()