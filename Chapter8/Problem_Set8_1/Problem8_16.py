#!/usr/bin/python3
'''
'''
## Problem 8_16
import matplotlib.pyplot as plt
from numpy import zeros,array, sin
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
    return array([alpha1, u[0], u[1]], dtype=object)
# end of initCond


def r(u):  # Boundary condition residual--see Eq. (8.3)
    beta1=0.0
    beta2=1.0
    r = zeros(len(u))
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    
    r[0] = Y[len(Y)//2 - 1 ][0] - beta1
    r[1] = Y[len(Y) - 1]  [0] - beta2
    
    return r
# end of r()

def F(x,y):    # First-order differential equations
    F = zeros(3)
    F[0] = y[1]
    F[1] = y[2]
    F[2] = -(2*y[2]-sin(y[0]))
    return F
# end of F()


# Global variables
xStart = -1.0 # Start of integration
xStop =  1.0  # End of integration
h = 0.1 # Printout increment
# end of Global variables


def main():
    freq = 1 # Printout frequency
    u = array([0.0, 0.0]) # Initial guess for {u}
    u = newtonRaphson2(r,u)
    print (u)
    
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    myplot(X, Y, "Problem 8_16")
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
