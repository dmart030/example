# -*- coding: utf-8 -*-
"""
Created on Sat May 09 21:24:44 2015

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

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

print "estimate of length 6 months"
months = 6





y -= (np.sum(t)/float(len(t)))    #option to remove frequency "0" contribution

coeff = dft(y)
plt.plot(np.arange(len(coeff)),np.abs(coeff)**2,linewidth=3)
