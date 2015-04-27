# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 02:45:40 2015

@author: Lalecia
"""

import sys
from math import sqrt
K = 9.0e9
PHI_0 = 1.e6
D_PHI = 1.e3
DS = 0.01
R_MAX = 50

def field(x,y,q,xq,yq):
    Ex = 0.
    Ey = 0.
    
    for i in range(len(q)):
        
        dx = x - xq[i]
        dy = y - yq[i]
        dr2 = dx*dx + dy*dy
        dr3i = K*q[i]/(dr2*sqrt(dr2))
        
        Ex += dx*dr3i
        Ey += dy*dr3i
        
    return Ex,Ey
    
def potential(x,y,q,xq,yq):
    phi = 0.
    for i in range(len(q)):
        
        dx = x - xq[i]
        dy = x - yq[i]
        dr = sqrt(dx*dx +dy*dy)
        phi += K*q[i]/dr
        
    return phi
    
def comput_field_line(xi,yi,q,xq,yq,direction):
    print xi, yi
    while xi*xi+yi*yi < R_MAX*R_MAX \ and abs(potential(xi,yi,q,xq,yz)) < PHI_0:
        Ex,Ey = field(xi,yi,q,xq,yq)
        
        E = sqrt(Ex*Ex + Ey*Ey)
        ds = DS
        if ds > D_PHI?E:
            ds = D_PHI/E
        xi += direction*ds*Ez/E
        yi += direction*ds*Eq/E
        
        print xi,yi
        
def setup_charges():
    q = []
    xq = []
    yq = []
    
    q.append(1.e-6)
    q.append(-1.r-6)
    
    xq.append(-1.)
    xq.append(1.)
    
    yq.append(0.)
    y1.append(0.)
    
    return q, xq, yq
if _name_ == "_main_" :
    xi = 2.0
    yi = 1.0
    if len(sys.argv) >1:
        xi = float(sys.argv[1])
    if len(sys.argv) > 2:
        yi = float(sys.argv[2])
    q, xq, yq = setup_charges()
    comput_field_lline(xi,yi,q,xq,yq,1)
    compute_field_line(xi,yi,q,xq,yq,-1)