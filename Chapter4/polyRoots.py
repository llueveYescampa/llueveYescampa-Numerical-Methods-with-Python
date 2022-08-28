## module polyRoots
''' 
'''

from evalPoly import *
from numpy import zeros,complex
from cmath import sqrt
from random import random

def polyRoots(a,tol=1.0e-12):

    def laguerre(a,tol):
        x = random()
        # Starting value (random number)
        n = len(a) - 1
        for i in range(30):
            p,dp,ddp = evalPoly(a,x)
            if abs(p) < tol: return x
            g = dp/p
            h = g*g - ddp/p
            f = sqrt((n - 1)*(n*h - g*g))
            if abs(g + f) > abs(g - f): dx = n/(g + f)
            else: dx = n/(g - f)
            x = x - dx
            if abs(dx) < tol: return x
        print ('Too many iterations')
    # end laguerre   

    def deflPoly(a,root):
        # Deflates a polynomial
        n = len(a)-1
        b = [(0.0 + 0.0j)]*n
        b[n-1] = a[n]
        for i in range(n-2,-1,-1):
            b[i] = a[i+1] + root*b[i+1]
        return b
    # end deflPoly
    
    n = len(a) - 1
    roots = zeros((n),dtype=complex)

    for i in range(n):
        x = laguerre(a,tol)
        if abs(x.imag) < tol: x = x.real
        roots[i] = x
        a = deflPoly(a,x)
    return roots
    raw_input("\nPress return to exit")
    
# end of polyRoots())