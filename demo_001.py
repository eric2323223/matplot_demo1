#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-7 下午7:45
# @Author  : Leon
# @Site    : 
# @File    : demo_001.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,100)
y=2*x+1
plt.plot(x,y)
plt.show()