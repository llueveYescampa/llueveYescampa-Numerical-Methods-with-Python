#!/usr/bin/python3
## example3_12

from numpy import array, power, vstack
from polyFit import polyFit, stdDev
import matplotlib.pyplot as plt

def evalPoly(x,coeff):
    m = len(coeff)
    n = len(x)
    myList=[]
    
    for i in range(n):
        answer=coeff[0]
        for j in range(1,m):
            answer = answer + coeff[j] * power(x[i],j)
        # end for
        myList.append(answer)    
    # end for
    return (array(myList).reshape(n,1))     
# end evalPoly()

def main():
    xData = array([-0.04,0.93,1.95,2.90,3.83,5.0, \
                   5.98,7.05,8.21,9.08,10.09])
    
    yData = array([-8.66,-6.44,-4.36,-3.27,-0.88,0.87, \
                   3.31,4.63,6.19,7.4,8.85])
    y = array([[]]).T
    while 1:
        try:
            m = eval(input("\nDegree of polynomial ==> "))
            coeff = polyFit(xData,yData,m)
            print ("Coefficients are:\n",coeff)
            print ("Std. deviation =",stdDev(coeff,xData,yData))
            temp = evalPoly(xData, coeff)
            y = vstack((y,temp))
        except SyntaxError: 
            break
        # end try
    # end while
    y = y.reshape((xData.size,-1), order='F')
    plt.plot(xData,yData, 'ro')
    plt.plot(xData,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Example 3.12')
    plt.grid(True)
    plt.show()
    input("Finished. Press return to exit")    
# end of main()    

if __name__ == '__main__':
    main()
# end if
