f = open('13-numbers.txt', 'r')

total = 0
for line in f:
	num = int(line)
	total += num

total = str(total)
print len(total)
print total[0:10]
