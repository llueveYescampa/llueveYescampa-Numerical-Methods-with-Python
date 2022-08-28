## module trapezoid
''' Inew = trapezoid(f,a,b,Iold,k).
    Recursive trapezoidal rule:
    Iold = Integral of f(x) from x = a to b computed by
    trapezoidal rule with 2^(k-1) panels.
    Inew = Same integral computed with 2^k panels.
'''

def trapezoid(f,a,b,Iold,k):
    if k != 1:
        n = 2**(k -2 ) # Number of new points
        h = (b - a)/n # Spacing of new points
        x = a + h/2.0
        sum = 0.0
        for i in range(n):
            sum = sum + f(x)
            x = x + h
        # end for    
        Inew = (Iold + h*sum)/2.0
    else:
        Inew = (f(a) + f(b))*(b - a)/2.0
    # end if
    return Inew
# end trapezoid