#!/usr/bin/python3
## example6_2

from math import sqrt,sin,pi
from trapezoid import trapezoid

def f(x): 
    return sin(x)
# end f(x)


def main():
    a = 0.0
    b = pi
    Iold = 0.0
    
    for k in range(1,5):
        Inew = trapezoid(f,a,b,Iold,k)
        if (k > 1) and (abs(Inew - Iold)) < 1.0e-6: break
        Iold = Inew
    # end for    
    print ("Integral =", Inew)
    print ("nPanels =", 2**(k-1))
    
    for k in range(1,6):
        Inew = trapezoid(f,a,b,Iold,k)
        if (k > 1) and (abs(Inew - Iold)) < 1.0e-6: break
        Iold = Inew
    # end for    
    print ("Integral =", Inew)
    print ("nPanels =", 2**(k-1))
    input("\nPress return to exit")

# end of main()

if __name__ == '__main__':
    main()
# end
