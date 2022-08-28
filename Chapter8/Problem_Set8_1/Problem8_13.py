#!/usr/bin/python3
'''
'''
## Problem 8_13
import matplotlib.pyplot as plt
from numpy import zeros,array
from run_kut4 import integrate
from newtonRaphson2 import newtonRaphson2
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
    alpha2=0.0
    return array([alpha1, u, alpha2], dtype=object)
# end of initCond


def r(u):  # Boundary condition residual--see Eq. (8.3)
    beta1=1.0
    r = zeros(len(u))
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    r[0] = Y[len(Y) - 1][0] - beta1
    return r
# end of r()

def F(x,y):    # First-order differential equations
    F = zeros(3)
    F[0] = y[1]
    F[1] = y[2]
    F[2] = 0.1*y[1]**3 + y[1]/(x**2) - y[2]/x
    return F
# end of F()


# Global variables
xStart = 1.0 # Start of integration
xStop =  2.0  # End of integration
h = 0.1 # Printout increment
# end of Global variables


def main():
    freq = 1 # Printout frequency
    u = array([0.0]) # Initial guess for {u}
    u = newtonRaphson2(r,u)
    print (u)
    
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    myplot(X, Y, "Problem 8_13")
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
