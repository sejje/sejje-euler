import math
import time

def is_prime(divided):
	if not divided % 2: return False
	divisor = 3
	sqrt_divided = int(math.sqrt(divided))
	while divisor <= sqrt_divided:
		if divided % divisor == 0:
			return False

		divisor += 2
	print divided
	return True

start = time.time()
print sum([2] + [x for x in xrange(3,2000000+1, 2) if is_prime(x)])
print time.time() - start

print is_prime(8)
