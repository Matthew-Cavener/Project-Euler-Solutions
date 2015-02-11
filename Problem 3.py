#Project Euler Problem 3

"""

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""
import timeit                               #To time my function
start = timeit.default_timer()

n = 600851475143
i = 2

while i * i < n:

    while n % i == 0:
        n = n / i
        
    i = i + 1
    
print (n)

stop = timeit.default_timer()
print ("Script runtime was " + str((stop - start) * 1000) + " ms.")
