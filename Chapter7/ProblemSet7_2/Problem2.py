#!/usr/bin/python3
## Problem 2 and 3

from numpy import array,zeros
from math import cos
from printSoln import printSoln
from run_kut4 import integrate
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):  
    alpha = 1.0
    F = zeros(1)
    F[0] = x - 10*y[0]
    return F
# end F(x,y)


def main():
    x = 0.0                       # Start of integration
    xStop = 5.0                   # End of integration
    y = array([10.0])             # Initial values of {y}
    h = 0.10                      # Step size
    #h = 0.25                      # Step size
    #h = 0.50                      # Step size
    freq = 1                      # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 2 and 3 ") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
