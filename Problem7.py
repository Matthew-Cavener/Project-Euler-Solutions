##10001st prime
##Problem 7
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##
##What is the 10 001st prime number?

import time
import sympy

s= time.time()

print(sympy.ntheory.generate.prime(10001))

print(round(time.time() - s, 5))
