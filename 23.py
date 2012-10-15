import math
from eulertools import factors

def is_abundant(num):
	if not num % 2 or not num % 3:
		return sum(factors(num)) > num

abundants = []
for i in xrange(1, 28124):
	if is_abundant(i):
		abundants.append(i)
		
sums = range(28123)
for num in abundants:
	for num2 in abundants:
		if num + num2 >= 28123:
			break
		sums[num + num2] = 0


print sum(sums)
