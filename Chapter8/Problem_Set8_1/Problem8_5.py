#!/usr/bin/python3
'''
'''
## Problem 8_5
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
    alpha2=1.0
    return array([alpha1, alpha2, u], dtype=object)
# end of initCond


def r(u):  # Boundary condition residual--see Eq. (8.3)
    beta1=0.0
    r = zeros(len(u))
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    y = Y[len(Y) - 1]
    r[0] = y[0] - beta1
    return r
# end of r()

def F(x,y):    # First-order differential equations
    F = zeros(3)
    F[0] = y[1]
    F[1] = y[2]
    F[2] = -5.0*y[2]*y[0]**2
    return F
# end of F()


# Global variables
xStart = 0.0 # Start of integration
xStop = 1.0 # End of integration
h = 0.05 # Printout increment
# end of Global variables


def main():
    freq = 1 # Printout frequency
    u = array([0.0]) # Initial guess for {u}
    u = newtonRaphson2(r,u)
    print ("u: %f\n" % (u))
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    myplot(X, Y[:,0], "Problem 8_5")
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
