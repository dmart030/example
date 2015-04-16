# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:38:08 2015

@author: Dominic Martinez-Ta
"""
'''
 Create your own functions to compute integrals using the trapezoidal rule and 
 Simpson’srule. These functions should take as input an array with the x  and y
 values of the function to be integrated. Hint: notice that the book has an 
 example program to execute the trapezoidal rule already, Sec. 5.1, Example 5.1
'''

print("We are inputting an equation indirectly, by determining the")
print(" coeficients and the power of each variable.\n")
print("note: we are only doing this for equations of x and not log/sing/etc.")
print("This also requires input from the User, so be paitent, :)")

x_max = input("Input the highest power(of x) for your equation: ")
print("The powers of x are: ")
x_pow_vect = [1*n for n in range(x_max + 1)]

print(x_pow_vect)

print("Now we will ask for the bounds of your equation")
bound_a = input("Input the minimum bound: ")
bound_b = input("Input the maximum bound: ")

print("Now we will ask for the coeficients of each x.(starting from x^0")
print("and increasing by 0+1)")
a_coef = []
i = 0
for i in range(x_max+1):
    a_coef.append(input("coefficient(with decimal point please): "))
print("The coefficients of the equation [C,CX,CX^2,...CX^n] are:")
print(a_coef)

print("So your equation is: [coefficient, X, power ]")
i = 0

for i in range(x_max+1):
    print(a_coef[i],'*x^',x_pow_vect[i])
N = input("How many intervals would you like? ")
float(N)

print("Now we have enough information to calculate the integrand via")
print("Trapezoidal, and Simpsons methods\n")
print("The Trapezoidal area is: ")
h = (bound_b-bound_a)
s = 0
sum1 = []
'''
for s in range(x_max):
    if s == 0:
        sum1.append(0.5*a_coef[s])
    else:
        sum1.append(0.5*(a_coef[s] * ((bound_a + (s/x_max)*h)**x_pow_vect[i])))
x = 0
s = 0
for x in range(x_max):
    s += sum1[x]
print(0.5*(s + 0.5*a_coef[0] + 0.5*a_coef[x_max]*(bound_b**x_pow_vect[x_max])))

print("Simpson's rule is: ")
h1 = h/N
m = bound_a*0.5 + bound_b*0.5
print(h1*(s + m + a_coef[0] + a_coef[x_max]*(bound_b**x_pow_vect[x_max])))
'''
def f(x):
    return sum(c_coef[]*x[]**x_pow_vect[])