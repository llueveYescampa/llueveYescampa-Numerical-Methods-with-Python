#!/usr/bin/python3
'''
'''
## Example 8_7 ( Same problem as example 8.1)

from numpy import zeros,array,arange
from newtonRaphson2 import newtonRaphson2
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



def residual(y):    # Residuals of finite diff. Eqs. (8.11)
    r = zeros(m + 1)
    r[0] = y[0]
    r[m] = y[m] - 1.0
    for i in range(1,m):
        r[i] = y[i-1] - 2.0*y[i] + y[i+1]- h*h*F(x[i],y[i],(y[i+1] - y[i-1])/(2.0*h))
    return r
# end of residual()


def F(x,y,yPrime):       # Differential eqn. y" = F(x,y,y')
    F = -3.0*y*yPrime
    return F
# end of F()

def startSoln(x): # Starting solution y(x)
    y = zeros(m + 1)
    for i in range(m + 1): 
        y[i] = 0.5*x[i]
    # end for
    return y
# end of startSoln()

# global definitions
m = 10              # Number of mesh intevals
xStart = 0.0        # x at left end
xStop = 2.0         # x at right end
h = (xStop - xStart)/m
x = arange(xStart,xStop + h,h)
# end of global definitions

def main():
    y = newtonRaphson2(residual,startSoln(x))
    
    myplot(x, y, "Example 8.7")
    print ("\n        x              y")
    for i in range(m + 1):
        print ("%14.5e %14.5e" %(x[i],y[i]))
    # end for    
    input("\nPress return to exit")    
# end of main()

if __name__ == '__main__':
    main()
