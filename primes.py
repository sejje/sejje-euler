import math

def isprime(num):
	if num == 1: return False
	if num == 2: return True
	if not num % 2: return False
	divisor = 3
	sqrt_divided = int(math.sqrt(num))
	for i in xrange(3, sqrt_divided + 1, 2):
		if not num % i:
			return False
	return True

def prime_list2(max_number):
	grid = prime_list(max_number)
	primes = []
	for i in xrange(0, len(grid)) :
		if grid[i]:
			primes.append(i)
	return primes


def prime_list( max_number):
	# Find all the primes up to max_number
	grid = [True] * (max_number + 1) #set array of all numbers
	grid[0] = False
	grid[1] = False
	for i in xrange(2, max_number + 1, 2):
		grid[i] = False
	grid[2] = True
	for num in xrange(3, max_number + 1, 2):
		try:
			if grid[num] == True: #if we hit a new prime
				for i in xrange(num, max_number, num):
					if i != num:
						grid[i] = False #mark multiples of the prime as not-prime
		except:
			pass
	return grid

def next_prime(num):
	#find the next prime given num
	prime = False
	while not prime:
		num += 1
		prime = isprime(num)
	return num

'''
import time
start = time.time()
print prime_list(200)[0]
print time.time() - start
start = time.time()
print next_prime(2000000000003), time.time() - start

print isprime(8)
print isprime(2000000000048)
'''

'''
x = prime_list(200)
for i in (0, 200):
	try:
		if x[i]:
			print i
	except:
		pass
'''
