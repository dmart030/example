# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:10:33 2015

@author: Dominic Martinez-Ta
"""
'''
Write a program to calculate the integral of the function: f(x) = x4 - 2x + 1, 
in the x-interval [0,2] using your functions for trapezoidal rule and Simpson’s
 rule (from Ex. 1). Use N=20 slices in both cases. Print the result to screen.
Now, compute the same integral using numpy or scipy intrinsic functions for 
trapezoidal and Simpson’s rule. Print both results to screen again. Use your 
function or the numpy/scipy to evaluate the error of the integrals for 
trapezoidal and Simpson’s rule case using the “practical estimation of errors”.
For this you will need to recompute the integrals with N=10 and apply the 
formulas we saw in class (Eq. 5.28 and 5.29 in the book). Make the program 
compare with the true result (solve the integral by hand and simply enter the 
result as a constant).
'''
import numpy as np
import scipy as sc

def f(x):
    return x**4 - 2*x + 1
    
a = 0.
b = 2.
N = 20
dx = (b-a)/N
x = a + np.arange(N+1)*dx
#x = [a+k*dx for k in range(N+1)]
print("These are the x positions")
print(x)
y = f(x)

print("Values of y per x: ")
print(y)
print("\n")


def trap(x,y):
    N = len(x)
    s = (0.5*y[0] + 0.5*y[N-1])
    for k in range(1,N-1):
        s += y[k]
   # I = (y[0]*0.5*+y[N-1]*0.5 + np.sum(y[1:N-1]))*(x[1]-x[0])
    return s*dx
    
    

def simps(x,y):
    n = len(y)
    s = y[0] + y[n-1]
 
    for i in range(1,(n/2) + 1):
        s += 4 * y[2*i - 1]
    for k in range(1,n/2):
        s += 2 * y[2*k]
        
    return s * dx / 3
 
print("Trapezoidal approximation")
w = trap(x,y)
print(w)
print("\n")
v = simps(x,y)
print("Simpson's approximation")
print v
print("\n")


print("Now we are using numpy/scipy (woops, i did that in ex1)\n")
print("Y is now and array and so is x")
a = 0.
b = 2.
N = 10
dx = (b-a)/N
x = a + np.arange(N+1)*dx
x = np.array(x)
y = np.array(y)

f = np.trapz(y, x=None, dx=0.1)
c = 4.4
print("using numpy/scipy functions built into python.(That was what you were asking for right?)\n")
print "trapezoidal approximation: ",f, "The error is: ", round(f - c,5)
print "The error of each trapezoid is  ~", (f - c )/(21*3)
g = sc.integrate.simps(y,x=None,dx=0.1)
print "\n"
print "Simpson approximation: ", g, "The error is: ", round(g - c,5)
print "\n"
print "The actual integral of the problem is is 4.4"
l = []
L = []
def er1(y):
    for i in range(N-1):
        L.append(round((y[i+1]-y[i])*1./3,4))
    return L
    
print "The errors of each trapezoid is: "
print er1(y)

def er2(y):
    for i in range(N-1):
        l.append(round((y[i+1]-[y[i]])*1./15,4))
    return l
print "The errors of each simpson trapezoid thingy is: "
print er2(y)

'''
Now, compute the same integral using numpy or scipy intrinsic functions for 
trapezoidal and Simpson’s rule. Print both results to screen again. Use your 
function or the numpy/scipy to evaluate the error of the integrals for 
trapezoidal and Simpson’s rule case using the “practical estimation of errors”.
For this you will need to recompute the integrals with N=10 and apply the 
formulas we saw in class (Eq. 5.28 and 5.29 in the book). Make the program 
compare with the true result (solve the integral by hand and simply enter the 
result as a constant).
'''