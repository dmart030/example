# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 02:22:55 2015

@author: Dominic Martinez-Ta
"""
'''
2) Download from the github repository of the course 
(https://github.com/lsales/rep_Phys177),the file called “velocities.txt” in the
 “extra_info_labs” folder (just make “git pull” if you have already cloned the 
 repository before). This file has 2 columns, time t in seconds (1st column), 
 and the x-velocity velocity in meters persecond of a particle, measured once 
 every second from time t=0 to t=100. Write a program to do the following: 
 • Read in the data and calculate the approximate distance traveled by the 
 particle in the x direction as a function of time. Use your functions to 
 compute this using the trapezoidal rule and the Simpson’s rule. Print results 
 to a file in both cases.
• Extend your program to make a graph that shows both, the original velocity 
curve and the distance curve, in two separate panels of the same figure.
 Hint: Use plt.subplot(2, 1, j), where j = 1 or 2 for upper/lower panels.
'''
import numpy as np
import matplotlib.pyplot as plt
DataIN = np.loadtxt('Velocities.txt.txt')
y = []
v = []
for column in DataIN:
    v.append(column[0])
    y.append(column[1])
print('\n')
t = [round(n,6) for n in y]

plt.plot(v,t)
plt.xlabel('Time')
plt.ylabel('Velocity')

def trap(v):
    N = len(v)
    dx = v[1]-v[0]
    x_sum = (v[0]+v[N-1])*0.5
    i = 0
    
    while i in range(1,N-1):
        x_sum += v[i]
    return x_sum*dx
    
def simps(v):
    N = len(v)
    dx = (100)/6
    

print( "Trapezoidal approximation & position coordinates",trap(x))
