from primes import isprime
from eulertools import is_pandigital

import time
start = time.time()
record = 0
for number in xrange(1, 7654322):
	if is_pandigital(number):
		if isprime(number):
			record = number
print record, time.time() - start
