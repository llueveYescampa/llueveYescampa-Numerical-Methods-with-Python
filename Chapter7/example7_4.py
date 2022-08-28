#!/usr/bin/python3
## example7_4

from numpy import array,zeros
from printSoln import printSoln
from run_kut4 import integrate

def F(x,y):    
    F = zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1] - x
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 2.0                     # End of integration
    y = array([0.0, 1.0])           # Initial values of {y}
    
    
    h = 0.25                        # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
