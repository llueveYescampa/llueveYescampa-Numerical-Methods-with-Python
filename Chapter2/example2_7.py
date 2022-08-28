#!/usr/bin/python3
## example2_7

from numpy import array,prod,diagonal
from LUdecomp import LUdecomp, LUsolve

def main():
    a = array([[ 3.0, -1.0,  4.0], \
               [-2.0,  0.0,  5.0], \
               [ 7.0,  2.0, -2.0]])

    b = array([[ 6.0,  3.0,  7.0], \
               [-4.0,  2.0, -5.0]])

    
    LUdecomp(a)                  # Decompose [a]
    
    det = prod(diagonal(a))
    print ("\nDeterminant =",det)
    
    
    for i in range(len(b)):      # Back-substitute one
        LUsolve(a,b[i])      # constant vector at a time
        print ("x",i+1,"=",b[i])
    # end for   
    #raw_input("\nPress return to exit")
    
# end of main()    

if __name__ == '__main__':
    main()
# end if