from eulertools import isprime

def rotate_once(string):
	string = str(string)
	'''rotate all the characters in a string one time to the left,
	so that "string" becomes "trings", "trings" becomes "ringst"
	'''
	return string[1:] + string[0]


def check_circular_prime(num):
	if not isprime(num):
		return False
	rotated = rotate_once(num)
	while not rotated == str(num):
		if not isprime(int(rotated)):
			return False
		rotated = rotate_once(rotated)
	return True

circulars = []
for i in xrange(2, 1000000):
	if check_circular_prime(i):
		circulars.append(i)
print len(circulars)
