#!/usr/bin/python3
## example2_3
from numpy import zeros,array,prod,diagonal,dot
from gaussElimin import gaussElimination


def main():
    n = 3
    a = zeros((n,n))
    a[0][0] = 6.0
    a[0][1] = -4.0
    a[0][2] = 1.0
    
    a[1][0] = -4.0
    a[1][1] = 6.0
    a[1][2] = -4.0
    
    a[2][0] = 1.0
    a[2][1] = -4.0
    a[2][2] = 6.0
    
    b = array([-14.0, 36.0, 6.0])
    
    print (a)
    gaussElimination(a,b)
    
    print ("x =\n",b)
    input("\nPress return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if    
