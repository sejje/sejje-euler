from eulertools import factors, isprime, prime_factors

def test_4(num):
    if len(prime_factors(num)) > 3:
        return True
    return False

for i in xrange(1, 10000000):
    if test_4(i):
        if test_4(i + 1):
            if test_4(i + 2):
                if test_4(i + 3):
                    print i
                    break
