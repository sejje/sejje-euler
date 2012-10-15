'''
Project Euler #7

Find the 10001st Prime
'''

from primes import prime_list

primes = prime_list(500000)

prime_count = 1
x = 2
while x < 100001:
	x += 1
	if primes[x]:
		prime_count += 1

print x
