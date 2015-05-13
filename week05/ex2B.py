# -*- coding: utf-8 -*-
"""
Created on Sat May 09 20:29:25 2015

@author: D
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c


x = np.linspace(0.,1.,1000)
y = signal.sawtooth(2 * np.pi * 5 * x)
y -= (np.sum(y)/float(len(x)))    #option to remove frequency "0" contribution
coeff = dft(y)
plt.plot(np.arange(len(coeff)),np.abs(coeff)**2,linewidth=3)
