'''
Project Euler Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math, time

start = time.time()

def d(n):
	divisors = [1]
	for i in range(2, int(math.sqrt(n)) + 1):
		if not n % i:
			divisors.append(i)
			if n / i < n and n/i <> i:
				divisors.append(n / i)
	divisors.sort()
	return sum(divisors)

'''
maxnum = 10000
biglist = [(0, 0)]
for i in xrange(1, maxnum):
	summ = d(i)
	biglist.append((i, summ))

pairlist = []
total = 0
for i in xrange(1, maxnum):
	x = biglist[i][1]
	if x < maxnum:
		if biglist[x][1] == i and x <> i:
			if i < x:
				#pairlist.append((i, x))
				print i, x
			else:
				#pairlist.append((x, i))
				print x, i
			total += i + x


#pairlist = set(pairlist)
total = total / 2
#print pairlist
print "Total: %s " % total, time.time() - start

#tests
print d(5020)
print d(5564)
'''

total = 0
for i in xrange(1, 10000):
	x = d(i)
	if (d(x) == i):
		if (i !=x):
			total += i
print total, time.time() - start
