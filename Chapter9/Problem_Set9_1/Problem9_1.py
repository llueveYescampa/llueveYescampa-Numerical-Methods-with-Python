#!/usr/bin/python3
## Problem 9_1

from numpy import array,zeros,dot
from stdForm import stdForm

def main():
    
    n = 3
    a = zeros((n,n))
    b = zeros((n,n))
    
    a[0,0] = 7.0 
    a[0,1] = 3.0 
    a[0,2] = 1.0
     
    a[1,0] = 3.0 
    a[1,1] = 9.0 
    a[1,2] = 6.0 

    a[2,0] = 1.0 
    a[2,1] = 6.0 
    a[2,2] = 8.0 
    
    b[0,0] = 4.0 
    b[1,1] = 9.0 
    b[2,2] = 4.0


    h,t = stdForm(a,b) # Convert to std. form
    print (h) 
    print (t) 
    input("\n Press return to exit")

# end of main()

if __name__ == '__main__':
    main()
# end
