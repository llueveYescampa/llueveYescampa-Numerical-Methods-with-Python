#!/usr/bin/python3
## example2_13

from numpy import array,identity,dot
from LUpivot import LUdecomp, LUsolve

def matInv(a):
    n = len(a[0])
    aInv = identity(n)
    a,seq = LUdecomp(a)
    for i in range(n):
        aInv[:,i] = LUsolve(a,aInv[:,i],seq)
    return aInv
# end of matInv()

def main():
    a = array([[ 0.6, -0.4, 1.0],\
               [-0.3,0.2, 0.5],\
               [ 0.6, -1.0, 0.5]])

    aOrig = a.copy() # Save original [a]
    aInv = matInv(a) # Invert [a] (original [a] is destroyed)

    print ("\naInv =\n",aInv)
    print ("\nCheck: a*aInv =\n", dot(aOrig,aInv))

    input("\nPress return to exit")

# end of main()    

if __name__ == '__main__':
    main()
# end if