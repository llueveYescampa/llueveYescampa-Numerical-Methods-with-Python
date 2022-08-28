#!/usr/bin/python3
'''
    Included by edgar black
'''
## example 9.12 Heat Book

from numpy import array,zeros
from math import sin 
from printSoln import printSoln
from run_kut4 import integrate

def F(x,y):    
    order=1
    F = zeros(order)
    F[0] = -2.0*x*y[0]
    return F
# end F(x,y)


def main():
    xStart = 0.0                    # Start of integration
    xStop = 0.5                     # End of integration
    h = 0.25                        # Step size
    freq = 1                        # Printout frequency
    x,y = integrate(F,xStart,array([1.0]),xStop,h)
    printSoln(x,y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
