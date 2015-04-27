# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:53:34 2015

@author: Dominic Martinez-Ta
"""

def myGauss(m):
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    ans = []
    m.reverse() 
    for sol in range(len(m)):
            if sol == 0:
                ans.append(m[sol][-1] / m[sol][-2])
            else:
                inner = 0
                #substitute in all known coefficients
                for x in range(sol):

                    ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    ans.reverse()
    return ans
print myGauss([[4.,-1,-1.,-1,5.]])
