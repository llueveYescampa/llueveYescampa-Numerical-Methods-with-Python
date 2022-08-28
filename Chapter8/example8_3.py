#!/usr/bin/python3
'''
'''
## example 8_3
from numpy import zeros,array
from run_kut5 import integrate
from linInterp import linInterp
from printSoln import printSoln
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    #plt.ion()
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show()
# end myplot()


def initCond(u):   # Init. values of [y,y']; use 'u' if unknown
    alpha0 = 0.0 # initial boundary condition
    alpha1 = 0.0 # initial boundary condition
    return array([alpha0,alpha1, u])
# end of initCond

def r(u):  # Boundary condition residual--see Eq. (8.3)
    beta = 2.0   # initial boundary condition 
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    r = Y[len(Y) - 1][0] - beta
    return r
# end of r()

def F(x,y):    # First-order differential equations
    F = zeros(3)
    F[0] = y[1]
    F[1] = y[2]
    F[2] = 2.0*y[2] + 6.0*x*y[0]
    return F
# end of F()


# Global variables
xStart = 5.0        # Start of integration
xStop = 0.0         # End of integration
h = -0.1             # Step size
# end of Global variables


def main():
    freq = 2            # Printout frequency
    u = linInterp(r,1.0,5.0) # Compute the correct initial condition
    #print u
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    myplot(X, Y[:,0], "Example 8.3")
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()


if __name__ == '__main__':
    main()
