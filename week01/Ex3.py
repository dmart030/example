# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 16:26:52 2015

@author: Dominic Martinez-Ta
Physics 177
lab1
Ex.3
"""
import matplotlib.pyplot as plt
import numpy as np

print"3)A ball drops from a very tall tower.\n"
print"3a.\n"

print"To find the time it takes to hit the ground,"
print"we use vt+0.5gt^2 = h -> 0.5gt^2+vt-h = 0"
print"which can then be simplified to \n"
print"(-v+sqrt(v^2+2gh))/g\n"
print"where g is the gravitational constant 9.81 m/s^2\n"
print"Therefore the time it takes to hit the ground is: \n"
G = 9.81*0.5
H = 800.

print" t = ((-1)*V+(V^2+4GH))/G"

print"3b)"
Vmin = input('Input minimum velocity: ')
Vmax = input('Input Maximum velocity: ')

dV = (Vmax-Vmin)/10.

v = []
t = []
i = 0
g = 0
w = 0
for i in range(11):
    v.append((i * dV) + Vmin)
for w in range(11):
    t.append((((-1)*(v[w]))+((v[w]**2 + (4*G*H))**0.5))/(2*9.81))
    round(t[w],2)
    
t = [round(n,2) for n in t]

plt.plot(v,t,'-o')
plt.xlabel('Velocity')
plt.ylabel('Time')
print("Velocity list")
print(v)
print("time list")
print(t)
t1 = np.array(t)
np.savetxt('file.dat',t1)
