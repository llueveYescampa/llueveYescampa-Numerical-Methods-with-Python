#!/usr/bin/python3
## Problem 5

from numpy import array,zeros
from math import cos
from printSoln import printSoln
from run_kut4 import integrate
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):  
    m=2.0
    c=460.0
    k=450.0    
    F = zeros(2)
    F[0] = y[1]
    F[1] = -(c*y[1]+k*y[0])/m    
    return F
# end F(x,y)

def main():
    x = 0.0                       # Start of integration
    xStop = 0.2                   # End of integration
    y = array([0.01,0.0])         # Initial values of {y}
    h = 0.008                     # Step size
    freq = 1                      # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 5") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
