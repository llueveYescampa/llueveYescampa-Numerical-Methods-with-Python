#!/usr/bin/python3
## Problem 9_3

from numpy import array,zeros,dot, sqrt
# sqrt,arange
from stdForm import stdForm
from inversePower import inversePower

def main():
    
    n = 3
    a = zeros((n,n))
    b = zeros((n,n))
    
    a[0,0] = 4.0 
    a[0,1] =-1.0 
    a[0,2] = 0.0
     
    a[1,0] = -1.0 
    a[1,1] =  4.0 
    a[1,2] = -1.0 

    a[2,0] = 0.0 
    a[2,1] =-1.0 
    a[2,2] = 4.0 
    
    b[0,0] = 2.0 
    b[0,1] =-1.0 
    b[0,2] = 0.0

    b[1,0] =-1.0 
    b[1,1] = 2.0 
    b[1,2] =-1.0

    b[2,0] = 0.0
    b[2,1] =-1.0
    b[2,2] = 1.0


    h,t = stdForm(a,b) # Convert to std. form

    s = 2.5
    
    lam,x = inversePower(h,s)
    
    print ("Eigenvalue =",lam)
    
    #print ("Eigenvalues:\n",lam[0:3])
    #print ("\nEigenvectors:\n",x[:,0:3])
    input("\n Press return to exit")

# end of main()

if __name__ == '__main__':
    main()
# end
