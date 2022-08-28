#!/usr/bin/python3
## example4_3

from math import tan
from bisection import bisection
from rootsearch import rootsearch


def f(x): 
    return x - tan(x)
# end if

def main():
    a,b,dx = (0.0, 20.0, 0.01)
    print ("The roots are:")
    while 1:
        x1,x2 = rootsearch(f,a,b,dx)
        if x1 != None:
            a = x2
            root = bisection(f,x1,x2,1)
            if root != None:
                print (root)
            # end if    
        else:
            print ("\nDone")
            break
        # end if
    # end while
    input("Press return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if
