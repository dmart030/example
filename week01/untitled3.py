# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 18:16:32 2015

@author: Lalecia
"""

def f(x):
        return x**4 - 2.*x + 1.
a = 0.
b = 2.
N = 10.

h = (a-b)/N
I = f(a) + f(b)
for k in range(1,N-1):
    I =I + 2.*f(a + k*h)
    
I = I*0.5*h
print 'results I =', I

#Page 142 of the computational physics book