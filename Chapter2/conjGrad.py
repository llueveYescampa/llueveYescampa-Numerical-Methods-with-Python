## module conjGrad
""" x, numIter = conjGrad(Av,x,b,tol=1.0e-9)
	Conjugate gradient method for solving [A]{x} = {b}.
	The matrix [A] should be sparse. User must supply
	the function Av(v) that returns the vector [A]{v}.
	Note: This algorithm was modified following
		  Heath's book Algorithm 11.1. In the present
		  form, it requires only one matrix-vector 
		  multiplication inside the main loop instead
		  of the original two.
"""

from numpy import dot
from math import sqrt

def conjGrad(Av,x,b,tol=1.0e-9):
    n = len(b)
    r = b - Av(x)
    s = r.copy()
    for i in range(1, n+1):
        As = Av(s)
        alpha = dot(r,r)/dot(s,As)
        x = x + alpha*s
        rNew = r - alpha*As
        if(sqrt(dot(rNew,rNew))) < tol:
            break
        else:
            beta = dot(rNew,rNew)/dot(r,r)
            s = rNew + beta*s
        # end if	
        r = rNew.copy()
    # end for
    return x,i
#end conjGrad()
