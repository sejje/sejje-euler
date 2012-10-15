'''
Project Euler Problem 10

Learned how a sieve works and then whipped this baby up.
'''
import time
import math

def sum_primes(maxnum):
	grid = [True] * maxnum #make grid of Trues to test primes
	total = 2 #start total at 2
	num_primes = 1
	for num in xrange(3, maxnum + 1, 2):
		if grid[num] == True:
			total += num
			num_primes += 1
			for i in xrange(num, maxnum, num):
				grid[i] = False
	return total, num_primes


start = time.time()
print sum_primes(2000000), time.time() - start
