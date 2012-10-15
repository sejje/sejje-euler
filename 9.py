'''
given a^2 + b^2 = c^2, find the product of a, b, c when
a + b + c = 1000

'''
import math

for a in range(1, 500):
	for b in range(1, 500):
		c = math.sqrt(a * a + b * b)
		if not c % 1:
			if a + b + c == 1000: #check that they qualify
				print int(a * b * c)

sets = [(a * a, b * b, math.sqrt(a * a + b * b)) for a in range(1, 500) for b in range(1, 500) if not math.sqrt(a * a + b * b) % 1]
for group in sets:
    if group[0] + group[1] + group[2] == 1000:
        print group
