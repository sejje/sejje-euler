'''
Project Euler Problem 104

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
'''

import time
start = time.time()
x = 1
y = 1
count = 2
tester = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
	y, x = x, y+x
	count += 1

	if not count % 5000:
		print count, len(str(x)), time.time() - start
	if len(str(x)) > 1:
		front = list(str(x)[0:9])
		front.sort()
		if front == tester:
			print 'front hit:', count 
		back = list(str(x)[(len(str(x)) - 9):(len(str(x))) + 1])
		back.sort()
		if back == tester:
			print count, 'backhaw!'
		if front == tester and back == tester:
			break
print "found: count %s" % count
