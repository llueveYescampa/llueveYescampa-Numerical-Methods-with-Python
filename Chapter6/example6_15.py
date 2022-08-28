#!/usr/bin/python3
## example6_15

from gaussQuad2 import gaussQuad2
from numpy import array

def f(x,y): 
    return ((x - 2.0)**2)*((y - 2.0)**2)
# end f()



def main():
    x = array([0.0, 4.0, 4.0, 1.0])
    y = array([0.0, 1.0, 4.0, 3.0])
    m = eval(input("Integration order ==> "))
    print ("Integral =", gaussQuad2(f,x,y,m))
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end
