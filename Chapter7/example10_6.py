#!/usr/bin/python3
'''
    Included by edgar black
'''
## example 10.6 Heat Book -- Shooting method

from numpy import array,zeros
from math import sin 
from printSoln import printSoln
from run_kut4 import integrate

def F(x,y):    
    order=2
    F = zeros(order)
    F[0] = y[1]
    F[1] = 6*x
    return F
# end F(x,y)


def main():
    xStart = 0.0                    # Start of integration
    xStop = 1.0                     # End of integration
    h = 0.50                        # Step size
    freq = 1                        # Printout frequency
    x,y = integrate(F,xStart,array([0.0,0.0]),xStop,h)
    printSoln(x,y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
