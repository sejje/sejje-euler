from eulertools import prime_list_numbers
import math

def f1(number):
    primes = prime_list_numbers(math.sqrt(number))
    for prime in primes:
        if not number % prime:
            print prime

f1(13195)
f1(600851475143)

