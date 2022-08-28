#!/usr/bin/python3
'''
'''
## Problem 6 
from numpy import zeros,ones,array,arange,pi
from LUdecomp3 import LUdecomp3, LUsolve3


def equations(x,h,m): # Set up finite difference eqs.
    h2 = h*h
    
    c = ones(m)
    d = ones(m + 1)*(2.0 + x*h2)
    e = ones(m)

    b = zeros(m+1)
    b[0] = 1.5
    b[m] = 3.0
    
    c[m-1] = 0.0
    e[0] = 0.0
    d[0] = 1.0
    d[m] = 1.0
    
    
    return c,d,e,b
# end of equations()


def main():
    xStart = 1.0        # x at left end
    xStop = 2.0      # x at right end    
    m = 20              # Number of mesh spaces
    h = (xStop - xStart)/m
    x = arange(xStart,xStop + h,h)
    c,d,e,b = equations(x,h,m)
    c,d,e = LUdecomp3(c,d,e)
    y = LUsolve3(c,d,e,b)
    print ("\n        x              y")
    for i in range(m + 1):
        print ("%14.5e %14.5e" %(x[i],y[i]))
    # end for    
    input("\nPress return to exit")
        
# end of main()

if __name__ == '__main__':
    main()
