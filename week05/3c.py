# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:44:47 2015

@author: Lalecia
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft #or fft

DataIN = np.loadtxt('sunspots.txt')

t = DataIN[:,0]
y = DataIN[:,1]

coef =  fft(y)

plt.plot(t,abs(coef))