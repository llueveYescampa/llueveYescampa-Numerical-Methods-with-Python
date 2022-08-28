#!/usr/bin/python3
## Problem 21

from numpy import array,zeros
from printSoln import printSoln
from run_kut5 import integrate
import matplotlib.pyplot as plt


def myplot(x,y,title="my title"):
    #plt.ion()
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('Pray Population')
    plt.ylabel('Predators population')
    plt.title(title)
    plt.show()
# end myplot()


def F(x,y):
    a = 1.0
    b = 0.2
    c = y[0]*y[1]
    F = zeros(2)
    F[0] = a*(y[0]-c)
    F[1] = b*(c - y[1])
    return F
# end F(x,y)

def main():
    
    x = 0.0                         # Start of integration
    xStop = 15.0                     # End of integration
    y = array([0.1, 1.0])          # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(Y[:,0], Y[:,1], "Problem 21")
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
