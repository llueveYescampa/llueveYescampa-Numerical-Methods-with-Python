#!/usr/bin/python3
'''
'''
## example 8_4
import matplotlib.pyplot as plt
from numpy import zeros,array
from bulStoer import bulStoer
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


def initCond(u):    # Initial values of [y,y',y'',y'''];
                    # use 'u if unknown
    disp1   = 0.0
    rot1    = u[0]
    moment1 = 0.0
    shear1  = u[1]
    return array([disp1, rot1, moment1, shear1])
# end of initCond


def r(u):  # Boundary condition residual--see Eq. (8.3)
    beta1=0.0
    beta2=0.0
    r = zeros(len(u))
    X,Y = bulStoer(F,xStart,initCond(u),xStop,h)
    y = Y[len(Y) - 1]
    r[0] = y[0] - beta1
    r[1] = y[2] - beta2
    return r
# end of r()

def F(x,y):    # First-order differential equations
    F = zeros(4)
    F[0] = y[1]
    F[1] = y[2]
    F[2] = y[3]
    F[3] = x
    return F
# end of F()


# Global variables
xStart = 0.0 # Start of integration
xStop = 1.0 # End of integration
h = 0.05 # Printout increment
# end of Global variables


def main():
    freq = 1 # Printout frequency
    u = array([0.0, 1.0]) # Initial guess for {u}
    u = newtonRaphson2(r,u)
    X,Y = bulStoer(F,xStart,initCond(u),xStop,h)
    myplot(X, Y[:,0], "Example 8.4")
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
