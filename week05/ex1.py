# -*- coding: utf-8 -*-
"""
Created on Fri May 01 12:51:40 2015
@author: Dominic Martinez-Ta
"""
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

print " Dominc Martinez-Ta, physics 177"
print "a) "
x = np.linspace(0,1,10000)
x_prime = []
slope =  []
def f(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
for i in range(0,len(x)):
    slope.append(f(x[i])/(x[1]-x[0]))
    x_prime.append(f(x[i])-slope[i])
p = f(x)

x = np.array(x)
y = np.array(p)
slope = np.array(slope)
x_prime = np.array(x_prime)

print "     The rough values for the six roots (just be looking at it) appear to be"
print " x = 0.09, 0.25, 0.5, 0.76, 0.97"

print "b) "

for i in range(0,(len(x_prime)-1)):
    if x_prime[i] == 0:
        print x[i], " \n"
plt.plot(x,y)


'''
 a) Make a plot of P(x) from x = 0 to x=1 and inspecting it find rough values for
the six roots of the polynomial (by eye, no need to mark them). Save plot to
a .png file.
b) Write a program to solve for the positions of all six roots to an accuracy of
10^-10 using Newton’s method.

'''