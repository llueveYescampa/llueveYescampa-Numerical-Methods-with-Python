#!/usr/bin/python3
## Example 9_4

from numpy import array,dot, sqrt

def main():
    s = array([[-30.0, 10.0,20.0], \
               [10.0, 40.0, -50.0], \
               [ 20.0, -50.0, -10.0]])
    
    
    v = array([1.0, 0.0, 0.0])
    for i in range(100):
        vOld = v.copy()
        z = dot(s,v)
        zMag = sqrt(dot(z,z))
        v = z/zMag
        if dot(vOld,v) < 0.0:
            sign = -1.0
            v = -v
        else: 
            sign = 1.0
        # end if
        if sqrt(dot(vOld - v,vOld - v)) < 1.0e-6: 
            break
        # end if
    # end for
    lam = sign*zMag
    print ("Number of iterations =",i)
    print ("Eigenvalue =",lam)
    input("Press return to exit")    
# end of main()

if __name__ == '__main__':
    main()
# end
