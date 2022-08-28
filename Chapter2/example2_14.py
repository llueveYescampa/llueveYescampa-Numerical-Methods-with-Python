#!/usr/bin/python3
## example2_14

from numpy import ones,identity
from LUdecomp3 import LUdecomp3,LUsolve3

def main():
    n = 6
    d = ones((n))*2.0
    e = ones((n-1))*(-1.0)
    c = e.copy()
    d[n-1] = 5.0
    aInv = identity(n)
    c,d,e = LUdecomp3(c,d,e)
    for i in range(n):
        aInv[:,i] = LUsolve3(c,d,e,aInv[:,i])
    print ("\nThe inverse matrix is:\n",aInv)
    input("\nPress return to exit")
# end of main()    

if __name__ == '__main__':
    main()
# end if
