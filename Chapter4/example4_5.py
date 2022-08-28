#!/usr/bin/python3
## example4_5

import numpy as np
import matplotlib.pyplot as plt
from ridder import ridder

def f(x):
    a = (x-0.3)**2 + 0.01
    b = (x-0.8)**2 + 0.04
    return (b-a)/(a*b)
# end f(x)

def main():
    x = np.arange(-2.0, 3.0, 0.05)
    y = f(x)
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Example 4.5')
    plt.show(block=False)
    input("Finished. Press return to exit")    
    print ("root: %8.4f" % (ridder(f,0.5,0.7)))
# end of main()    

if __name__ == '__main__':
    main()
# end if
