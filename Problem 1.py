#Project Euler Problem 1
"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

import timeit                               #To time my function
start = timeit.default_timer()

n = 0                                       #Defining variables


for i in range(0, 1000):                    #Create list of all multiples of 3 and add them

    if i % 3 == 0 or i % 5 == 0:
        n = n + i


print (n)


stop = timeit.default_timer()
print ("Script runtime was " + str((stop - start) * 1000) + " ms.")




