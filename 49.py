from primes import isprime

def check_for_sequence(primelist, start):
    if start + 6660 > 9999:
        return False
    if not start in primelist:
        return False
    if not start + 3330 in primelist:
        return False
    if not start + 6660 in primelist:
        return False
    return True

primelist = []
for i in xrange(1000, 10000):
	if isprime(i):
		primelist.append(i)

def get_starts(primelist):
    results = []
    for i in primelist:
        if check_for_sequence(primelist, i):
            results.append(i)
    return results

def check_permutations(number):
    '''
    Specialized function to see if a number,
    when increased by 3330 is a permutation of itself
    '''
    num2 = number + 3330
    if set(list(str(num2))) == set(list(str(number))):
        return True
    return False
    
print len(primelist)
print check_for_sequence(primelist, 1487)
print check_permutations(1009)
print check_permutations(1487)
#print get_starts(primelist)

for prime in get_starts(primelist):
    if check_permutations(prime):
        if check_permutations(prime + 3330):
            print prime, prime + 3330, prime + 6660
