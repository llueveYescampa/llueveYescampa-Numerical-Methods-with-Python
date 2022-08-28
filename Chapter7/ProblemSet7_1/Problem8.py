#!/usr/bin/python3
## Problem 8

from numpy import array,zeros
from printSoln import printSoln
from run_kut4 import integrate
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('time')
    plt.ylabel("meters")
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):    
    F = zeros(2)
    F[0] = y[1]
    F[1] = 9.80665 - (0.2028/80.0)*y[1]**2
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 84.79                   # End of integration
    y = array([0.0, 0.0])           # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 8") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()