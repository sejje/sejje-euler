from math import factorial as fact
from itertools import product

def ways(n, r):
	return fact(n) / (fact(r) * fact(n - r))

count = 0
for n in xrange(23, 101):
	for r in xrange(1, n + 1):
		if ways(n, r) > 1000000:
			count += 1
print count
