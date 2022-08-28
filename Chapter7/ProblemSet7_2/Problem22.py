#!/usr/bin/python3
## Problem 22

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
    a = 5.0
    b = 0.9
    c = 8.2
    F = zeros(3)
    F[0] = -a*(y[0]+y[1])
    F[1] = c*y[0]-y[1]-y[0]*y[2]
    F[2] = y[0]*y[1] -b*y[2]
    return F
# end F(x,y)

def main():
    
    x = 0.0                         # Start of integration
    xStop = 10.0                    # End of integration
    y = array([0.0, 1.0, 2.0])      # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 22")
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
