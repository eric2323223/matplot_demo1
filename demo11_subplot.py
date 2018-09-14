#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-14 下午8:15
# @Author  : Leon
# @Site    : 
# @File    : demo11_subplot.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
'''
plt.figure()
plt.subplot(2,2,1)
plt.plot([0,1],[0,1]) #画一条直线

plt.subplot(2,2,2)
plt.plot([0,1],[0,2]) #画一条直线

plt.subplot(2,2,3)
plt.plot([0,1],[0,3]) #画一条直线

plt.subplot(224)
plt.plot([0,1],[0,3]) #画一条直线

plt.show()
'''
plt.figure()
plt.subplot(2,1,1)
plt.plot([0,1],[0,1]) #画一条直线

plt.subplot(2,3,4)
plt.plot([0,1],[0,2]) #画一条直线

plt.subplot(2,3,5)
plt.plot([0,1],[0,3]) #画一条直线

plt.subplot(236)
plt.plot([0,1],[0,3]) #画一条直线

plt.show()