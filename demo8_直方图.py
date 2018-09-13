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
y = 2**x +10

plt.bar(x,y,facecolor='red',edgecolor='b')

for x,y in zip(x,y):
    plt.text(x,y,'%.2f'%y,ha='center',va='bottom')
plt.show()