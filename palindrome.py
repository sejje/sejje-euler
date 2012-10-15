def palindrome(string):
	'''
	Test a string for palindrome-ity
	This is case-sensitive
	'''
	palin = True
	for i in range(len(string) - 1):
		if not string[i] == string[len(string) - i - 1]:
			palin = False
	return palin

def palindrome_tests():
	print palindrome("Jesse")
	print palindrome("radar")
	print palindrome("Radar")
	print palindrome("123321")
	print palindrome("12321")
	print palindrome("11")
	print palindrome("1")

'''
from primes import prime_list
primes = prime_list(100000)
for i in xrange(1, 100001):
	if primes[i]:
		if palindrome(str(i)):
			print i
'''
