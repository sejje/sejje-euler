from fractions import *

def test_curious(num, den):
	f = Fraction(num, den)
	if not f < 1:
		return False

	try:
		if str(num)[1] == str(den)[0]:
			if Fraction(int(str(num)[0]), int(str(den)[1])) == f:
				if num % 11:
					return True
	except ZeroDivisionError:
		pass

start = Fraction(1, 1)
for num in xrange(10, 100):
	for den in xrange(10, 100):
		if test_curious(num, den):
			start *= Fraction(num, den)
print start
