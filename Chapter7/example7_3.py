#!/usr/bin/python3
## example7_3

from numpy import array,zeros
from math import sin 
from printSoln import printSoln
from run_kut4 import integrate

def F(x,y):    
    F = zeros(1)
    F[0] = sin(y[0])
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 0.5                     # End of integration
    y = array([1.0])                # Initial values of {y}
    h = 0.10                        # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
