#!/usr/bin/python3
## example2_4
from numpy import zeros,array,prod,diagonal,dot
from gaussElimin import gaussElimination


def vandermode(v):
    n = len(v)
    a = zeros((n,n))
    for j in range(n):
        a[:,j] = v**(n-j-1)
    return a
#end vandermode()

def main():
    v = array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
    b = array([0.0, 1.0, 0.0, 1.0, 0.0, 1.0])
    a = vandermode(v)
    print (a)
    aOrig = a.copy() # Save original matrix
    bOrig = b.copy() # and the constant vector
    
    gaussElimination(a,b)
    
    det = prod(diagonal(a))
    print ("x =\n",b)
    print ("\ndet =",det)
    print ("\nCheck result: [a]{x} - b =\n",dot(aOrig,b) - bOrig)
    input("\nPress return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if    
