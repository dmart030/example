# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:53:01 2015

@author: Dominic Martinez-Ta
"""
'''
Download from the github repository of the course 
(https://github.com/lsales/rep_Phys177),
the file called “velocities.txt” in the “extra_info_labs” folder 
(just make “git pull” if you have
already cloned the repository before).
This file has 2 columns, time t in seconds (1st column), and the x-velocity 
velocity in meters per
second of a particle, measured once every second from time t=0 to t=100.
Write a program to do the following:
• Read in the data and calculate the approximate distance traveled by the 
particle in the x
direction as a function of time. Use your functions to compute this using the 
trapezoidal rule
and the Simpson’s rule. Print results to a file in both cases.
• Extend your program to make a graph that shows both, the original velocity 
curve and the
distance curve, in two separate panels of the same figure. Hint: Use 
plt.subplot(2, 1, j), where
j = 1 or 2 for upper/lower panels.
'''
from math import *
from pylab import *
'''
Simpsons rule
'''
def simpson(f, a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,n/2 + 1):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,n/2):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)
'''
Trapezoidal rule
'''
def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h

print( trapezoidal(lambda x:x**2, 5, 10, 100))
