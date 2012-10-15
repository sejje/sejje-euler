'''
Project Euler Problem 14

To create a sequence:
If N is even, the next number is n/2
If N is odd, the next number is 3N + 1

When N is one, the sequence is complete.

Which starting number under one-million
produces the longest chain?
'''

def next(n):
	'''
	Create the next number
	'''
	if not n % 2:
		return n / 2
	return 3 * n + 1

def chain(n):
	'''
	Starting with N, create a chain
	'''
	chain = [n]
	while not n == 1:
		n = next(n)
		chain.append(n)
	
	return chain

def longest_chain():
	longest = 0
	for i in range(500001,1000000, 2):
		if not i % 10000:
			print i
			print "Current record: %d" % longest

		y = chain(i)
		x = len(y)
		#print y
		#print "Length: %d from digit %d\n" % (x, i)

		if x > longest:
			#print "%d > %d" % (x, longest)
			longest = x
			longest_start = i
			print "New Record: %d from digit %d" % (longest, longest_start)
			#print "longest length now from digit %d\n\n" % longest 
	return longest_start

import time
start = time.time()
print longest_chain()
print time.time() - start
