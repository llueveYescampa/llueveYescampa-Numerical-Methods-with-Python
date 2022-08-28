#!/usr/bin/python3
'''
'''
## Problem 10

from numpy import zeros,array,arange,pi,sin
from newtonRaphson2 import newtonRaphson2
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

def residual(y):    # Residuals of finite diff. Eqs. (8.11)
    alpha = 0.5
    beta = -2.0/9.0
    r = zeros(m + 1)
    r[0] = y[0] - alpha
    r[m] = 2.0*y[m-1] - 2.0*y[m] - h*h*F(x[m],y[m],beta) + 2.0*h*beta 
    for i in range(1,m):
        r[i] = y[i-1] - 2.0*y[i] + y[i+1]- h*h*F(x[i],y[i],(y[i+1] - y[i-1])/(2.0*h))
    return r
# end of residual()


def F(x,y,yPrime):       # Differential eqn. y" = F(x,y,y')
    F = -2.0*y*(2*x*yPrime + y)
    return F
# end of F()

def startSoln(x): # Starting solution y(x)
    y = zeros(m + 1)
    for i in range(m + 1): 
        y[i] = 0.5*x[i]
    # end for
    return y
# end of startSoln()

# global definitions
m = 20              # Number of mesh intevals
xStart = 0.0        # x at left end
xStop = 1.0         # x at right end
h = (xStop - xStart)/m
x = arange(xStart,xStop + h,h)
# end of global definitions

def main():
    y = newtonRaphson2(residual,startSoln(x))
    myplot(x, y, "Problem 10")
    print ("\n        x              y")
    for i in range(m + 1):
        print ("%14.5e %14.5e" %(x[i],y[i]))
    # end for    
    input("\nPress return to exit")    
# end of main()

if __name__ == '__main__':
    main()
