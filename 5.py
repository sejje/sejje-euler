"""
Project Euler Problem 5

What's the smallest positive number that is
evenly divisible by all of the numbers
from 1 to 20?

"""

maxnum = 11
found = False
x = 0

while found == False:
	x = x + maxnum
	nums = []
	for i in range(1,maxnum + 1):
		if not x % i:
			nums.append(i)
			if len(nums) == maxnum:
				print(nums)
				found = True
				print "Found number: %d " % x
