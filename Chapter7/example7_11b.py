#!/usr/bin/python3
'''
'''
## example7_11b

from numpy import array, zeros, exp
from run_kut5 import integrate
from printSoln import printSoln
import matplotlib.pyplot as plt


def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel("y'")
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):    
    F = zeros(2)
    F[0] = y[1]
    F[1] = (-1.0*y[1]-y[0]/0.45 + 9.0)/2.0
    return F
# end F(x,y)

def main():
    x = 0.0                         # Start of integration
    xStop = 10.0                    # End of integration
    y = array([0.0, 0.0])           # Initial values of {y}
    h = 0.5                         # Step size
    freq = 4                        # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    myplot(X, Y[:,1], "Example 7.9") 
    printSoln(X,Y,freq)
    raw_input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
