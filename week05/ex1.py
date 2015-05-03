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
x = np.linspace(0,1,1000)
x_prime = []
slope =  []
def f(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
def f_prime(x):
    return 924*6*x**5 - 2772*5*x**4 + 3150*4*x**3 - 1680*3*x**2 + 420*2*x - 42

p = f(x)

x = np.array(x)
y = np.array(p)


print "     The rough values for the six roots (just be looking at it) appear to be"
print " x = 0.09, 0.25, 0.5, 0.76, 0.97"

print "b) "

slope = f_prime(x)
slope1 = np.around(slope, decimals = 1)
f = np.around(x,decimals = 3)
for i in range(len(x)):
    if slope1[i] == 0:
        if f[i+1] != f[i]:
            print f[i], "Actual 0, x coordinate calculated from slope."
print "If there are 2 points very close to eachother. It just meant that the slope was somewhat flat."
print "Meaning, the 0 root is inbetween the two values."
x_i = x[:]-slope[:]
print x_i

plt.plot(x,y)
'''
plt.savefig('barack_the_rock_obama.png')
'''


'''
 a) Make a plot of P(x) from x = 0 to x=1 and inspecting it find rough values for
the six roots of the polynomial (by eye, no need to mark them). Save plot to
a .png file.
b) Write a program to solve for the positions of all six roots to an accuracy of
10^-10 using Newton’s method.

'''