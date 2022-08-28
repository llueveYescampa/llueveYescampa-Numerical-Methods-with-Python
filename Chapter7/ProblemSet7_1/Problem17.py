#!/usr/bin/python3
## Problem 17

from numpy import array,zeros
from printSoln import printSoln
from run_kut4 import integrate
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('time')
    plt.ylabel("Position")
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):  
    k = 3000
    m = 6.0
    mu=0.5
    g=9.80665
    F = zeros(2)
    F[0] = y[1]
    if y[1] >= 0.0:
        F[1] = -((k/m)*y[0] + mu*g)
    else:
        F[1] = -((k/m)*y[0] - mu*g)
    # end if        
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 0.5                   # End of integration
    y = array([0.1, 0.0])          # Initial values of {y}
    h = 0.01                        # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,0], "Problem 17") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()