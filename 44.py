import math

def pentagonal(n):
	return n * (3 * n - 1) / 2

def is_pentagonal(n):
	# if X is a natural number, return True
	x = ((math.sqrt(24 * n + 1) + 1) / 6)
	return int(x) == x
			
for i in xrange(1, 9999999):
	if is_pentagonal(i):
		for x in xrange(1, i):
			if is_pentagonal(x):
				if is_pentagonal(i - x):
					if is_pentagonal(i + x):
						print i, x, abs(i - x)

