#!/usr/bin/python3
## example 6_16_b

from numpy import array
from math import sqrt
from triangleQuadrature import triangleQuad


def f(x,y):
    return (x**2.0 - y**2.0)
# end of f()     

def main():

    # Using trianQuad
    x = array([0.0, 16.0, 12.0])
    y = array([0.0, 10.0, 20.0])
    print ("Integral = ", triangleQuad(f,x,y))
    # Using trianQuad
    
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end
