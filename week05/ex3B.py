# -*- coding: utf-8 -*-
"""
Created on Sat May 09 21:24:44 2015

@author: D
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft #or fft

DataIN = np.loadtxt('sunspots.txt')

t = DataIN[:,0]
y = DataIN[:,1]
'''
def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c
'''
#coefficients will be fft of the function qed (remember to remove the min)
print "estimate of length 6 months"
months = 6
coef =  fft(y)

#y -= (np.sum(y)/float(len(t)))    #option to remove frequency "0" contribution

plt.plot(np.arange(len(coef)),np.abs(coef)**2,linewidth=3)
plt.xlabel('sunspot signal')
plt.ylabel('power spextrum')
plt.title('3b')