#!/usr/bin/python3
'''
'''
## Example 8_8

from numpy import zeros,ones,array,arange
from LUdecomp5 import LUdecomp5, LUsolve5
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

def equations(x,h,m): # Set up finite difference eqs.
    h4 = h**4
    d = ones(m + 1)*6.0
    e = ones(m)*(-4.0)
    f = ones(m-1)
    b = zeros(m+1)
    d[0] = 1.0
    d[1] = 7.0
    e[0] = 0.0
    f[0] = 0.0
    d[m-1] = 7.0
    d[m] = 3.0
    b[m] = 0.5*h**3
    return d,e,f,b
# end if


# global definitions
# end of global definitions

def main():
    xStart = 0.0    # x at left end
    xStop = 0.5     # x at right end
    m = 20          # Number of mesh spaces
    h = (xStop - xStart)/m
    x = arange(xStart,xStop + h,h)
    d,e,f,b = equations(x,h,m)
    d,e,f = LUdecomp5(d,e,f)
    y = LUsolve5(d,e,f,b)
    myplot(x, -y, "Example 8.8")    
    print ("\n        x              y")
    for i in range(m + 1):
        print ("%14.5e %14.5e" %(x[i],y[i]))
    # end for    
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
