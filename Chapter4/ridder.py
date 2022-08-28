## module ridder

''' 
    root = ridder(f,a,b,tol=1.0e-9).
    Finds a root of f(x) = 0 with Ridder's method.
    The root must be bracketed in (a,b).
'''
from error import err 
from math import sqrt

def ridder(f,a,b,tol=1.0e-9):
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if fa*fb > 0.0:
        err('Root is not bracketed') 
    # end id  
    
    for i in range(30):
        # Compute the improved root x from Ridder's formula
        c = 0.5*(a + b) 
        fc = f(c)
        s = sqrt(fc**2 - fa*fb)
        if s == 0.0: return None
        dx = (c - a)*fc/s
        if (fa - fb) < 0.0: dx = -dx
        x = c + dx 
        fx = f(x)
        # Test for convergence
        if i > 0  and abs(x - xOld) < tol*max(abs(x),1.0):
            return x
        # end if
        xOld = x
        # Re-bracket the root as tightly as possible
        if fc*fx > 0.0:
            if fa*fx < 0.0: 
                b = x 
                fb = fx
            else:
                a = x 
                fa = fx
            # end if     
        else:
            a = c 
            b = x 
            fa = fc 
            fb = fx
        # end if
    return None
    print ('Too many iterations')
 # end of rider()   


# end of ridder()