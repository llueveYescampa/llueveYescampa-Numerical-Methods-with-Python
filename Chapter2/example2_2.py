#!/usr/bin/python3
## example2_2
from numpy import zeros,array,prod,diagonal,dot
from gaussElimin import gaussElimination


def main():
    n = 3
    a = zeros((n,n))
    a[0][0] = 8.0
    a[0][1] = -6.0
    a[0][2] = 2.0
    
    a[1][0] = -4.0
    a[1][1] = 11.0
    a[1][2] = -7.0
    
    a[2][0] = 4.0
    a[2][1] = -7.0
    a[2][2] = 6.0
    
    b = array([28.0, -40.0, 33.0])
    
    print (a)
    gaussElimination(a,b)
    
    print ("x =\n",b)
    input("\nPress return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if    
