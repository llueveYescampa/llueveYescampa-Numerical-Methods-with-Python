#!/usr/bin/pytho3
## example5_4
from cubicSpline import curvatures
from LUdecomp3 import *
from numpy import array


def main():
    xData = array([1.5, 1.9, 2.1, 2.4, 2.6, 3.1])
    yData = array([1.0628, 1.3961, 1.5432, 1.7349, 1.8423, 2.0397])
    print (curvatures(xData,yData))
    input("Press return to exit")# end of main()
# end main
if __name__ == '__main__':
    main()
# end if
