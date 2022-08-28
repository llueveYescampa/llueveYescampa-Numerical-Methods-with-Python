## module newtonRaphson2
''' soln = newtonRaphson2(f,x,tol=1.0e-9).
    Solves the simultaneous equations f(x) = 0 by
    the Newton-Raphson method using {x} as the initial
    guess. Note that {f} and {x} are vectors.
'''

from numpy import zeros,dot,sqrt
from gaussPivot import *
import sys

def newtonRaphson2(f,x, tol=1.0e-9,iter=30):
    
    def jacobian(f,x):
        h = 1.0e-4
        n = len(x)
        jac = zeros((n,n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:,i] = (f1 - f0)/h
        # end for    
        return jac,f0
    # end of jacobian()
    
    for i in range(iter):
        jac,f0 = jacobian(f,x)
        #print jac
        if sqrt(dot(f0,f0)/len(x)) < tol: 
            return x
        # end if
        dx = gaussPivot(jac,-f0)
        #print  dx
        x = x + dx
        #print x
        if sqrt(dot(dx,dx)) < tol*max(max(abs(x)),1.0): 
            return x
        # end if
    sys.exit('Too many iterations in Newton-Raphson2')   
# end newtonRaphson2()