#!/usr/bin/python3
## example4_2

from bisection import bisection

def f(x):
    return x**3 - 10*x**2 + 5
# end f(x)

def main():
    print ("root: %8.4f" % (bisection(f,0.6,0.8)))
# end of main()    

if __name__ == '__main__':
    main()
# end if
