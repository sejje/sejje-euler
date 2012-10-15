'''
Project Euler Problem 16

What is the sum of the digits of the number 2^1000?
'''

count = 0
num = 2
for i in xrange(1, 1000):
	count += 1
	num *= 2

print num

total = 0
for i in xrange(0, len(str(num))):
	total += int(str(num)[i:i+1])

print total
