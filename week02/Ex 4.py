# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 01:24:34 2015

@author: Dominic Martinez-Ta
"""
'''
Consider the integral of the function f(x) = sin2 * sqrt(100x) in the range 
x=[0,1] Write a program that uses the adaptive trapezoidal rule method 
(Eq. 5.34) to calculate the value of this integral to an approximate accuracy 
of e=10-6 (i.e. correct to six digits after the decimal point). Start with a 
single integration slice and work up from there to two, four, eight and so forth.
Have the program print out the number of slices, its estimate of the integral, 
and its estimate of the error on the integral, for each value of the number
 of slices N, until the target accuracy is reached. 
 (Hint: you should find the result around I=0.45)
 '''
import math as m
import numpy as np
import scipy as scy
def f(x):
     return m.sin(((100*x))**0.5)

a = 0.
b = 1.
N = range(input("Number of steps that you want: ") + 1)
x = 0.
l = []
N.pop(0)
print "The steps are numbered:", N, '\n'
def h(N):
    for r in range(0, len(N)):
        l.append((b - a) / N[r])
    return l
l = h(N)
i = []
I = 0.
print l
x = 0
y = f(x)
np.array(l)
s = (0.5*f(a) + 0.5*f(b))
for k in range(1,len(l)-1, 2):
    s += f(a + k*l[k])
for i in range(0,len(l)/2):
    print s * l[i]*2
for i in range(0,len(l) - 1):
    print "error of each trapezoid", (1./3)*(s*(l[i+1]-l[i]))*-1


