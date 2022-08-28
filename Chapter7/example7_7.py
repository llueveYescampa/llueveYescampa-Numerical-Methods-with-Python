#!/usr/bin/python3
'''
    Included by edgar black
    solved using Runge-Kutta
'''
## example7_7

from numpy import array, zeros, exp
from printSoln import printSoln
from run_kut4 import integrate


def F(x,y):    
    F = zeros(2)
    F[0] = y[1]
    F[1] = -19.0*0.25*y[0]-10*y[1]
    return F
# end F(x,y)

def main():
    x = 0.0                         # Start of integration
    xStop = 10.0                    # End of integration
    y = array([-9.0, 0])            # Initial values of {y}
    h = 0.1                         # Step size
    freq = 10                       # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
