#!/usr/bin/python3
'''
'''
## Problem  8_2
from numpy import zeros,array
from run_kut4 import integrate
from ridder import ridder
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
    alpha1 = 2.0 # initial boundary condition
    alpha2 = 0.0 # initial boundary condition
    return array([alpha1, alpha2, u])
# end of initCond

def r(u):  # Boundary condition residual--see Eq. (8.3)
    beta = 0.0   # initial boundary condition 
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    r = Y[len(Y) - 1][0] - beta
    return r
# end of r()

def F(x,y):    # First-order differential equations
    F = zeros(3)
    F[0] = y[1]
    F[1] = y[2]
    F[2] = 6.0 -2.0*y[1] - y[2]
    return F
# end of F()


# Global variables
xStart = 0.0        # Start of integration
xStop = 1.0         # End of integration
h = 0.1             # Step size
# end of Global variables


def main():
    u1 = -10.0            # 1st trial value of unknown init. cond.
    u2 = -5.0            # 2nd trial value of unknown init. cond.
    freq = 2            # Printout frequency
    u = ridder(r,u1,u2) # Compute the correct initial condition
    #print "u: %f\n" % (u)
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    myplot(X, Y[:,0], "Problem 8.2")

    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()


if __name__ == '__main__':
    main()
