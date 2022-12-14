## module LUpivot
""" a,seq = LUdecomp(a,tol=1.0e-9).
	LU decomposition of matrix [a] using scaled row pivoting.
	The returned matrix [a] = [L\\U] contains [U] in the upper
	triangle and the nondiagonal terms of [L] in the lower triangle.
	Note that [L][U] is a row-wise permutation of the original [a];
	the permutations are recorded in the vector {seq}.

	x = LUsolve(a,b,seq).
	Solves [L][U]{x} = {b}, where the matrix [a] = [L\\U] and the
	permutation vector {seq} are returned from LUdecomp.
"""

from numpy import argmax,abs,dot,zeros,float,array
import swap

def LUdecomp(a,tol=1.0e-9):
    n = len(a)
    seq = array(range(n))

    # Set up scale factors
    s = zeros((n),dtype=float)
    for i in range(n):
        s[i] = max(abs(a[i,:]))
    # end for

    for k in range(0,n-1):
        # Row interchange, if needed
        p = int(argmax(abs(a[k:n,k])/s[k:n])) + k
        if abs(a[p,k]) < tol:
            print ('Matrix is singular')
        # end if
        if p != k:
            swap.swapRows(s,k,p)
            swap.swapRows(a,k,p)
            swap.swapRows(seq,k,p)
        # end if

        # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam
            # end if
        # end for
    # end for

    return a,seq
# end LUdecomp()

def LUsolve(a,b,seq):
    n = len(a)
    # Rearrange constant vector; store it in [x]
    x = b.copy()
    for i in range(n):
        x[i] = b[seq[i]]
    # end for

    # Solution
    for k in range(1,n):
        x[k] = x[k] - dot(a[k,0:k],x[0:k])
    # end for
    for k in range(n-1,-1,-1):
        x[k] = (x[k] - dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    # end for
    return x
# end of LUsolve()

