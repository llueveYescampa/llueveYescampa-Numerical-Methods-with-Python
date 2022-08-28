#!/usr/bin/python3
## Problem 10

from numpy import array,zeros
from printSoln import printSoln
from run_kut5 import integrate
import matplotlib.pyplot as plt
from math import sqrt


def myplot(x,y,title="my title"):
    #plt.ion()
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show()
# end myplot()


def F(x,y):  
    F = zeros(2)
    F[0] = y[1]
    F[1] = -(3.0*y[0] + 2.0*y[1])
    return F
# end F(x,y)

def main():
    
    x = 0.0                         # Start of integration
    xStop = 5.0                     # End of integration
    y = array([0.0, sqrt(2)])          # Initial values of {y}
    h = 0.01                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 10")
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
