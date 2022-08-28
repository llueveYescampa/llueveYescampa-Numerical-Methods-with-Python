#!/usr/bin/python3
## Example 9_6

from numpy import ones,zeros
from inversePower5 import inversePower5

def Bv(v):          # Compute {z} = [B]{v}
    n = len(v)
    z = zeros(n)
    z[0] = 2.0*v[0] - v[1]
    for i in range(1,n-1):
        z[i] = -v[i-1] + 2.0*v[i] - v[i+1]
    # end for
    z[n-1] = -v[n-2] + 2.0*v[n-1]
    return z
# end of Bv()


def main():
    n = 100                 # Number of interior nodes
    d = 6.0*ones(n)         # Specify diagonals of [A] = [f\e\d\e\f]
         
    d[0] = 5.0
    d[n-1] = 7.0
    e = ones(n-1)*(-4.0)    
    f = ones(n-2)*1.0
    lam,x = inversePower5(Bv,d,e,f)
    print ("PL^2/EI = ",lam*(n+1)**2)
    input("\nPress return to exit")    
# end of main()

if __name__ == '__main__':
    main()
# end
