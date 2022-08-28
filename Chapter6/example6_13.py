#!/usr/bin/python3
## example6_14

from gaussQuad2 import gaussQuad2
from numpy import array
from math import cos,pi


def f(x,y):
     return (x**2 + y)
# end f()



def main():
    x = array([0.0, 2.0, 2.0, 0.0])
    y = array([0.0, 0.0, 3.0, 2.0])
    m = eval(input("Integration order ==> "))
    print ("Integral =", gaussQuad2(f,x,y,m))
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end
