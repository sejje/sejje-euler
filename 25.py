'''
Project Euler Problem 25

Find the first term in the Fibonacci sequence with 1000 digits
'''

x = 1
y = 1
count = 2
while len(str(x)) < 1000:
	new = x + y
	y = x
	x = new
	count += 1

print len(str(x))
print count

	


