## module gaussPivot
""" x = gaussPivot(a,b,tol=1.0e-9).
	Solves [a]{x} = {b} by Gauss elimination with
	scaled row pivoting
"""
from numpy import zeros,argmax,dot
from swap import swapRows

def gaussPivot(a,b,tol=1.0e-9):
    n = len(b)

    # Set up scale factors
    s = zeros(n)
    for i in range(n):
        s[i] = max(abs(a[i,:]))
    # end for	

    for k in range(0,n-1):
        # Row interchange, if needed
        p = argmax(abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol:
            print ('Matrix is singular')
        # end if
        if p != k:
            swapRows(b,k,p)
            swapRows(s,k,p)
            swapRows(a,k,p)
        # end if

        # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a [i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
            # end if
        # end for
    # end for
    
    if abs(a[n-1,n-1]) < tol:
        print ('Matrix is singular')
    # end if

    # Back substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    # end for

    return b
# end gaussPivot()
