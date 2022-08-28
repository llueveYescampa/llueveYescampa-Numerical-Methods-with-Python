#!/usr/bin/python3
## Example 9_3

from numpy import array,zeros,dot, sqrt, concatenate, arange
from stdForm import stdForm
from jacobi import jacobi
from sortJacobi import sortJacobi
import matplotlib.pyplot as plt

def myplot(x,y,title="my title"):
    #plt.ion()
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show()
# end myplot()


def main():
    
    n = 10
    a = zeros((n,n))
    b = zeros((n,n))
    for i in range(n):
        a[i,i] = 6.0
        b[i,i] = 2.0
    # end for    
    a[0,0] = 5.0
    a[n-1,n-1] = 7.0
    
    for i in range(n-1):
        a[i,i+1] = -4.0
        a[i+1,i] = -4.0
        b[i,i+1] = -1.0
        b[i+1,i] = -1.0
    # end for     
    for i in range(n-2):
        a[i,i+2] = 1.0
        a[i+2,i] = 1.0
    # end for
    
    h,t = stdForm(a,b) # Convert to std. form
    lam,z = jacobi(h) # Solve by Jacobi mthd.
    x = dot(t,z) # Eigenvectors of orig. prob. [x] = [t][z]
    for i in range(n): # Normalize eigenvectors
        xMag = sqrt(dot(x[:,i],x[:,i]))
        x[:,i] = x[:,i]/xMag
    # end for
    sortJacobi(lam,x)       # Arrange in ascending order
    
    
    y = array([zeros(3)])
    y = concatenate ((y,x[:, 0:3]), axis=0)
    y = concatenate ((y,[y[0, 0:3]]), axis=0)
    
    xx = arange(y.shape[0], dtype=float)/(y.shape[0]-1.0)
    myplot(xx, y, "Example 9.3")
    
    print ("Eigenvalues:\n",lam[0:3])
    print ("\nEigenvectors:\n",x[:,0:3])
    input("\n Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end
