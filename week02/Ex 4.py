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














'''

#Calculate the first approximation I1 to the integral using the chosen
#value N1 with the standard trapezoidal rule formula (Eq. 5.3).
I1 = (0.5*f(a) + 0.5*f(b))*h

#Display Results
print "Slices: ", N1, "   Integral:", I1,"   Error: ", error

Ii = I1
Ni = 2*N1
I = 0.5*Ii
error = 1

#Double the number of steps and use Eq. 5.34 to calculate an improved 
#estimate of the integral. Also calculate the error on that estimate 
#from Eq. 5.30. If the absolute magnitude of the error is less than the
#target accuracy for the integral, stop. Otherwise repeat above.

while( error > 10**(-6) ):
    hi = (b-a)/Ni
    
    for n in range(1,Ni-1,2):
        I += (f(n*hi))*hi
        
    error = (1/3.)*(abs(I-Ii))
    print "Slices: ", Ni, "   Integral:", I,"   Error: ", error
    Ii = I
    I = 0.5*I
    Ni = 2*Ni
'''