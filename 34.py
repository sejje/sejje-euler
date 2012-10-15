import math

def sum_fact(num):
	num_digits = [int(digit) for digit in str(num)]
	return sum([math.factorial(digit) for digit in num_digits])

results = []
for i in xrange(3, 999999):
	if sum_fact(i) == i:
		results.append(i)

print sum(results)
