def get_next(number):
	number = str(number)
	total = 0
	for i in range(len(number)):
		x = int(number[i])
		total += x * x
	return total

total = 0
for number in xrange(1,10000001):
	if not number % 10000:
		print number
	
	while not number == 89 and not number == 1:
		number = get_next(number)
	if number == 89:
		total += 1
		
print total
