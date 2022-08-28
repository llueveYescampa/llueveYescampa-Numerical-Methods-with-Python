## module run_kut2
''' X,Y = integrate(F,x,y,xStop,h).
    4th-order Runge--Kutta method for solving the
    initial value problem {y}' = {F(x,{y})}, where
    {y} = {y[0],y[1],...y[n-1]}.
    x,y = initial conditions.
    xStop = terminal value of x.
    h = increment of x used in integration.
    F = user-supplied function that returns the
        array F(x,y) = {y'[0],y'[1],...,y'[n-1]}.
'''

from numpy import array

def integrate(F,x,y,xStop,h):
    
    def run_kut2(F,x,y,h):
        # Computes increment of y from Eqs. (7.9)
        K0 = h*F(x,y)
        return (h*F(x + h/2.0, y + 0.5*K0)) 
    # end of run_kut2()

    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut2(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    # end while    
    return array(X),array(Y)