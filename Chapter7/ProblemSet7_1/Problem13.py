#!/usr/bin/python3
## Problem 13

from numpy import array,zeros
from math import sin, cos, pi, sqrt
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
    g = 9.80665
    Cd=0.03
    m = 0.25
    v=sqrt(y[1]**2 + y[3]**2)
    F = zeros(4)
    F[0] = y[1]
    F[1] = -Cd/m*sqrt(v)*y[1]  
    F[2] = y[3]
    F[3] = -Cd/m*sqrt(v)*y[3] - g
    return F
# end F(x,y)


def main():
    x = 0.0                         # Start of integration
    xStop = 3.47                     # End of integration
    y = array([0.0, 50*cos(pi/6), 0.0, 50*sin(pi/6)])          # Initial values of {y}
    h = 0.02                        # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,2], "Problem 13") 
    myplot(Y[:,0], Y[:,2], "Problem 13") 
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()