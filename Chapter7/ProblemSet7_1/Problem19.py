#!/usr/bin/python3
## Problem 19

from numpy import array,zeros
from math import cos
from printSoln import printSoln
from run_kut5 import integrate
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel("y")
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):  
    alpha = 1.0
    F = zeros(2)
    F[0] = y[1]
    F[1] = -(  y[1]/x  +  (1.0 - (alpha/x)**2 )* y[0]  )
    return F
# end F(x,y)


def main():
    x = 1.0e-12                         # Start of integration
    xStop = 5.0                     # End of integration
    y = array([0.0, 1.0])       # Initial values of {y}
    h = 0.01                        # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 19") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()