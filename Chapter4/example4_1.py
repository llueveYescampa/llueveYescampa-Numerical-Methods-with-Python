#!/usr/bin/python3
## example4_1

from rootsearch import rootsearch

def f(x):
    return x*x*x-10*x*x+5
# end f(x)

def main():
    a=0.0
    b=0.8
    dx=0.2
    (x1,x2) = rootsearch(f,a,b,dx)
    print (x1, x2)
# end of main()    

if __name__ == '__main__':
    main()
# end if
