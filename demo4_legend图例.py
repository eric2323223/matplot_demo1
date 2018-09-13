#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-7 下午8:19
# @Author  : Leon
# @Site    : 
# @File    : demo4_legend图例.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

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

L1,=plt.plot(x,y1,color='red',linewidth=5.0,linestyle='-')
L2,=plt.plot(x,y2,color='blue',linewidth=1.0,linestyle='--')

plt.legend([L1,L2],['test1','test2'],loc='upper right')

#blue_line = mlines.Line2D([], [], color='blue', marker='*',markersize=15, label='Blue stars')
#plt.legend(handles=[blue_line])

plt.show()