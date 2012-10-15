def isprime(n):
	for x in xrange(2, int(n * 0.5), 2):
		if not n % x:
			return False
		return True

def highest_prime(num):
	if isprime(num):
		return num

	for x in xrange(2, int(n ** 0.5), 2):
		if not num % x:
			return highest_prime(num/x)


import time
start = time.time()
x = highest_prime(600851475143)
print x
print time.time() - start
