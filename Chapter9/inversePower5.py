## module inversePower5
''' lam,x = inversePower5(Bv,d,e,f,tol=1.0e-6).
    Inverse power method for solving the eigenvalue problem
    [A]{x} = lam[B]{x}, where [A] = [f\e\d\e\f] is
    pentadiagonal and [B] is sparse.. User must supply the
    function Bv(v) that returns the vector [B]{v}.
'''

from numpy import zeros,dot, sqrt
from LUdecomp5 import LUdecomp5, LUsolve5
from random import random

def inversePower5(Bv,d,e,f,tol=1.0e-6):
    n = len(d)
    d,e,f = LUdecomp5(d,e,f)
    x = zeros(n)
    for i in range(n):          # Seed {v} with random numbers
        x[i] = random()
    # end for
    xMag = sqrt(dot(x,x))       # Normalize {v}
    x = x/xMag
    for i in range(30):         # Begin iterations
        xOld = x.copy()         # Save current {v}
        x = Bv(xOld)            # Compute [B]{v}
        x = LUsolve5(d,e,f,x)   # Solve [A]{z} = [B]{v}
        xMag = sqrt(dot(x,x))   # Normalize {z}
        x = x/xMag
        if dot(xOld,x) < 0.0:   # Detect change in sign of {x}
            sign = -1.0
            x = -x
        else: 
            sign = 1.0
        # end if    
        if sqrt(dot(xOld - x,xOld - x)) < tol:
            return sign/xMag,x
        # end if
    # end for
    print ('Inverse power method did not converge')
# end of inversePower5()

