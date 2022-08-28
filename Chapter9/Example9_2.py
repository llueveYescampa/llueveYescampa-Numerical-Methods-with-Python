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
    
    n = 3
    a = zeros((n,n))
    b = zeros((n,n))
    
    a[0,0] = 1.0/3.0 
    a[1,1] = 4.0/3.0 
    a[2,2] = 2.0
    
    a[0,1] = -1.0/3.0 
    a[1,0] = -1.0/3.0 

    a[2,1] = -1.0 
    a[1,2] = -1.0 
    
    b[0,0] = 1.0 
    b[1,1] = 1.0 
    b[2,2] = 2.0


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
    myplot(xx, y, "Example 9.2")
    
    print ("Eigenvalues:\n",lam[0:3])
    print ("\nEigenvectors:\n",x[:,0:3])
    input("\n Press return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end
