#!/usr/bin/python3
## Problem 13

from numpy import array,zeros
from printSoln import printSoln
from run_kut4 import integrate
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
    F = zeros(1)
    F[0] = (9.0/y[0] - y[0])*x
    return F
# end F(x,y)

def main():
    
    x = 0.0                         # Start of integration
    xStop = 4.0                     # End of integration
    y = array([5.0])          # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 13")
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
