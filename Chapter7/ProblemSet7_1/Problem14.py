#!/usr/bin/python3
## Problem 14

from numpy import array,zeros
from math import pi
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
    a= 100.0
    b = 15.0
    F = zeros(2)
    F[0] = y[1]
    F[1] = (a*(b-y[0]) - y[0]*y[1]**2)/(1+y[0]**2)
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 0.5                     # End of integration
    y = array([2*pi,0.0])          # Initial values of {y}
    h = 0.01                        # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,1], "Problem 13") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()