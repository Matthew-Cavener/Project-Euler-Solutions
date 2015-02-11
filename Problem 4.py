#Project Euler Problem 4

"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

import timeit                               #To time my function
start = timeit.default_timer()



k = 0


for i in range (999,900,-1):
    for j in range (999,900,-1):
        n = i * j
        a = str(n)
        if n > k:
            if a == a[::-1]:
                k = i * j

print (k)

stop = timeit.default_timer()
print ("Script runtime was " + str((stop - start) * 1000) + " ms.")
