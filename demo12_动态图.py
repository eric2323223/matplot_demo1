#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-14 下午8:21
# @Author  : Leon
# @Site    : 
# @File    : demo12_动态图.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig,ax = plt.subplots()
x=np.arange(0,2*np.pi,0.01)
line, =ax.plot(x,np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,
ani = animation.FuncAnimation(fig=fig,func=animate,init_func=init,interval=20)

plt.show()