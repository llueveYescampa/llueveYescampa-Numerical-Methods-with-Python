#!/usr/bin/python3
## Example 9_5

from numpy import array
from inversePower import inversePower 

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

def main():
    s = 5.0
    a = array([[ 11.0, 2.0, 3.0, 1.0, 4.0], \
               [ 2.0, 9.0, 3.0, 5.0, 2.0], \
               [ 3.0, 3.0, 15.0, 4.0, 3.0], \
               [ 1.0, 5.0, 4.0, 12.0, 4.0], \
               [ 4.0, 2.0, 3.0, 4.0, 17.0]])
    
    lam,x = inversePower(a,s)
    print ("Eigenvalue =",lam)
    print ("\nEigenvector:\n",x)
    input("\nPrint press return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end
