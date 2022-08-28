#!/usr/bin/python3
#from math import sqrt, sin, pi
import sys
from numpy import sqrt, sin, arange
from math import pi

def main():
    
    x = arange(0.0,1.001*pi,0.01*pi)
    #print x
    print (sum(sqrt(x)*sin(x)))
    input('press return')
    sys.exit()
    
    '''    
    x = 0.0
    sum = 0.0
    for i in range(0,101):
        sum = sum + sqrt(x)*sin(x)
        x = x + 0.01*pi
    # end for
    print sum    
    '''    


# end of main()    

if __name__ == '__main__':
    main()
# end if    


'''
    string1 = 'press return to exit'
    string2 = 'the program'
    
    print string1 + ' ' + string2 # Concatenation
    
    print string1[0:12]
    
    # about tuples
    rec = ('Black', 'Edgar',   (06,16,1959)  )
    
    lastname, firstname, birthdate = rec
    month, day, year = birthdate
    
    print lastname, firstname, month, day, year
    
    # about lists
    a = [1.0, 2.0, 3.0]
    print a
    a.append(4.0)
    print a
    a.insert(0, 0.0)
    print a
    print len(a)
    a[2:4] = [-1.0,-1.0,-1.0]
    print a
    b = a
    print b
    a[2:4] = [10.0, 10.0, 10.0]
    print a

from numpy import array, float, int, zeros, ones, arange, sin, trace, identity
#diagonal, sqrt,

    a = array([[2, -1],[-1, 3]], dtype=float)
    print a
    b = zeros((2,2), dtype=float)
    print b 
    c = ones((2,2), dtype=int)
    print c
    
    print arange(2,10,2)
    
    a = zeros((3,3), dtype=float)
    print a
    a[0] = [2.,3.,2.]
    print a
    a[1,1] = 5
    print a
    
    a[2,0:2] = [8,-3]
    print a
    
    
    a = array([0,4,9,16], dtype=float)
    print sin(a)
    
    A = array([[4,-2,1],[-2,4,-2],[1,-2,3]],dtype=float)
    b = array([1,4,3],dtype=float)
    
    print trace(A)
    
    print identity(3)
     


from numpy import  array
from numpy.linalg import  inv, solve

    A = array([[1, 1, 1, 1 ],\
              [8 , 4 , 2, 1],\
              [27, 9, 3, 1],\
              [64, 16, 4, 1]], dtype=float)
    print A
    b = array([1, 5, 14, 30], dtype=float)
    print b
    
    print inv(A)
    
    print solve(A,b)

'''    