# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 02:14:31 2015

@author: Dominic Martinez-Ta
"""

from math import pi,sqrt
import numpy as np
from pylab import imshow, show

r = [i for i in range(1,11)]
a = np.array([r,r],float)

xi = np.empty([11,11],float)

e0 = 8.854187817
x1 = 10./2 + 0.5
y1 = 10./2
x2 = 10./2 - 0.5
y2 = 10./2

for i in range(1,11):
    y = i
    for j in range(1,11):
     x = j
     r1 = sqrt((x-x1)**2 +(y-y1)**2)
     r2 = sqrt((x-x2)**2 +(y-y2)**2)
     xi[i,j] = (1/(4*pi*e0))*((1/r1)+(1/r2))
imshow(xi,origin = "lower",extent = [0,10,0,10])
show()