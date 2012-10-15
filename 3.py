"""
Project Euler problem 3

The prime factors of 13195 are 5, 7, 13, and 29

What is the largest prime factor of the number 600851475143?

"""

def isprime(num):
	if num == 2:
		return True
	if num == 3:
		return True

	for i in xrange(2, num / 2 + 1, 1):
		if not num % i:
			return False
	return True

def next_prime(num):
	"""
	Given number, compute the next prime number
	"""
	found = False
	x = num 
	while found == False:
		x = x + 1
		if isprime(x):
			found = x
	return found

def find_factor(num):
	if isprime(num):
		return num
	x = 2
	while num % x:
		x = next_prime(x)
	return num / x

def prime_factor(num):
	"""
	Prime Factorize given number
	"""
	factor = find_factor(num)
	while not isprime(factor):
		factor = find_factor(factor)

	return factor

import time
start = time.time()
x = prime_factor(60085147514342)
print x
print time.time() - start
