#!/usr/bin/python3
'''
    Included by edgar black
'''
## example 9.11 Heat Book

from numpy import array, zeros
from printSoln import printSoln 
from taylor import taylor

def deriv(x,y):
    D = zeros((4,1))
    D[0] = [-2.0*x*y[0]**2]
    D[1] = [8.0*x**2*y[0]**3 - 2.0*y[0]**2 ]
    D[2] = [16*x*y[0]**3 - 48*x**3*y[0]**4 + 8*x*y[0]**3]
    D[3] = [16*y[0]**3 + 48*x*y[0]**2 - 144*x**2*y[0]**4 + 384*x**4*y[0]**5+8*y[0]**3-48*x**2*y[0]**4]
    #D[2] = [0]  # use those wit 0 for 2nd order taylor
    #D[3] = [0]
    return D
#end deriv   

def main():
    xStart = 0.0                    # Start of integration
    xStop = 0.5                     # End of integration
    h = 0.25                         # Step size
    freq = 1                        # Printout frequency
    x,y = taylor(deriv,xStart,array([1.0]),xStop,h)
    printSoln(x,y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
