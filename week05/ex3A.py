# -*- coding: utf-8 -*-
"""
Created on Sat May 09 20:56:58 2015

@author: D
"""
import numpy as np
import matplotlib.pyplot as plt

DataIN = np.loadtxt('sunspots.txt')
y = []
t = []
for column in DataIN:
    y.append(column[1])
    t.append(column[0])

t = np.array(t)
y = np.array(y)


plt.plot(t,y)




#error when i try to label the axis.
#plt.xlim('time[months]')
#plt.ylim('number of sunspots')