#!/usr/bin/python3
## example 6_11

from math import pi,sin
from gaussQuad import *

def f(x): 
    return (sin(x)/x)**2
# end f()


def main():
    a = 0.0 
    b = pi
    Iexact = 1.41815
    
    for m in range(2,12):
        I = gaussQuad(f,a,b,m)
        if abs(I - Iexact) < 0.00001:
            print ("Number of nodes = ",m)
            print ("Integral =", gaussQuad(f,a,b,m))
            break
        # end if
    # end for
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end
