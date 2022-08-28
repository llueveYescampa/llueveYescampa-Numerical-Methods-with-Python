#!/usr/bin/python3
## example7_2

from numpy import array, zeros
from printSoln import printSoln 
from taylor import taylor

def deriv(x,y):
    D = zeros((4,2))
    D[0] = [  y[1], -0.1   * y[1] - x]
    D[1] = [D[0,1],  0.01  * y[1] + 0.1  * x - 1.0]
    D[2] = [D[1,1], -0.001 * y[1] - 0.01 * x + 0.1]
    D[3] = [D[2,1],  0.0001* y[1] + 0.001* x - 0.01]
    #print D
    return D
#end deriv   

def main():
    x = 0.0                         # Start of integration
    xStop = 2.0                     # End of integration
    y = array([0.0, 1.0])           # Initial values of {y}
    h = 0.25                        # Step size
    freq = 1                        # Printout frequency
    X,Y = taylor(deriv,x,y,xStop,h)
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
