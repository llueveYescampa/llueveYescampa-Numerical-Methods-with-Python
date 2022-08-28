#!/usr/bin/python3
## example2_6
from numpy import array
from choleski import choleski, choleskiSol

def main():
    a = array([[4.0, -2.0, 2.0], \
               [-2.0, 2.0, -4.0], \
               [2.0, -4.0, 11.0]])
    
    b = array([ 6.0,  -10.0,  27.0])

    #print a
    L = choleski(a)              # L is a pointer to the modified a
    #print a
    x = choleskiSol(L,b)         # x is a pointer to the modified b 
    print (x)
    input("\nPress return to exit")
    
# end of main()    

if __name__ == '__main__':
    main()
# end if