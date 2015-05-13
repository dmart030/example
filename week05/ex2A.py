# -*- coding: utf-8 -*-
"""
Created on Sat May 09 15:41:14 2015

@author: Dominic Martinez-Ta
"""
'''
Write a program to calculate the coefficients in the discrete Fourier
 transforms of the following periodic functions sampled at N=1000 evenly
 spaced points, and make plots of their amplitudes 
 (similar to Figure 7.4 in the book):
a) A single cycle of a square-wave with amplitude 1
b) The sawtooth wave yn = n
c) The modulated sine wave yn = sin(pi*n/N) * sin(20*pi*n/N) 
'''
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


x = np.linspace(0.,6,1000)
#y = np.ones(len(x))    #example for a function y(x) = constant
y = signal.square(x)

#y = x                   #example for a function y(x) = x
y -= (np.sum(y)/float(len(x)))  

coeff = dft(y)
plt.plot(np.arange(len(coeff)),np.abs(coeff)**2,linewidth=3)
plt.title('A) A single cycle of a square wave with amplitude 1')











