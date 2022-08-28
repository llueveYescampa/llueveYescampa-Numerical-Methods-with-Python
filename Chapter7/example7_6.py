#!/usr/bin/python3
'''
'''
## example7_6

from numpy import array, zeros
from printSoln import printSoln
from run_kut4 import integrate


def F(x,y):
    F = zeros(4)
    F[0] = y[1]
    F[1] = y[0]*(y[3]**2) - 3.9860e14/(y[0]**2)
    F[2] = y[3]
    F[3] = -2.0*y[1]*y[3]/y[0]
    return F
# end F(x,y)

def main():
    x = 0.0                         # Start of integration
    xStop = 1200.0                    # End of integration
    y = array([7.15014e6, 0.0, 0.0, 0.937045e-3])                # Initial values of {y}
    h = 50.0                         # Step size
    freq = 2                       # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
