#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-13 下午7:59
# @Author  : Leon
# @Site    : 
# @File    : demo8_直方图.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(10)
y = 2*x +10
print(x)
y[5]=-10
plt.bar(x,y,facecolor='b',edgecolor='r')

for x,y in zip(x,y): #zip-->把x,y结合一个整体，一次读取x,y值
    plt.text(x,y,'%.3f'%y,ha='center',va='bottom')
plt.show()