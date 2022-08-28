#!/usr/bin/python3
## example2_11
from numpy import array,ones
from LUdecomp3 import LUdecomp3,LUsolve3

def main():
    d = ones((5))*2.0
    c = ones((4))*(-1.0)
    e = c.copy()
    
    b = array([5.0, -5.0, 4.0, -5.0, 5.0])

    LUdecomp3(c,d,e) 
    x = LUsolve3(c,d,e,b)               # x is a pointer to the modified b

    print ("\nx =\n",x)
    input("\nPress return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if