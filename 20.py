'''
Project Euler Problem 20

Find the sum of the digits of 100! (factorial)
'''

import math
value = math.factorial(100)

total = 0
for i in range(0,len(str(value))):
	total += int(str(value)[i:i+1])

print total
