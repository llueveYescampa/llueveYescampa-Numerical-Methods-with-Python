#!/usr/bin/python3
## example2_18

from numpy import zeros
from conjGrad import conjGrad

def Ax(v):
    n = len(v)
    Ax = zeros(n)
    Ax[0] = 2.0*v[0] - v[1]+v[n-1]
    Ax[1:n-1] = -v[0:n-2] + 2.0*v[1:n-1] -v [2:n]
    Ax[n-1] = -v[n-2] + 2.0*v[n-1] + v[0]
    
    return Ax
# end Ax()o

def main():
    n = eval(input("Number of equations ==> "))
    b = zeros(n)
    b[n-1] = 1.0
    x = zeros(n)
    x,numIter = conjGrad(Ax,x,b)

    print ("\nThe solution is:\n",x)
    print ("\nNumber of iterations =",numIter)
    input("\nPress return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if
