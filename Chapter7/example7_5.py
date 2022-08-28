 #!/usr/bin/python3
'''
    Included by edgar black
    solved using Runge-Kutta
'''
## example7_5

from numpy import array, zeros, exp
from printSoln import printSoln
from run_kut4 import integrate


def F(x,y):    
    F = zeros(1)
    F[0] = 3*y[0]-4*exp(-x)
    return F
# end F(x,y)

def main():
    x = 0.0                         # Start of integration
    xStop = 10.0                    # End of integration
    y = array([1.0])                # Initial values of {y}
    h = 0.1                         # Step size
    freq = 20                       # Printout frequency
    X,Y = integrate(F,x,y,xStop,h)
    printSoln(X,Y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
