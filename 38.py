def is_pandigital(number):
	number = str(number)
	if not len(number) == 9:
		return False
	number = list(number)
	if len(set(number)) == 9 and len(number) == 9 and not 0 in number:
		return True
	else:
		return False

print is_pandigital(1234)
print is_pandigital(123456789)
print is_pandigital(1234567890)
print is_pandigital(1123456789)

record = 0
for i in xrange(1, 200000):
	final = str(i)
	count = 1
	while len(final) < 9:
		count += 1
		final = final + str(i * count)
		if is_pandigital(final):
			print final
			if int(final) > record:
				record = final
print record
