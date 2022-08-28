#!/usr/bin/python3
'''
'''
## Problem 8
from numpy import zeros,ones,array,arange,pi
from LUdecomp3 import LUdecomp3, LUsolve3
import matplotlib.pyplot as plt


def myplot(x,y,title="my title"):
    #plt.ion()
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show()
# end myplot()


def equations(x,h,m): # Set up finite difference eqs.
    h2 = h*h
    e = ones(m)*(1.0 + 0.5*h/x[0:m])
    d = ones(m + 1)*((h2/x**2.0) - 2.0)
    c = ones(m)*(1.0 - 0.5*h/x[1:m+1])

    c[m-1] = 0.0
    e[0] = 0.0
    d[0] = 1.0
    d[m] = 1.0

    b = zeros(m+1)
    b[0] = 0.0
    b[m] = 0.638961
    return c,d,e,b
# end of equations()


def main():
    xStart = 1.0        # x at left end
    xStop = 2.0         # x at right end    
    m = 20              # Number of mesh spaces
    h = (xStop - xStart)/m
    x = arange(xStart,xStop + h,h)
    c,d,e,b = equations(x,h,m)
    c,d,e = LUdecomp3(c,d,e)
    y = LUsolve3(c,d,e,b)
    myplot(x, y, "Problem 8")    
    print ("\n        x              y")
    for i in range(m + 1):
        print ("%14.5e %14.5e" %(x[i],y[i]))
    # end for    
    input("\nPress return to exit")
        
# end of main()

if __name__ == '__main__':
    main()
