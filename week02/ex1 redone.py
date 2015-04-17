# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:41:47 2015
@author: Dominic Martinez-Ta
"""
import numpy as np
import scipy as py

def f(x):
    return py.poly1d(input("Input coefficients of equation i.e [1,0,0,-2,1]: "))
    
a = input("Minimum boundary? ")
b = input("Maximum boundaray? ")
N = input("How many N's? ")
dx = (b-a)/N
x = a + np.arange(N+1)*dx
#x = [a+k*dx for k in range(N+1)]
print("These are the x positions")
print(x)
y = f(x)

print("Your equation is: \n")
print(y)
print("\n")


def trap(x,y):
    N = len(x)
    h = (x[1]-x[0])
    s = (0.5*y(a) + 0.5*y(b))
    for k in range(1,N-1):
        s += y(a + k*dx)
   # I = (y[0]*0.5*+y[N-1]*0.5 + np.sum(y[1:N-1]))*(x[1]-x[0])
    return s*h
    
    
def simps(x,y):
    h = (b - a) / N
    s = y(a) + y(b)
 
    for i in range(1, N, 2):
        s += 4 * y(a + i * h)
    for i in range(2,  N, 2):
        s += 2 * y(a + i * h)
 
    return s * h / 3
    
print("Trapezoidal approximation")
w = trap(x,y)
print(w)
print("\n")
print("Simpson's approximation")
print(round(simps(x,y), 3))
print("\n")
print("On a side note, Thank you so much for having the patience to help me! :)")
