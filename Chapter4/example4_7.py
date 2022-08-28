#!/usr/bin/python3
## example4_7

#from newtonRaphson import newtonRaphson
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752    
# end f(x)

def df(x): 
    return 4.0*x**3 - 19.2*x**2 + 12.9*x + 20.538
# end df(x)

def newtonRaphson(x,tol=1.0e-9):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol: 
            return x,i
        # end if
    print ('Too many iterations\n')
# end newtonRaphson

def main():
    x = np.arange(0.0, 5.0, 0.05)
    y = f(x)
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Example 4.7')
    plt.show(block=True)
    #raw_input("Finished. Press return to exit")
    
    var = input("Please enter approximate root: ")
    var=float(var)
    
    root,numIter = newtonRaphson(var)
    print ('Root =',root)
    print ('Number of iterations =',numIter)
# end of main()

if __name__ == '__main__':
    main()
# end if
