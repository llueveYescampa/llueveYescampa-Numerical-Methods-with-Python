#!/usr/bin/python3
## example2_12

from numpy import array,dot
from gaussPivot import gaussPivot

def main():
    a = array([[2.0, -2.0, 6.0 ], \
               [-2.0, 4.0, 3.0], \
               [-1.0, 8.0, 4.0]])

    b = array([16.0, 0.0, -1.0])

    aOrig = a.copy()
    bOrig = b.copy() # and the constant vector


    x = gaussPivot(a,b);
    print ("x =", x)
    #print "\nCheck: A*x =\n",dot(aOrig,x)
    print ("\nCheck result: [a]{x} - b =\n",dot(aOrig,b) - bOrig)

    input("\nPress return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if