# -*- coding: utf-8 -*-
"""
Created on Sat May 09 20:56:58 2015

@author: D
"""
import numpy as np
import matplotlib.pyplot as plt


DataIN = np.loadtxt('sunspots.txt')

t = DataIN[:,0]
y = DataIN[:,1]

plt.plot(t,y)
plt.xlabel("time[months]")
plt.ylabel("number of sunspots")
print "estimate of length 6 months"
months = 6