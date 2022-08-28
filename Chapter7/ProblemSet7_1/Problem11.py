#!/usr/bin/python3
## Problem 11

from numpy import array,zeros
from math import sin, cos
from printSoln import printSoln
from run_kut4 import integrate
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('time')
    plt.ylabel("theta")
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):  
    g = 9.80665
    L = 1.0
    Y = 0.25
    w = 2.5
    F = zeros(2)
    F[0] = y[1]
    F[1] = -g/L*sin(y[0]) + w**2/L*Y*cos(y[0])*sin(w*x)
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 10.0                     # End of integration
    y = array([0.0, 0.0])           # Initial values of {y}
    h = 0.02                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 8") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()