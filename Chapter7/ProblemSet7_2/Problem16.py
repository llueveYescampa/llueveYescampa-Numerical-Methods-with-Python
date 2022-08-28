#!/usr/bin/python3
## Problem 16

from numpy import array,zeros
from printSoln import printSoln
from run_kut5 import integrate
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


def F(x,y):
    c = 5.0
    k = 120.0
    L = 0.2
    m = 1.0
    F = zeros(2)
    F[0] = y[1]
    F[1] = c/y[0]**2 - k*(y[0]-L)
    return F
# end F(x,y)

def main():
    
    x = 0.0                         # Start of integration
    xStop = 1.0                     # End of integration
    y = array([0.2, 0.0])          # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 16 Y")
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
