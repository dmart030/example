# -*- coding: utf-8 -*-
"""
Created on Fri May 01 12:51:40 2015
@author: Dominic Martinez-Ta
"""
import numpy as np
import matplotlib.pyplot as plt

print " Dominc Martinez-Ta, physics 177"
print "a) "
x = np.linspace(0,1.,1000)
x_prime = []
slope =  []
def f(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
def f_prime(x):
    return (924*6)*x**5 - (2772*5)*x**4 + (3150*4)*x**3 - (1680*3)*x**2 + (420*2)*x - 42

p = f(x)

x = np.array(x)
y = np.array(p)


print "     The rough values for the six roots (just be looking at it) appear to be"
print " x = 0.03, 0.2, 0.39, 0.61, 0.89,0.94"
x_approx = [0.03, 0.2, 0.39, 0.61, 0.89, 0.94]
x_approx = np.array(x_approx)
print "b) "



i = 0 
for j in range(6):
    for i in range(10):
        b = x_approx[j]
        x_approx[j] = b - f(b)/f_prime(b)



slope = f_prime(x_approx)
z = [0 for i in range(len(x))]
z = np.array(z)
print x_approx, "approximated roots."
        
plt.plot(x,y,'-')
plt.plot(x,z,'black')
plt.xlabel("x, axis")
plt.ylabel("y, axis")
plt.title("Graph of the polynomial")
plt.savefig('barack_the_rock_obama.png')



'''
 a) Make a plot of P(x) from x = 0 to x=1 and inspecting it find rough values for
the six roots of the polynomial (by eye, no need to mark them). Save plot to
a .png file.
b) Write a program to solve for the positions of all six roots to an accuracy of
10^-10 using Newton’s method.

'''