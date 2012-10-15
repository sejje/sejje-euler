import math, itertools

def factorize(num):
    factors = [1, num]
    for i in range(2, int(math.sqrt(num))+ 1):
        if not num % i:
            factors.append(i)
            factors.append(num / i)
    return list(set(factors))

def isprime(num):
	if num == 2: return True
	if not num % 2: return False
	divisor = 3
	sqrt_divided = int(math.sqrt(num))
	for i in xrange(3, sqrt_divided + 1, 2):
		if not num % i:
			return False
	return True

def prime_factors(num):
    results = []
    for i in factors(num):
        if isprime(i):
            results.append(i)
    return results

def prime_list(max_number):
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

def prime_list_numbers(max_number):
    primers = prime_list(max_number)
    primes = []
    for i in xrange(2, max_number):
        if primers[i]:
            primes.append(i)
    return primes

def next_prime(num):
	#find the next prime given num
	prime = False
	while not prime:
		num += 1
		prime = isprime(num)
	return num

def is_pandigital(number):
	number = list(str(number))
	if len(number) < 10:
		return len(set(number)) == len(number) == int(max(number)) and not '0' in number
	else:
		return len(set(number)) == len(number) == int(max(number)) + 1
