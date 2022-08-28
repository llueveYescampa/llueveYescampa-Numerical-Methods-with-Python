#!/usr/bin/python3
'''
'''
## example7_8

from numpy import array,zeros
from run_kut5 import integrate
from printSoln import printSoln
from math import exp

def F(x,y):
    F = zeros(2)
    F[0] = y[1]
    F[1] = -9.80665 + 65.351e-3 * y[1]**2 * exp(-10.53e-5*y[0])
    return F
# end F(x,y)

def main():
    x = 0.0                         # Start of integration
    xStop = 10.0                    # End of integration
    y = array([9000.0, 0.0])        # Initial values of {y}
    h = 0.5                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h, 1.0e-2)
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
