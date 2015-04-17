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
    v.append(column[1])
    y.append(column[0])
print('\n')
t = [round(n,6) for n in y]
x = 0
plt.plot(t,v)
plt.ylabel('Time[s]')
plt.xlabel('Velocity[m/s]')

xfinal = np.trapz(v,x=t)
print 'final position= ',xfinal

N = len(t)
pos = np.zeros(N)
dist = np.zeros(N)

pos[0] = 0.
dist[0] = 0.
for i in range(1,N):
	x1 = np.trapz(v[0:i], x=t[0:i])
	x2 = np.trapz(np.abs(v[0:i]), x=t[0:i])
	pos[i] = x1
	dist[i] = x2

ax1 = plt.subplot(3,1,1)
plt.plot(t,v)
plt.ylabel('V [m/s]')
ax2 = plt.subplot(3,1,2)
plt.plot(t,pos)
plt.ylabel('Pos [m]')
ax2 = plt.subplot(3,1,3)
plt.plot(t,dist)
plt.ylabel('Distance [m]')
plt.xlabel('time [s]')

