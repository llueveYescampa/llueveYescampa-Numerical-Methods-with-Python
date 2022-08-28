#!/usr/bin/python3
## example 6_16_a

from gaussQuad2 import gaussQuad2

from numpy import array
from math import sqrt

def f(x,y):
    return (x**2 + y**2)/2.0 - (x**3 - 3.0*x*y**2)/6.0 - 2.0/3.0
# end of f()     
    


def main():
    x = array([-1.0,-1.0,2.0,2.0])
    y = array([sqrt(3.0),-sqrt(3.0),0.0,0.0])
    m = eval(input("Integration order ==> "))
    print ("Integral = ", gaussQuad2(f,x,y,m))
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end
