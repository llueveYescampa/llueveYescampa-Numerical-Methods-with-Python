#!/usr/bin/python3
## Problem 2(a)

from numpy import array,zeros
from math import sin 
from printSoln import printSoln
from run_kut2 import integrate

def F(x,y):    
    F = zeros(1)
    F[0] = x**2 - 4.0*y[0]
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 0.1                     # End of integration
    y = array([1.0])                # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()