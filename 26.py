from decimal import Decimal, getcontext

getcontext().prec = 3000


def detect_repeat(string):
	for start in range(1, len(string)):
		for length in range(1, len(string)):
			end = length + start
			start2 = end + 1
			end2 = start2 + length
			start3 = end2 + 1
			end3 = start3 + length
			pre = string[start:end]
			test = string[start2:end2]
			test2 = string[start3:end3]
			if pre == test == test2:
				return pre
	return ""

record = (0, 0)
for i in xrange(1, 1000):
	x = Decimal(1) / Decimal(i)
	y = len(detect_repeat(str(x)))
	#print i, y 
	if y > record[1]:
		record = (i, y)
		print record

print detect_repeat(str(Decimal(1) / Decimal(983)))
