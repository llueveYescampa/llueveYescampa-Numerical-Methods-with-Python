#!/usr/bin/python3
## example6_7

from math import cos,sqrt,pi, exp
from romberg import romberg
from trapezoid import trapezoid

def f(x): 
    return 2.0*(x**2)*cos(x**2)
# end f(x)


def main():
    I,n = romberg(f,0,sqrt(pi))
    print ("Integral = ",I)
    print ("nPanels =",n)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end
