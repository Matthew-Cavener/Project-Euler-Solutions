#Smallest multiple: 2520 is the smallest number that can be divided by
#each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all
#of the numbers from 1 to 20?

import numpy as np
import time


def euler5(n,x):

    a = np.zeros(shape=(10000000000, x))

    for i in range(n, 1000000000, n):
        for j in range(1,x):

            #if i % j != 0: StopIteration
            
            a[i,j] = i % j
            
        if sum(a[i]) == 0:
            break
    return i


q = 20 #int(input('Evenly divisible by all numbers up to what? '))

print('Processing... \n')
start = time.time()

n =1
for x in range(1, q + 2):
    n = euler5(n, x)
    
end = time.time()
print(n)
print('cpu time = ' + str(round(end-start,5)) + ' seconds.')

