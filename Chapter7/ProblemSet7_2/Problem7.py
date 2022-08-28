#!/usr/bin/python3
## Problem 7

from numpy import array,zeros
from printSoln import printSoln
from run_kut5 import integrate
import matplotlib.pyplot as plt


def myplot(x,y,title="my title"):
    plt.ion()
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
    F[1] = 16.81*y[0]
    return F
# end F(x,y)

def main():
    
    x = 0.0                         # Start of integration
    xStop = 2.0                     # End of integration
    y = array([1.0, -4.1])          # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 7 case1") 
    printSoln(X,Y,freq)
    
    y = array([1.0, -4.11])          # Initial values of {y}
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 7 case2") 
    printSoln(X,Y,freq)
    input("Press return to exit")
    
    
# end of main()

if __name__ == '__main__':
    main()
