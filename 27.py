from eulertools import isprime

record = 0
keys = (0, 0)
for a in xrange(-999, 1001, 2):
	for b in xrange(-999, 1001, 2):
		n = 0
		while isprime(abs(n**2 + a * n + b)):
			n += 1
		if n > record:
			print "New record %d consecutive primes, keys %d and %d" % (n, a, b)
			record = n
			keys = (a, b)
print record, keys
print keys[0] * keys[1]


