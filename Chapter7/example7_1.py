#!/usr/bin/python3
'''
    Included by edgar black
'''
## example7_1

from numpy import array, zeros
from printSoln import printSoln 
from taylor import taylor

def deriv(x,y):
    D = zeros((4,1))
    D[0] = [-4.0*y[0] +  x**2]
    D[1] = [16.0*y[0] - 4.0*x**2 + 2 *x]
    D[2] = [-64.0*y[0] + 16.0*x**2 - 8.0*x + 2.0]
    D[3] = [256.0*y[0] - 64.0*x**2 + 32.0*x - 8.0]
    return D
#end deriv   

def main():
    x = 0.0                         # Start of integration
    xStop = 0.1                     # End of integration
    y = array([1.0])                # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = taylor(deriv,x,y,xStop,h)
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
