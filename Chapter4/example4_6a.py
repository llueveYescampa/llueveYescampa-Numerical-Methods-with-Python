#!/usr/bin/python3
## example4_6a

from newtonRaphson import newtonRaphson
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 -10*x**2 + 5
# end f(x)

def df(x): 
    return 3*x**2-20*x
# end df(x)

def myplot(xl,xh,title, incre=0.05):
    x = np.arange(xl,xh,incre)
    y = f(x)
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show(block=False)
# end myplot()

def main():
    var = input("Please enter lower limit for x: ")
    a = float(var)
    var = input("Please enter upper limit for x: ")
    b = float(var)
    myplot(a, b, 'example4.6a')
    #raw_input("Finished. Press return to exit")
    #var = raw_input("Please enter approximate root: ")
    #var = float(var)
    
    root,numIter = newtonRaphson(f,df,a, b)
    
    print ('Root =',root)
    print ('Number of iterations =',numIter)
    input("Finished. Press return to exit")    
# end of main()

if __name__ == '__main__':
    main()
# end if
