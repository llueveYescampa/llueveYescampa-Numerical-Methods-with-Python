## module newtonRaphson
''' 
    root = newtonRaphson(f,df,a,b,tol=1.0e-9).
    Finds a root of f(x) = 0 by combining the Newton--Raphson
    method with bisection. The root must be bracketed in (a,b).
    Calls user-supplied functions f(x) and its derivative df(x).
'''
import sys

def newtonRaphson(f,df,a,b,tol=1.0e-9):
    #import error
    fa = f(a)
    if fa == 0.0: return a, 0
    
    fb = f(b)
    if fb == 0.0: return b, 0
    #print 'initial fa %f and fb %f :' % (fa, fb)
    if fa*fb > 0.0: 
        sys.exit("Root is not bracketed")
    # end if
    x = 0.5*(a + b)
    for i in range(30):
        fx = f(x)
        if abs(fx) < tol: 
            return x, i
        # end if
        # Tighten the brackets on the root
        if fa*fx < 0.0:
            b = x
        else:
            a = x
        # end if    
        # Try a Newton-Raphson step
        dfx = df(x)
        # If division by zero, push x out of bounds
        try: 
            dx = -fx/dfx
        except ZeroDivisionError: 
            dx = b - a
        # end try    
        x = x + dx
        # If the result is outside the brackets, use bisection
        if (b - x)*(x - a) < 0.0:
            dx = 0.5*(b-a)
            x = a + dx
        # Check for convergence
        if abs(dx) < tol*max(abs(b),1.0): 
            return x, i
        # end if
    # end for
    sys.exit('Too many iterations in Newton-Raphson')    
# end newtonRaphson()