#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-12 下午8:26
# @Author  : Leon
# @Site    : 
# @File    : demo7_散点图.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

plt.scatter(np.arange(5),np.arange(5))

x=np.random.normal(0,1,500)
y=np.random.normal(0,1,500)
plt.scatter(x,y,s=50,c='r',alpha=0.5)

plt.xlim((-2,2))
plt.ylim((-2,2))

plt.xticks(())
plt.yticks(())
plt.show()