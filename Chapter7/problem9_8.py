#!/usr/bin/python3
'''
'''
## Computer problem 9.8 Heath book 

from numpy import array, zeros, sqrt
from printSoln import printSoln
from run_kut4 import integrate
import matplotlib.pyplot as plt


def myplot(x,y,title="my title"):
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel("y'")
    plt.title(title)
    plt.show(block=True)
# end myplot()


def F(x,y):
    G = 6.67259e-11
    M = 5.974e24
    m = 7.348e22
    muS=M/(m+M)
    mu=m/(m+M)
    D = 3.844e8
    d = 4.669e6
    om = 2.661e-6
    r1 = sqrt( (y[0]+d)**2 + y[2]**2)
    r2 = sqrt( (D-d-y[0])**2 + y[2]**2 )
    
    order=4    
    F = zeros(order)
    F[0] = y[1]
    F[1] = -G*(M*(y[0]+mu*D)/r1**3 + m*(y[0]-muS*D)/r2**3) + om**2*y[0] + 2*om*y[3] 
    F[2] = y[3]
    F[3] = -G*(M*y[2]/r1**3 + m*y[2]/r2**3) + om**2*y[2] - 2*om*y[1]
    return F
# end F(x,y)

def main():
    xStart = 0.0                         # Start of integration
    xStop = 2.4e6                    # End of integration
    h = 500                         # Step size
    freq = 50                       # Printout frequency
    x,y = integrate(F,xStart,  array([4.613e8, 0.0, 0.0, -1074]) ,xStop,h)
    myplot(y[:,0], y[:,2], "Problem 9.8") 
    
    ##printSoln(x,y,freq)
    input("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()