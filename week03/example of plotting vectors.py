# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 01:20:57 2015

@author: Lalecia
"""
'''
import plotly.plotly as py
from plotly.graph_objs import *
from pylab import *
from visual import vector, norm, mag
'''
from pylab import imshow,show
import numpy as np
 
#electric constant
k=9e9
a = aray()
#x,y are the axis values.  X,Y are the mesh
x=np.arange(1,11,1)
y=np.arange(1,11,1)
X,Y = np.meshgrid(x, y)
print x
print y
z = x*y
imshow(z)
show()