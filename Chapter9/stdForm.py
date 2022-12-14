## module stdForm
''' h,t = stdForm(a,b).
    Transforms the eigenvalue problem [a]{x} = lam[b]{x}
    to the standard form [h]{z} = lam{z}. The eigenvectors
    are related by {x} = [t]{z}.
'''
from numpy import dot,inner,transpose
from choleski import choleski

def stdForm(a,b):
    
    def invert(L): # Inverts lower triangular matrix L
        n = len(L)
        for j in range(n-1):
            L[j,j] = 1.0/L[j,j]
            for i in range(j+1,n):
                L[i,j] = -dot(L[i,j:i],L[j:i,j])/L[i,i]
            # end for
        # end for             
        L[n-1,n-1] = 1.0/L[n-1,n-1]
    # end invert()
        
    n = len(a)
    L = choleski(b)
    invert(L)
    h = dot(b,inner(a,L))
    return h,transpose(L) 
# end stdForm