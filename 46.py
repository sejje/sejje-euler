from primes import prime_list, isprime, prime_list2
from itertools import product

primes = prime_list2(10000)
composites = [i for i in xrange(3, 10000, 2) if not isprime(i)]
square2 = [2 * i * i for i in xrange(1, 100)]
sums = list(set(sum(c) for c in product(primes, square2) if sum(c) % 2))
sums.sort()
print sums[:25]

print [c for c in composites if not c in sums][:25]

result = False
