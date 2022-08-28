#!/usr/bin/python3
## example3_4

import numpy as np
#from numpy import array, arange, append
from math import pi,cos
from newtonPoly import coeffts, evalPoly
import matplotlib.pyplot as plt

def main():
    xData = np.array([0.15,2.3,3.15,4.85,6.25,7.95])
    yData = np.array([4.79867,4.49013,4.2243,3.47313,2.66674,1.51909])
    a = coeffts(xData,yData)
    
    X = np.array([])
    Y = np.array([[],[]]).T
    print (" x    yInterp    yExact")
    print ("-----------------------")
    for x in np.arange(0.0,8.1,0.5):
        y = evalPoly(a,xData,x)
        yExact = 4.8*cos(pi*x/20.0)
        print ("%3.1f %9.5f %9.5f"% (x,y,yExact))
        X=np.append(X, x)
        Y = np.vstack((Y,np.array([y, yExact])))
    # end for
    plt.plot(X,Y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Example 3.4')
    plt.grid(True)
    plt.show(block=False)
    input("\nPress return to exit")
    
# end of main()    

if __name__ == '__main__':
    main()
# end if
