#!/usr/bin/python3
'''
'''
## example 8_1 ( Same problem as example 8.7)
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
    alpha = 0.0 # initial boundary condition
    return array([alpha, u])
# end of initCond
    
def r(u):  # Boundary condition residual--see Eq. (8.3)
    beta = 1.0   # initial boundary condition 
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    return (Y[len(Y) - 1][0] - beta)
# end of r()

def F(x,y):    # First-order differential equations
    F = zeros(2)
    F[0] = y[1]
    F[1] = -3.0*y[0]*y[1]
    return F
# end of F()


# Global variables
xStart = 0.0        # Start of integration
xStop = 2.0         # End of integration
h = 0.1             # Step size
# end of Global variables


def main():
    freq = 2            # Printout frequency
    u1 = 0.0            # 1st trial value of unknown init. cond.
    u2 = 2.0            # 2nd trial value of unknown init. cond.
    u = ridder(r,u1,u2) # Compute the correct initial condition
    
    #print "u: %f\n" % (u)
    x,y = integrate(F,xStart,initCond(u),xStop,h)
    myplot(x, y[:,0], "Example 8.1")

    printSoln(x,y,freq)
    input("\nPress return to exit")
# end of main()


if __name__ == '__main__':
    main()
