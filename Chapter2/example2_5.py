#!/usr/bin/python3
## example2_5

from numpy import array,prod,diagonal
from LUdecomp import LUdecomp, LUsolve

def main():
    a = array([[1.0, 4.0, 1.0], \
               [1.0, 6.0, -1.0], \
               [2.0, -1.0, 2.0]])

    b = array([ 7.0,  13.0,  5.0])

    a = LUdecomp(a)                             # Decompose [a]    
    print ("\nDeterminant =", prod(diagonal(a)))# print determinant of A    
    LUsolve(a,b)                                # Solve for solution    
    print (b)                                   # print solution
        
    input("\nPress return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if