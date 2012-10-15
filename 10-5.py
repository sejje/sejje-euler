import primes, time

start = time.time()

x = primes.prime_list(2000000)

total = 0
for i in xrange(1, 2000000):
	if x[i]:
		total += i

print total, time.time() - start
