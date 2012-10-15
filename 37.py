from primes import isprime

def get_trunks(string):
	le = len(string)
	return [string[x:] for x in range(le)] + [string[:-x] for x in range(le) if not string[:-x] == '']

def check_prime(list):
	#ensure all the members of a list are prime
	if all(isprime(int(number)) for number in list):
		return True
	return False

def get_eleven(max_num):
	#return [i in xrange(10, max_num) if check_prime(get_trunks(str(i)))]
	results = []
	for i in xrange(9, max_num, 2):
		if check_prime(get_trunks(str(i))):
			results.append(i)
	return len(results), sum(results)

print get_eleven(999999)
