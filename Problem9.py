##Special Pythagorean triplet
##Problem 9
##A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##
##a^2 + b^2 = c^2
##For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
##
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.

import time
from math import sqrt

s = time.time()

for i in range(0, 1000):
    
    for j in range(i, int(i/2), -1):
        
        k = sqrt((i*i + j*j))
        if i + j + k == 1000:
            
            print(i,j,int(k))
            print(int(i*j*k))
            print(str(1000 * round(time.time() - s,6)) + ' ms')
            input('\nPress any key to exit.')
            raise SystemExit

    
    
