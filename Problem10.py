##Summation of primes
##Problem 10
##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
##Find the sum of all the primes below two million.

from sympy import sieve
import time

s = time.time()

print(sum(sieve.primerange(0,2000000)))
print(round(time.time() - s,5))

