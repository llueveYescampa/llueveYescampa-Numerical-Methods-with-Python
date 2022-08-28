#!/usr/bin/python3
## Problem 17

from numpy import array,zeros
from math import sin, cos, tan, pi
from printSoln import printSoln
from run_kut5 import integrate
import matplotlib.pyplot as plt


def myplot(x,y,title="my title"):
    #plt.ion()
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('phi')
    plt.title(title)
    plt.show()
# end myplot()


def F(x,y):
    F = zeros(4)
    F[0] = y[1]
    F[1] = y[3]**2*sin(y[0])*cos(y[0])
    F[2] = y[3]
    F[3] = -2.0*y[1]*y[3]/tan(y[0])
    return F
# end F(x,y)

def main():
    
    x = 0.0                         # Start of integration
    xStop = 1.5                     # End of integration
    y = array([pi/12, 0.0, 0.0, 20.0])          # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,3], "Problem 17")
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
