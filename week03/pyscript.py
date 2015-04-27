# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 01:20:57 2015

@author: Lalecia
"""
import plotly.plotly as py
from plotly.graph_objs import *
from pylab import *
from visual import vector, norm, mag
 
#you need to add your own plot.ly credentials here
#py.sign_in(dmart031)
 
#electric constant
k=9e9
 
#x,y are the axis values.  X,Y are the mesh
x=arange(0,.05,0.001)
y=arange(0,.05,0.001)
X,Y = meshgrid(x, y)
 
#q1 and q2 are the vector locations of the two charges
q1=vector(0.02, 0.02, 0)
q2=vector(0.03, 0.03, 0)
 
#these are the charge values
q1q=1e-6
q2q=-1e-6
 
#V is the potential.  This next line puts in zero for every value.
V=X*0
 
#In order to have a well behaved plot, Vmax sets the upper and lower limit
Vmax=4e6
 
#This double loop goes through all the values in the mesh
for i in range(len(X[:,0])):
    for j in range(len(Y[0,:])):
        #r_loc is the vector observation location based on x,y
        r_loc=vector(X[i,j],Y[i,j],0)
 
        #r1 is the vector from charge 1 to observation location
        r1=r_loc-q1
        #r2 is the vector from charge 2 to observation location
        r2=r_loc-q2
 
        #if the observation location is on either of the charge charges
        #do not computer V (it would be a division by zero)
        if mag(r1) !=0 and mag(r2)!=0:
            #calculate V
            V[i,j]=k*q1q/mag(r1) + k*q2q/mag(r2)
            #if V is too high, limit it
            if V[i,j]>=Vmax: V[i,j]=Vmax
            if V[i,j]<=-Vmax: V[i,j]=-Vmax
 
 
#the plotting part
data=[{'x':x, 'y':y, 'z':V, 'type':'contour'}]
plot_url = py.plot(data, filename='electric potential_v2')