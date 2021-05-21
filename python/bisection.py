# Python code for bisection method for finding the zero of a function

import numpy as np

def f(x):
    return np.sin(x)

def bisection(a,b,tol):
    xl=a
    xr=b
    while (np.abs(xl-xr)>=tol):
        c = (xl+xr)/2.0
        prod = f(xl)*f(c)
        if prod > tol:
            xl=c
        else:
            if prod < tol:
                xr=c

    return c

answer = bisection(-5,5,1e-8)
print("Num:", answer)
