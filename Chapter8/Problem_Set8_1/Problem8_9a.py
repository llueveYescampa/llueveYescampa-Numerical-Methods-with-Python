#!/usr/bin/python3
'''
'''
## Problem 8_9a
import matplotlib.pyplot as plt
from numpy import zeros,array, pi
from run_kut4 import integrate
from ridder import ridder
from printSoln import printSoln
import sys

def myplot(x,y,title="my title"):
    #plt.ion()
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show()
# end myplot()


def initCond(u):    
    alpha1=0.0
    return array([alpha1, u])
# end of initCond


def r(u):  # Boundary condition residual--see Eq. (8.3)
    beta1=-1.0
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    r = Y[len(Y) - 1][0] - beta1
    return r
# end of r()

def F(x,y):    # First-order differential equations
    F = zeros(2)
    F[0] = y[1]
    F[1] = -(2.0*y[1] + 3.0*y[0])
    return F
# end of F()


# Global variables
xStart = 0.0 # Start of integration
xStop =  2.0  # End of integration
h = 0.1 # Printout increment
# end of Global variables


def main():
    freq = 1 # Printout frequency
    u1 = -100.0         # 1st trial value of unknown init. cond.
    u2 = 0.0            # 2nd trial value of unknown init. cond.
    u = ridder(r,u1,u2) # Compute the correct initial condition
    print (u)
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    myplot(X, Y, "Problem 8_9a")
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
