#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-7 下午7:48
# @Author  : Leon
# @Site    : 
# @File    : demo1_figure.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,100)
y1=2*x+1
y2=x**2

#figure1
plt.figure(figsize=(5,5)) #figure大小
plt.plot(x,y1,color='red',linewidth=5.0,linestyle='-')

#figure2
plt.figure()
plt.plot(x,y2,color='blue',linewidth=1.0,linestyle='--')
plt.show()