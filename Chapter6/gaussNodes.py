## module gaussNodes
''' x,A = gaussNodes(m,tol=10e-9)
    Returns nodal abscissas {x} and weights {A} of
    Gauss--Legendre m-point quadrature.
'''

from math import cos,pi
from numpy import zeros

def gaussNodes(m,tol=10e-9):

    def legendre(t,m):
        p0 = 1.0 
        p1 = t
        for k in range(1,m):
            p = ((2.0*k + 1.0)*t*p1 - k*p0)/(1.0 + k )
            p0 = p1; p1 = p
        # end for    
        dp = m*(p0 - t*p1)/(1.0 - t**2)
        return p,dp
    # end legendre

    A = zeros(m)
    x = zeros(m)
    nRoots = (m + 1)//2
    # Number of non-neg. roots
    for i in range(nRoots):
        t = cos(pi*(i + 0.75)/(m + 0.5))
        # Approx. root
        for j in range(30):
            p,dp = legendre(t,m)    # Newton-Raphson
            dt = -p/dp; t = t + dt  # method
            if abs(dt) < tol:
                x[i] = t; x[m-i-1] = -t
                A[i] = 2.0/(1.0 - t**2)/(dp**2) # Eq.(6.25)
                A[m-i-1] = A[i]
                break
            # end if
        # end for
    #end for    
    #print "x: " , x
    #print A
    return x,A
# end gaussNodes()
