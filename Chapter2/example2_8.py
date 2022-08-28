#!/usr/bin/python3
## example2_8
from numpy import array, dot
from choleski import choleski, choleskiSol

def main():
    a = array([[ 1.44,  -0.36,  5.52, 0.0], \
              [-0.36, 10.33, -7.78, 0.0], \
              [ 5.52, -7.78, 28.40, 9.0] , \
              [ 0.0,  0.0,  9.0, 61.0]])

    b = array([0.04, -2.15, 0.0, 0.88])

    aOrig = a.copy()
    L = choleski(a)                         # L is a pointer to the modified a
    x = choleskiSol(L,b)                    # x is a pointer to the modified b
    print ("x =",x)
    print ("\nCheck: A*x =\n",dot(aOrig,x))
    input("\nPress return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if