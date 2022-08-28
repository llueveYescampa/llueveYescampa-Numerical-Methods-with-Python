#!/usr/bin/pytho3
## example5_5
## based on example 3_12

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
    xData = array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]) 
    yData = array([1.9934, 2.1465, 2.2129, 2.1790, 2.0683, 1.9448, 1.7655, 1.5891])
                   
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
    plt.title('Example 5.5 (based on Example 3.12)')
    plt.grid(True)
    #plt.show(block=False)
    plt.show()
    
    input("Finished. Press return to exit")    
# end of main()    

if __name__ == '__main__':
    main()
# end if
