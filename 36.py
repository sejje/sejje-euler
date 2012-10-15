from palindrome import palindrome

dbl = []
for i in xrange(1, 1000000):
	if palindrome(str(i)):
		if palindrome(str(bin(i))[2:]):
			dbl.append(i)

print sum(dbl)
