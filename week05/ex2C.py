# -*- coding: utf-8 -*-
"""
Created on Sat May 09 20:33:49 2015

@author: D
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from cmath import sin, pi
def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c





x = np.linspace(0.,1.,1000)
y = [0 for i in range(len(x))]
for i in range(len(x)):
    y[i] = sin(pi*x[i])* sin(20*pi*x[i])
y -= (np.sum(x)/float(len(x)))    #option to remove frequency "0" contribution
coeff = dft(y)
plt.plot(np.arange(len(coeff)),np.abs(coeff)**2,linewidth=3)
