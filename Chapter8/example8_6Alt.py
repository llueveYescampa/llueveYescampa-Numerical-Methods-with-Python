#!/usr/bin/python3
'''
'''
## Example 8_6 Alternative Solution
import matplotlib.pyplot as plt
from numpy import zeros,array, pi
from run_kut4 import integrate
#from newtonRaphson2 import newtonRaphson2
from linInterp import linInterp
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
    beta1=0.0
    #r = zeros(len(u))
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    #r[0] = Y[len(Y) - 1][1] - beta1
    r = Y[len(Y) - 1][1] - beta1
    return r
# end of r()

def F(x,y):    # First-order differential equations
    F = zeros(2)
    F[0] = y[1]
    F[1] = 4.0*(x-y[0])
    return F
# end of F()


# Global variables
xStart = 0.0     # Start of integration
xStop  = 0.5*pi  # End of integration
h      = 0.1     # Printout increment
# end of Global variables


def main():
    freq = 1 # Printout frequency
    #u = array([8.0]) # Initial guess for {u}
    #u = newtonRaphson2(r,u)
    u = linInterp(r,1.0,5.0) # Compute the correct initial condition
    print (u)
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    myplot(X, Y[:,0], "Example 8.6 Alternate")
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
