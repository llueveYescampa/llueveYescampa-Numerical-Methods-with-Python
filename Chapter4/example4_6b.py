#!/usr/bin/python3
## Solving uninhibited frame equation 
## for effective length

from newtonRaphson import newtonRaphson
import matplotlib.pyplot as plt
import numpy as np
from math import pi, tan


def f(x):
    global Ga,Gb
    y = pi/x
    #return (Ga*Gb*(y)**2 - 36)/(6*(Ga+Gb)) - y/tan(y)
    return (Ga*Gb*(y)**2 - 36)/(6*(Ga+Gb)) - y/tan(y) 
# end f(x)

def df(x): 
    dx = 1.0e-6
    return (f(x+dx) - f(x))/dx
# end df(x)


def main():
    lowerK = 1.0
    upperK = 20.0

    var = input("Please enter Ga: ")
    Ga = float(var)
    var = input("Please enter Gb: ")
    Gb = float(var)
    
    root,numIter = newtonRaphson(f,df,lowerK, upperK)
    
    print ('Root =',(root))
    print ('Number of iterations =',numIter)
    input("Finished. Press return to exit")    
# end of main()

if __name__ == '__main__':
    main()
# end if
