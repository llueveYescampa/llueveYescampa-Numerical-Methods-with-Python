#!/usr/bin/python3
## example3_9

from numpy import array,float
from cubicSpline import curvatures, evalSpline

def main():
    xData = array([1,2,3,4,5],dtype=float)
    yData = array([0,1,0,1,0],dtype=float)
    k = curvatures(xData,yData)
    while 1:
        try: x = eval(input("\nx ==> "))
        except SyntaxError: break
        print ("y = ", evalSpline(xData,yData,k,x))
    # end while   
    input("Done. Press return to exit")

# end of main()    

if __name__ == '__main__':
    main()
# end if
