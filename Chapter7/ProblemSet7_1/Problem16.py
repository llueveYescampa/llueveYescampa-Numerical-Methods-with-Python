#!/usr/bin/python3
## Problem 16

from numpy import array,zeros
from math import sin, cos, pi, sqrt
from printSoln import printSoln
from run_kut4 import integrate
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('time')
    plt.ylabel("theta [degrees]")
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):  
    g = 9.80665
    k=40.0
    L=0.5
    m=0.25
    F = zeros(4)
    F[0] = y[1]
    F[1] = y[0]*y[3]**2 + g*cos(y[2]) - k/m*(y[0]-L)  
    F[2] = y[3]
    F[3] = -(2*y[1]*y[3] + g *sin(y[2]))/y[0]
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 0.42                     # End of integration
    y = array([0.575
               , 0, pi/3, 0.0])          # Initial values of {y}
    h = 0.02                        # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, 180/pi*Y[:,2], "Problem 13") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()