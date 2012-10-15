'''
Project Euler problem 10

Calculate the sum of all the primes
below two million
'''

maxnum = 2000000
from primes import isprime as isp

def isprime(num):
	for i in xrange(2, int(num/2) + 1, 2):
		if not num % i:
			return False
	print num
	return True

import math
def isprime2(num):
	divisor = 3
	sqrt_divided = int(math.sqrt(num))
	while divisor <= sqrt_divided:
		if num % divisor == 0:
			return False
		divisor += 2
	print num
	return True

def sum_primes(maxnum):
	total = 5 #running total
	num = 5 #number to test for prime-ness
	while num <= maxnum:
		if isp(num):
			total += num
		num += 2
	return total

import time
start = time.time()
print sum_primes(2000000)
print time.time() - start
