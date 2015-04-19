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
def f(x):
     return m.sin(2)*m.sqrt(100*x)

a = 0.
b = 1.
N = range(input("Number of steps that you want: ") + 1)
x = 0.
l = []
N.pop(0)
print "The nsteps are numbered:", N, '\n'
def h(N):
    for r in range(0, len(N)):
        l.append(round((b - a) / N[r],5))
    return l
l = h(N)
i = []
I = 0.
def I(I):
    for i in range(len(N)):
        I = I + l[i]*(0.5*f(a)+0.5*f(b))
    return I
print I(I)
 
 