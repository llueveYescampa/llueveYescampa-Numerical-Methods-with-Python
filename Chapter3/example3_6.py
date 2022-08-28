#!/usr/bin/python3
## example3_6

from numpy import array, arange, zeros
from rational import rational
from neville import neville
import matplotlib.pyplot as plt

def main():
    xData = array([0.1,0.2,0.5,0.6,0.8,1.2,1.5])
    yData = array([-1.5342,-1.0811,-0.4445,-0.3085, -0.0868,0.2281,0.3824])
    
    x = arange(0.1,1.55,0.05)
    n = len(x)
    y = zeros((n,2))
    print ('    x Rational Neville')
    
    
    for i in range(n):
        y[i,0] = rational(xData,yData,x[i])
        y[i,1] = neville (xData,yData,x[i])
        print ('%4.2f %9.5f %9.5f' % (x[i],y[i,0],y[i,1]))
    # end for 
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Example 3.6')
    plt.grid(True)
    plt.show(block=False)
    input("\nPress return to exit")
    
# end of main()    

if __name__ == '__main__':
    main()
# end if
