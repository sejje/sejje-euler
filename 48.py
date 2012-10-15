'''
Project Euler Project 48

Find the last ten digits of 1^1 + 2^2...+1000^1000
'''
total = 0
for i in range(1, 1001):
	total += i ** i

total = str(total)
print total[-10:len(str(total))]
