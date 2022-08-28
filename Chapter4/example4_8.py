#!/usr/bin/python3
## example4_8

import numpy as np
from newtonRaphson2 import *

def f(x):
    f = np.zeros(len(x))
    f[0] = x[0]**2 + x[1]**2 -3.0
    f[1] = x[0] * x[1] -1.0
    return f
# end f()

def main():
    x = np.array([1.0, 2.0])
    print (newtonRaphson2(f,x))
    input ("\nPress return to exit")
# end of main()

if __name__ == '__main__':
    main()
# end if
