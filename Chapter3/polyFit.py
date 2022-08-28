## module polyFit
''' 
    c = polyFit(xData,yData,m).
    Returns coefficients of the polynomial
    p(x) = c[0] + c[1]x + c[2]x2 +...+ c[m]xm
    that fits the specified data in the least
    squares sense.
    sigma = stdDev(c,xData,yData).
    Computes the std. deviation between p(x)
    and the data.
'''
from numpy import zeros
from math import sqrt
from gaussPivot import gaussPivot

def polyFit(xData,yData,m):
    a = zeros((m+1,m+1))
    b = zeros(m+1)
    s = zeros(2*m+1)
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp*xData[i]
        # end for    
        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*xData[i]
        # end for
    # end for
    for i in range(m+1):
        for j in range(m+1):
            a[i,j] = s[i+j]
        # end for
    # end for    
    return gaussPivot(a,b)
# end of polyFit() 

def stdDev(c,xData,yData):
    def evalPoly(c,x):
        m = len(c) - 1
        p = c[m]
        for j in range(m):
            p = p*x + c[m-j-1]
        return p
    # end of evalPoly()

    n = len(xData) - 1
    m = len(c) - 1
    sigma = 0.0
    for i in range(n+1):
        p = evalPoly(c,xData[i])
        sigma = sigma + (yData[i] - p)**2
    # end for    
    sigma = sqrt(sigma/(n - m))
    return sigma
# end of stdDev()
