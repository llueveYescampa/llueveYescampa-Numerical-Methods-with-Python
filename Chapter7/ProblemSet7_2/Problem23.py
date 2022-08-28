#!/usr/bin/python3
## Problem 23
from numpy import array,zeros
from printSoln import printSoln
from run_kut5 import integrate
import matplotlib.pyplot as plt


def myplot(x,y,title="my title"):
    #plt.ion()
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('time')
    plt.ylabel('Concentration')
    plt.title(title)
    plt.show()
# end myplot()

def F(x,y):
    F = zeros(4)
    F[0] = (-6*y[0]+4*y[1]+50)*0.1
    F[1] = (-7*y[1]+3*y[2]+4*y[3])*0.1
    F[2] = 4*(y[0]-y[2])*0.1
    F[3] = (2*y[0]+y[2]-4*y[3]+50)*0.1
    return F
# end F(x,y)

def main():
    
    x = 0.0                         # Start of integration
    xStop = 100.0                    # End of integration
    y = array([0.0, 0.0, 0.0, 0.0])      # Initial values of {y}
    h = 0.1                         # Step size
    freq = 1                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y, "Problem 23")
    printSoln(X,Y,freq)
    input("Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
