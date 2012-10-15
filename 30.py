total = 0
for i in xrange(10, 999999):
	minitotal = 0
	for istr in str(i):
		minitotal += int(istr)**5
	if minitotal == i:
		print i
		total += minitotal
print total

