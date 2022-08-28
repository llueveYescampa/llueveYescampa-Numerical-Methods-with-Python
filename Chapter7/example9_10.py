#!/usr/bin/python3
'''
    Included by edgar black
'''
## example 9.10 Heat Book - Stiff ODE
## a small change of the initial
## condition kill the solution 

from numpy import array, zeros
from printSoln import printSoln 
from taylor import taylor

def deriv(x,y):
    D = zeros((4,1))
    D[0] = [100*(-y[0] + x + 1.01)]
    D[1] = 0
    D[2] = 0
    D[3] = 0
    # using only D[0] reduce this to forward Euler method
    #D[1] = [10000*(y[0] - x - 1.0)]
    #D[2] = [-1000000*(y[0] - x - 1.0)]
    #D[3] = [100000000*(y[0] - x - 1.0)]
    #D[2] = [0]  # use those wit 0 for 2nd order taylor
    #D[3] = [0]
    return D
#end deriv   

def main():
    xStart = 0.0                    # Start of integration
    xStop = 0.5                     # End of integration
    h = 0.10                         # Step size
    freq = 1                        # Printout frequency
    x,y = taylor(deriv,xStart,array([1.01]),xStop,h)
    printSoln(x,y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
