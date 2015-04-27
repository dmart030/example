# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:53:34 2015

@author: Dominic Martinez-Ta
"""
'''
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
print myGauss([[4.,-1.,-1.,-1.,5.],[-1.,3.,0.,-1.,0.],
               [-1.,0.,3.,-1.,5.],[0.,-1.,-1.,4.,5.]])
'''
import numpy as np

def forward_elimination(A, b, n):
    """
    Calculates the forward part of Gaussian elimination.
    """
    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = A[i,row] / A[row,row]
            for j in range(row, n):
                A[i,j] = A[i,j] - factor * A[row,j]

            b[i] = b[i] - factor * b[row]

        print('A = \n%s and b = %s' % (A,b))
    return A, b

def back_substitution(a, b, n):
    """"
    Does back substitution, returns the Gauss result.
    """
    x = np.zeros((n,1))
    x[n-1] = b[n-1] / a[n-1, n-1]
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = sums - a[row,j] * x[j]
        x[row] = sums / a[row,row]
    return x

def gauss(A, b):
    """
    This function performs Gauss elimination without pivoting.
    """
    n = A.shape[0]

    # Check for zero diagonal elements
    if any(np.diag(A)==0):
        raise ZeroDivisionError(('Division by zero will occur; '
                                  'pivoting currently not supported'))

    A, b = forward_elimination(A, b, n)
    return back_substitution(A, b, n)

# Main program starts here
if __name__ == '__main__':
    A = np.array([[4,   -1,   -1, -1],
                  [-1, 3,  0, -1],
                  [-1,   0, 3, -1],
                  [-1, -1,  -1, 4]])
    b = np.array([5, 0, 5, 0])
    x = gauss(A, b)
    print('Gauss result is x = \n %s' % x)
    




