"""
Add all the natural numbers below one-thousand that
are multiples of 3 or 5
"""
from timer import timer

@timer
def f1():
	"""
	this is the classic, textbook solution
	"""
	total = 0
	for i in xrange(1,1000):
		if (i % 5 == 0) or (i % 3==0):
			total += i
	print total

@timer
def f2():
	"""
	attempt at a faster solution
	create two lists, merge the lists
	"""
	print sum(set(xrange(0, 1000, 5)) | set(xrange(0, 1000, 3)))
	
@timer
def f3():
	fives = [5]
	while fives[-1] < 995:
		fives.append(fives[-1] + 5)
	
	threes = [3]
	while threes[-1] < 999:
		threes.append(threes[-1] + 3)
	total = sum(set(fives) | set(threes))
	print total

@timer
def f4():
	print sum(x for x in xrange(1, 1000)
			  if not x % 3 or not x % 5)
	

f1
f2
f3
f4
