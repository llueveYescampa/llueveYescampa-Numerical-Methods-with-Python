#!/usr/bin/python3
## Problem 12

from numpy import array,zeros
from math import sin, cos, pi
from printSoln import printSoln
from run_kut4 import integrate
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('time')
    plt.ylabel("Position")
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):  
    g = 9.80665
    F = zeros(2)
    F[0] = y[1]
    F[1] = pi**4/144.0 * y[0] *sin(pi*x)**2 -g*sin(pi/12*cos(pi*x))  
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 3.56                     # End of integration
    y = array([0.75, 0.0])          # Initial values of {y}
    h = 0.02                        # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 8") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()